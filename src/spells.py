import pygame
from functions import loadAndScaleImage
from settings import TILE_SIZE

class Spell():
    def __init__(self, name: str, damage: int, cooldown: float) -> None:
        print("Creating a new spell")
        self.name: str = name
        self.image: pygame.Surface = loadAndScaleImage(f"assets/spell{self.name}.png", (TILE_SIZE / 2, TILE_SIZE / 2))
        self.damage: int = damage
        self.cooldown: int = cooldown
        self.currentCooldown: int = 0
        
# Spell with an immediate effect.
class SpellHitscan(Spell):
    def __init__(self, name: str, damage: int, range: float) -> None:
        super().__init__(name, damage)
        self.range = range

# Spell with a projectile.
class SpellProjectile(Spell):
    def __init__(self, name: str, damage: int, speed: float, lifetime: float) -> None:
        super().__init__(name, damage)
        self.speed = speed
        self.lifetime = lifetime
        
class SpellBurn(SpellHitscan):
    def __init__(self) -> None:
        super().__init__(name = "Burn", damage = 10, range = 200)
    
    def attack(self) -> None:
        #TODO: Check for mouse position and create a ray towards that location, limited by self.range.
        mousePos = pygame.mouse.get_pos()
        pass

    def update(self) -> None:
        #TODO: Check for cooldown status and other statuses.
        pass

    def draw(self) -> None:
        pass
        # screen.blit(self.image, self.pos)
        