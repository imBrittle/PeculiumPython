import pygame

def loadAndScaleImage(path: str, scale: tuple) -> pygame.Surface:
    return pygame.transform.scale(pygame.image.load(path), scale)