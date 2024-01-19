

import pygame
from pygame.locals import *


class Fontes:
    def __init__(self, jogo_base=object):
        self.jogo_base = jogo_base
        self._fonte_impact = pygame.font.SysFont("impact", 28)
        self._fonte_candara = pygame.font.SysFont('Candara', 30, True, False)
        self._fonte_arial = pygame.font.SysFont('arial', 32, True, False)
        self._fonte_times_new_roman = pygame.font.SysFont('times new roman', 25, True, False)
        self._fonte_colibri = pygame.font.SysFont('colibri', 30, False, False)

        