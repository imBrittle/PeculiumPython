import pygame
from spells import *

class Player():
    def __init__(self, name, pos) -> None:
        print("Creating a new player")
        # Details
        self.name: str = name
        self.image: pygame.Surface = pygame.image.load("assets/player.png")
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
        print("Updating player")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.pos.y -= self.speed
                if event.key == pygame.K_s:
                    self.pos.y += self.speed
                if event.key == pygame.K_a:
                    self.pos.x -= self.speed
                if event.key == pygame.K_d:
                    self.pos.x += self.speed
        
        
    def draw(self) -> None:
        print("Drawing player")