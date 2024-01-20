

import pygame
from pygame.locals import *
from pygame.font import Font


class Fontes:
    def __init__(self, jogo_base:object):
        self.jogo_base = jogo_base
        self.__font_cache = {}
        self._fonte_impact = self.get_fonts_system32('impact', 28)
        self._fonte_candara = self.get_fonts_system32('Candara', 30, True, False)
        self._fonte_arial = self.get_fonts_system32('arial', 32, True, False)
        self._fonte_times_new_roman = self.get_fonts_system32('times new roman', 25, True, False)
        self._fonte_colibri = self.get_fonts_system32('colibri', 30, False, False)

    def get_fonts_system32(self, nome=str, tamanho=int, negrito:bool=False, italico:bool=False) -> Font:

        key = (nome, tamanho, negrito, italico)

        if key not in self.__font_cache:
            self.__font_cache[key] = pygame.font.SysFont(nome, tamanho, negrito, italico)
        
        return self.__font_cache[key]