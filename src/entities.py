import pygame

class Entity:
    def __init__(self, screen: pygame.Surface, tileOffset: pygame.Vector2, name: str, pos: pygame.Vector2, maxHealth: int, maxSpeed: pygame.Vector2, multiplier: tuple = (1, 1)):
        print(f"Creating new entity: {name}")
        self.screen = screen
        self.tileOffset: pygame.Vector2 = tileOffset
        # Details
        self.name: str = name
        self.image: pygame.Surface = pygame.image.load(f"src/assets/img/entities/entity{self.name}.png")
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
    
    def draw(self, tileOffset: pygame.Vector2) -> None:
        self.screen.blit(self.image, self.drawPos)

class HostileEntity(Entity):
    def __init__(self, name, pos, health):
        super().__init__(name, pos, health)

class NeutralEntity(Entity):
    def __init__(self, name, pos, health, damage):
        super().__init__(name, pos, health, damage)

class PassiveEntity(Entity):
    def __init__(self, name, pos, health):
        super().__init__(name, pos, health, 0)

class BossEntity(Entity):
    def __init__(self, name, pos, health, damage):
        super().__init__(name, pos, health, damage)
        
# Specific Entities
class PyrusSpirit(HostileEntity):
    def __init__(self, screen: pygame.Surface, tileOffset: pygame.Vector2, pos: pygame.Vector2, multiplier: tuple = (1, 1)) -> None:
        super().__init__(screen, tileOffset, "PyrusSpirit", pos)