
# import pygame
# import pickle

# from core.player import Player

# class BotPlayer:
#     def __init__(self, screen, border, width, height):
#         self.player = Player(screen, border, width, height)
#         self.x = self.player.x
#         self.y = self.player.y
#         self.rectb = pygame.Rect(self.x, self.y, 40, 5)
#         self.modelo_carregado = self.coletar_dados_pkl()
#         self.acao_atual = 0

#     def coletar_dados_pkl(self):
#         with open('src/IA-Block-Bricks.pkl', 'rb') as arquivo:
#             modelo_carregado = pickle.load(arquivo)
#             return modelo_carregado

#     def bot_desenho_player(self):
#         pygame.draw.rect(self.player.screen, (200,10,90), (self.rectb))

#     def bot_executar_acoes(self):
#         if self.modelo_carregado is not None and size(self.modelo_carregado) > 0:
#             if self.acao_atual < size(self.modelo_carregado):
#                 acao = self.modelo_carregado[self.acao_atual]
#                 if acao == 'direita':
#                     self.x += 1
#                 elif acao == 'esquerda':
#                     self.x -= 1
#                 self.bot_desenho_player()
#                 self.acao_atual += 1
#             else:
#                 print("Todas as ações foram executadas.")

#         else:
#             raise ValueError("Algo deu errado na coleta de dados do modelo.")

#     def bot_reset_1(self):
#         self.x = self.width // 2 - 40 // 2
#         self.rect.x = self.x
#         self.acao_atual = 0
