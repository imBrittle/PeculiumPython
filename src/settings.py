import pygame
import sys

pygame.font.init()

# Display
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
FPS = 60
# Tiles
TILE_SIZE = 64
# Fonts
DEFAULT_FONT_SIZE = 32
GAME_OVER_FONT_SIZE = 128

DEFAULT_FONT = pygame.font.Font("src/assets/fonts/Ancient.ttf", DEFAULT_FONT_SIZE)
GAME_OVER_FONT = pygame.font.Font("src/assets/fonts/Ancient.ttf", GAME_OVER_FONT_SIZE)