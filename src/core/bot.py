import os
from pathlib import Path

import pygame
import numpy as np

class Bot:
    def __init__(self, game_base):
        self.game_base = game_base 
        self.pos_x = 280 # 280
        self.pos_y = 402 # 402
        self.width_draw_x = 40 # 40
        self.height_draw_y = 1 # 1
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width_draw_x, self.height_draw_y)
        self.model = None
        self.model_path = Path("hard_model.keras")
        self.keras_backend_enabled = os.getenv("BLOCK_BRICKS_ENABLE_KERAS_BOT", "0") == "1"
        self._model_load_attempted = False
    
    def draw_bot(self):
        pygame.draw.rect(self.game_base.screen, (20, 155, 40),
                         (self.pos_x, self.pos_y, self.width_draw_x, 5))

    def ensure_model_loaded(self):
        if self._model_load_attempted:
            return

        self._model_load_attempted = True

        if not self.keras_backend_enabled or not self.model_path.exists():
            self.model = None
            return

        self.load_weights()
        
    def load_weights(self):
        try:
            import keras
        except Exception:
            self.model = None
            return

        self.model = keras.models.load_model(self.model_path)
        print("Modelo carregado com sucesso...")
    
    def reset_bot(self):
        self.pos_x = self.game_base.width / 2
    
    def move_left(self):
        self.pos_x -= 5.0
    
    def move_right(self):
        self.pos_x += 5.0
    
    def fine_adjustment(self, distance_to_ball):
        if abs(distance_to_ball) < 25:
            if distance_to_ball < 0:
                self.pos_x -= 3.0
            elif distance_to_ball > 0:
                self.pos_x += 3.0
    
    def update(self):
        self.ensure_model_loaded()

        if self.model is None:
            self.follow_ball()
            return

        # Obtém a observação atual do estado do jogo
        state = self.get_observation()
        
        # Usa o modelo para prever a ação
        action_values = self.model.predict(np.expand_dims(state, axis=0))
        action = np.argmax(action_values[0])
        
        # Calcula a distância até a bola (você precisa implementar este cálculo)
        distance_to_ball = self.calculate_distance_to_ball()
        
        # Executa a ação correspondente
        if action == 0:
            self.move_right()
        elif action == 1:
            self.move_left()
        elif action == 2:
            self.fine_adjustment(distance_to_ball)

    def follow_ball(self):
        distance_to_ball = self.calculate_distance_to_ball()
        if distance_to_ball > 5:
            self.move_right()
        elif distance_to_ball < -5:
            self.move_left()
    
    def get_observation(self):
        obs = np.array(pygame.surfarray.array3d(self.game_base.screen_surface), dtype=np.float32) 
        obs /= 255.0 # Consegui usar a resolução de compressão 'screen_surface'
        return obs
    
    def calculate_distance_to_ball(self):
        # Implementa o cálculo da distância entre o jogador e a bola
        ball_center = self.game_base.ball.bola_Rect.centerx
        player_center = self.rect.centerx # self.pos_x + (self.width_draw_x / 2)
        distance = (ball_center - player_center)
        return distance
    
    def bot_collision(self):
        if self.pos_x - 5 <= self.game_base.border.left:
            self.pos_x = self.game_base.border.left + 5

        if self.pos_x + 45 >= self.game_base.border.right:
            self.pos_x = self.game_base.border.right - 45

        self.rect.x = self.pos_x
