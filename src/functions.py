import pygame

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