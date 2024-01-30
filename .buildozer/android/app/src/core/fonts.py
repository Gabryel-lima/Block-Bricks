

import pygame
from pygame.locals import *
from pygame.font import Font


class Fonts:
    def __init__(self, jogo_base:object):
        self.jogo_base = jogo_base
        self.__font_cache = {}
        self.font_impact = self.get_fonts_system32('impact', 28)
        self.font_candara = self.get_fonts_system32('Candara', 30, True, False)
        self.font_arial = self.get_fonts_system32('arial', 32, True, False)
        self.font_times_new_roman = self.get_fonts_system32('times new roman', 25, True, False)
        self.font_colibri = self.get_fonts_system32('colibri', 30, False, False)

    def get_fonts_system32(self, name=str, size=int, bold: bool = False, iitalic: bool = False) -> \
            Font:

        key = (name, size, bold, iitalic)

        if key not in self.__font_cache:
            self.__font_cache[key] = pygame.font.SysFont(name, size, bold, iitalic)
        
        return self.__font_cache[key]