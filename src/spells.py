import pygame
from functions import loadAndScaleImage
from settings import TILE_SIZE

class Spell():
    def __init__(self, screen: pygame.Surface, spellObjects: list, name: str, damage: int, cooldown: int) -> None:
        print(f"Loaded spell: {name}")
        self.screen: pygame.Surface = screen
        self.spellObjects: list = spellObjects
        self.name: str = name
        self.image: pygame.Surface = loadAndScaleImage(f"src/assets/img/spells/spell{self.name}.png", (TILE_SIZE / 2, TILE_SIZE / 2))
        self.damage: int = damage
        self.cooldown: int = cooldown
        self.currentCooldown: int = 0
        
# Spell with an immediate effect.
class SpellHitscan(Spell):
    def __init__(self, screen: pygame.Surface, spellObjects: list, name: str, damage: int, cooldown: int, range: int) -> None:
        super().__init__(screen, spellObjects, name, damage, cooldown)
        self.range: int = range

# Spell with a projectile.
class SpellProjectile(Spell):
    def __init__(self, screen: pygame.Surface, spellObjects: list, name: str, damage: int, cooldown: int, speed: float, lifetime: int) -> None:
        super().__init__(screen, spellObjects, name, damage, cooldown)
        self.speed: float = speed
        self.lifetime: int = lifetime
        
class SpellBurn(SpellHitscan):
    def __init__(self, screen, spellObjects) -> None:
        super().__init__(screen, spellObjects, name = "Burn", damage = 10, range = 200, cooldown = 30)
    
    def attack(self, target, pos) -> None:
        self.currentCooldown = self.cooldown
        self.spellObjects.append(Ray(self.screen, "src/assets/img/spells/spellBurn.png", pos, target, self.damage, self.range))

    def update(self) -> None:
        if self.currentCooldown > 0:
            self.currentCooldown -= 1

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
        self.image = loadAndScaleImage(particleDirectory, (8, 8))
        self.pos: pygame.Vector2 = pos
        self.target: pygame.Vector2 = target
        self.targetDrawPos: pygame.Vector2 = target
        self.damage: int = damage
        self.range: int = range
        
    def getTarget(self) -> pygame.Vector2:
        # Calculate the distance between pos and target. If the distance is greater than the range, return the point at the range.
        distance: float = self.pos.distance_to(self.target)
        if distance > self.range:
            target = self.pos + (self.target - self.pos).normalize() * self.range
        else:
            target = self.target
        return target
    
    def update(self, tileOffset) -> None:
        self.drawPos = self.pos - tileOffset
        self.targetDrawPos = self.getTarget() - tileOffset
    
    def draw(self) -> None:
        pass
        pygame.draw.line(self.screen, (255, 0, 0), self.drawPos, self.targetDrawPos, 3)
        # screen.blit(self.image, self.pos)