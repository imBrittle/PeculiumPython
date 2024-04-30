import pygame
from functions import loadAndScaleImage

class Menu():
    def __init__(self, screen) -> None:
        self.screen: pygame.Surface = screen

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pass

class Title():
    def __init__(self) -> None:
        self.image: pygame.Surface = loadAndScaleImage("src/assets/img/ui/title.png", (400, 100))

class ShortButton(pygame.sprite.Sprite):
    def __init__(self, screen) -> None:
        self.screen: pygame.Surface = screen
        self.images: list[pygame.Surface] = [loadAndScaleImage("src/assets/img/ui/buttonUp.png", (96, 32)), loadAndScaleImage("src/assets/img/ui/buttonDown.png", (96, 32))]
        self.state: bool = False

    def update(self) -> None:
        pass

    def draw(self) -> None:
        self.screen.blit(self.images[self.state])

class LongButton(pygame.sprite.Sprite):
    def __init__(self) -> None:
        self.images: list[pygame.Surface] = [loadAndScaleImage("src/assets/img/ui/buttonUp1.png", (128, 32)), loadAndScaleImage("src/assets/img/ui/buttonDown1.png", (128, 32))]