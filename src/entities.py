import pygame
from functions import loadAndScaleImage, drawText
from settings import TILE_SIZE

class Entity:
    def __init__(self, screen: pygame.Surface, tileOffset: pygame.Vector2, name: str, pos: pygame.Vector2, maxHealth: int, maxSpeed: pygame.Vector2, multiplier: tuple = (1, 1)):
        print(f"Creating new entity: {name}")
        self.screen = screen
        self.tileOffset: pygame.Vector2 = tileOffset
        # Details
        self.name: str = name
        self.image: pygame.Surface = loadAndScaleImage(f"src/assets/img/entities/entity{self.name}.png", (TILE_SIZE, TILE_SIZE))
        self.dimensions: pygame.Vector2 = pygame.Vector2(self.image.get_size())
        self.pos: pygame.Vector2 = pygame.Vector2(pos)
        self.posCentre: pygame.Vector2 = self.pos + self.dimensions.xy / 2
        self.drawPos: pygame.Vector2 = pygame.Vector2(pos)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.direction: pygame.Vector2 = pygame.Vector2(0, 0)
        # Stat Multiplier
        self.healthMultiplier: float = multiplier[0]
        self.damageMultiplier: float = multiplier[1]
        # Stats
        self.maxHealth: int = maxHealth * self.healthMultiplier
        self.health: int = self.maxHealth
        self.maxSpeed: pygame.Vector2 = maxSpeed
        self.speed: pygame.Vector2 = self.maxSpeed

    def attack(self, target):
        pass
        # Attack animation
        
    def update(self) -> None:
        #TODO: Cast a ray to player and check for collision. If no collision, pathfind/attack towards player
        
        self.pos += self.velocity
        # Update Centre Position
        self.posCentre = self.pos + self.dimensions.xy / 2
        # Update Draw Position
        self.drawPos = self.pos - self.tileOffset
        
    def drawUI(self) -> None:
        drawText(self.screen, f"{self.name}", self.posCentre, None, (255, 255, 255), None)
        drawText(self.screen, f"Health: {self.health}/{self.maxHealth}", self.posCentre + pygame.Vector2(0, 16), None, (255, 255, 255), None)
    
    def draw(self, tileOffset: pygame.Vector2) -> None:
        self.screen.blit(self.image, self.drawPos)

class HostileEntity(Entity):
    def __init__(self, screen: pygame.Surface, tileOffset: pygame.Vector2, name: str, pos: tuple, maxHealth: int, maxSpeed: int, multiplier: tuple = (1, 1)) -> None:
        super().__init__(screen, tileOffset, name, pos, maxHealth, maxSpeed, multiplier)

class NeutralEntity(Entity):
    def __init__(self, screen: pygame.Surface, tileOffset: pygame.Vector2, name: str, pos: tuple, maxHealth: int, maxSpeed: int, multiplier: tuple = (1, 1)):
        super().__init__(screen, tileOffset, name, pos, maxHealth, maxSpeed, multiplier)

class PassiveEntity(Entity):
    def __init__(self, screen: pygame.Surface, tileOffset: pygame.Vector2, name: str, pos: tuple, maxHealth: int, maxSpeed: int, multiplier: tuple = (1, 1)):
        super().__init__(screen, tileOffset, name, pos, maxHealth, maxSpeed, multiplier)

class BossEntity(Entity):
    def __init__(self, screen: pygame.Surface, tileOffset: pygame.Vector2, name: str, pos: tuple, maxHealth: int, maxSpeed: int, multiplier: tuple = (1, 1)):
        super().__init__(screen, tileOffset, name, pos, maxHealth, maxSpeed, multiplier)
        
# Specific Entities
class PyrusSpirit(HostileEntity):
    def __init__(self, screen: pygame.Surface, tileOffset: pygame.Vector2, pos: pygame.Vector2, multiplier: tuple = (1, 1)) -> None:
        super().__init__(screen, tileOffset, "PyrusSpirit", pos, 100, 5, multiplier)