import pygame
from spells import *
from settings import TILE_SIZE
from functions import loadAndScaleImage

class Player():
    def __init__(self, screen, name, pos) -> None:
        print("Creating a new player")
        self.screen: pygame.Surface = screen
        # Details
        self.name: str = name
        self.image: pygame.Surface = loadAndScaleImage("src/assets/img/entities/playerTemp.png", (TILE_SIZE, TILE_SIZE))
        self.pos: pygame.Vector2 = pygame.Vector2(pos)
        # Stats
        self.maxHealth: int = 100
        self.health: int = self.maxHealth
        self.maxSpeed: float = 5
        self.speed: float = self.maxSpeed
        # Spells
        self.spellPrimeOne: SpellBurn
        # States
        self.isAlive: bool = True
        
    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print("Move")
                if event.key == pygame.K_w:
                    self.pos.y -= self.speed
                if event.key == pygame.K_s:
                    self.pos.y += self.speed
                if event.key == pygame.K_a:
                    self.pos.x -= self.speed
                if event.key == pygame.K_d:
                    self.pos.x += self.speed
        
        
    def draw(self) -> None:
        self.screen.blit(self.image, self.pos)