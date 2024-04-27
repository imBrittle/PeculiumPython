import pygame
from spells import *
from settings import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from functions import loadAndScaleImage

class Player():
    def __init__(self, screen, name, pos) -> None:
        print("Creating a new player")
        self.screen: pygame.Surface = screen
        # Details
        self.name: str = name
        self.image: pygame.Surface = loadAndScaleImage("src/assets/img/entities/playerTemp.png", (TILE_SIZE, TILE_SIZE))
        self.dimensions: pygame.Vector2 = pygame.Vector2(self.image.get_size())
        self.pos: pygame.Vector2 = pygame.Vector2(pos)
        self.posCentre: pygame.Vector2 = self.pos + self.dimensions.xy / 2
        self.drawPos: pygame.Vector2 = pygame.Vector2(pos)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.direction: pygame.Vector2 = pygame.Vector2(0, 0)
        # Stats
        self.maxHealth: int = 100
        self.health: int = self.maxHealth
        self.maxSpeed: pygame.Vector2 = pygame.Vector2(8, 8)
        self.speed: pygame.Vector2 = self.maxSpeed
        # Spells
        self.spellPrimeOne: Spell = None
        self.spellPrimeTwo: Spell = None
        self.spellSignature: Spell = None
        self.spellUltimate: Spell = None
        # States
        self.isAlive: bool = True
        
    def update(self, tileOffset: pygame.Vector2, tileCount: tuple) -> None:
        # Key Input
        keys: list = pygame.key.get_pressed()
        self.direction.xy = (0, 0)
        if keys[pygame.K_w]:
            self.direction.y = -1
        if keys[pygame.K_s]:
            self.direction.y = 1
        if keys[pygame.K_a]:
            self.direction.x = -1
        if keys[pygame.K_d]:
            self.direction.x = 1
        # Normalise Vector
        if self.direction.length() != 0:
            self.direction = self.direction.normalize()
        # Update Position
        self.velocity.xy = (self.direction.x * self.speed.x, self.direction.y * self.speed.y)
        # TODO: Scroll player when too far right or down
        # Update Tile Offset Y
        verticalPixels: int = TILE_SIZE * tileCount[1]
        if self.posCentre.y > (SCREEN_HEIGHT / 2) and self.posCentre.y < verticalPixels - (SCREEN_HEIGHT / 2):
            tileOffset.y += self.velocity.y
            
        # Update Tile Offset X
        horizontalPixels: int = TILE_SIZE * tileCount[0]
        if self.posCentre.x > (SCREEN_WIDTH / 2) and self.posCentre.x < horizontalPixels - (SCREEN_WIDTH / 2):
            tileOffset.x += self.velocity.x
        
        # Check this code here
        if tileOffset.x < 0:
            tileOffset.x = 0
        if tileOffset.x > horizontalPixels - SCREEN_WIDTH:
            tileOffset.x = horizontalPixels - SCREEN_WIDTH
        if tileOffset.y < 0:
            tileOffset.y = 0
        if tileOffset.y > verticalPixels - SCREEN_HEIGHT:
            tileOffset.y = verticalPixels - SCREEN_HEIGHT
            
        self.pos += self.velocity
        # Update Centre Position
        self.posCentre = self.pos + self.dimensions.xy / 2
        # Update Draw Position
        self.drawPos = self.pos - tileOffset
        return tileOffset
        
    def draw(self, tileOffset) -> None:
        self.screen.blit(self.image, self.drawPos)