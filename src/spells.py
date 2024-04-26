import pygame

class Spell():
    def __init__(self, name: str, damage: int, cooldown: float) -> None:
        print("Creating a new spell")
        self.name: str = name
        self.image: pygame.Surface = pygame.image.load(f"assets/spell{self.name}.png")
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
        super().__init__(name = "Burn", damage = 10, range = 10)
        