import pygame
from entities import Projectile
from functions import loadAndScaleImage
from settings import TILE_SIZE

class Spell():
    def __init__(self, screen: pygame.Surface, name: str, damage: int, cooldown: float) -> None:
        print("Creating a new spell")
        self.screen = screen
        self.name: str = name
        self.image: pygame.Surface = loadAndScaleImage(f"src/assets/img/spells/spell{self.name}.png", (TILE_SIZE / 2, TILE_SIZE / 2))
        self.damage: int = damage
        self.cooldown: int = cooldown
        self.currentCooldown: int = 0
        
# Spell with an immediate effect.
class SpellHitscan(Spell):
    def __init__(self, screen: pygame.Surface, name: str, damage: int, range: float, cooldown: float) -> None:
        super().__init__(screen, name, damage, cooldown)
        self.range = range

# Spell with a projectile.
class SpellProjectile(Spell):
    def __init__(self, screen: pygame.Surface, name: str, damage: int, speed: float, lifetime: float) -> None:
        super().__init__(screen, name, damage)
        self.speed = speed
        self.lifetime = lifetime
        
class SpellBurn(SpellHitscan):
    def __init__(self, screen) -> None:
        super().__init__(screen, name = "Burn", damage = 10, range = 200, cooldown = 1.0)
    
    def attack(self, target, pos) -> None:
        self.currentCooldown = self.cooldown
        Ray(self.screen, "src/assets/img/spells/spellBurn.png", pos, target, self.damage, self.range, ) #TODO: Implement this

    def update(self) -> None:
        #TODO: Check for cooldown status and other statuses.
        pass

    def draw(self) -> None:
        pass
        # screen.blit(self.image, self.pos)
        
# Entities/Objects created through spells        
class Projectile(): #! Incomplete Method
    def __init__(self, screen: pygame.Surface, image: pygame.Surface, pos: pygame.Vector2, direction: pygame.Vector2, damage: int, lifetime: int) -> None:
        self.screen = screen
        self.image = loadAndScaleImage(image) #? Perhaps change this image to a dictionary
        self.pos: pygame.Vector2 = pos
        self.direction: pygame.Vector2 = direction
        self.velocity: pygame.Vector2 = direction # * speed
        self.damage: int = damage
        self.lifetime: int = lifetime
        self.remainingLifetime: int = self.lifetime
        
    def update(self) -> None:
        self.pos += self.velocity
        self.remainingLifetime -= 1
        
    def draw(self) -> None:
        self.screen.blit(self.image, self.pos)
        
class Ray():
    def __init__(self, screen: pygame.Surface, particleDirectory: str, pos: pygame.Vector2, target: pygame.Vector2, damage: int, range: int) -> None:
        self.screen = screen
        self.pos: pygame.Vector2 = pos
        self.target: pygame.Vector2 = target
        self.range: int = range
        self.update()
        self.draw()
    
    def update(self) -> None:
        pass
    
    def draw(self) -> None:
        pass
        pygame.draw.line(self.screen, (255, 0, 0), self.pos, self.pos + self.direction * self.range, 2) #! Fix this
        # screen.blit(self.image, self.pos)