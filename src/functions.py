import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_OVER_FONT

def loadAndScaleImage(path: str, scale: tuple) -> pygame.Surface:
    return pygame.transform.scale(pygame.image.load(path), scale)

def onScreen(screen: pygame.Surface, pos: pygame.Vector2, tileOffset: pygame.Vector2) -> bool:
    return pos.x > -tileOffset.x and pos.x < (screen.get_width() - tileOffset.x) and pos.y > -tileOffset.y and pos.y < (screen.get_height() - tileOffset.y)

def drawText(screen: pygame.Surface, text: str, pos: pygame.Vector2, font: pygame.font.Font, colour: tuple, backgroundColour: tuple) -> None:
    if not font:
        font = pygame.font.Font(None, 32)
    textSurface = font.render(text, True, colour)
    if backgroundColour:
        pygame.draw.rect(screen, backgroundColour, (pos.x, pos.y, textSurface.get_width(), textSurface.get_height()))
    screen.blit(textSurface, pos)
    
def gameOver(screen: pygame.Surface) -> None:
    text = "GAME OVER"
    text_surface = GAME_OVER_FONT.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    screen.blit(text_surface, text_rect)