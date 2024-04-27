import pygame

def loadAndScaleImage(path: str, scale: tuple) -> pygame.Surface:
    return pygame.transform.scale(pygame.image.load(path), scale)

def onScreen(screen: pygame.Surface, pos: pygame.Vector2, tileOffset: pygame.Vector2) -> bool:
    return pos.x > -tileOffset.x and pos.x < (screen.get_width() - tileOffset.x) and pos.y > -tileOffset.y and pos.y < (screen.get_height() - tileOffset.y)