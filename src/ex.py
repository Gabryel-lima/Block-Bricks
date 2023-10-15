import pygame
from pygame.math import Vector2

# Criar um vetor bidimensional
vetor = Vector2(3, 4)  # Isso representa um vetor com coordenadas (3, 4)

# Converter o vetor para coordenadas polares
polar = vetor.as_polar()

# A tupla "polar" conterá o ângulo (direção) e a magnitude (comprimento)
angulo_em_radianos, magnitude = polar

print(f"Ângulo em radianos: {angulo_em_radianos}")
print(f"Magnitude (comprimento): {magnitude}")
