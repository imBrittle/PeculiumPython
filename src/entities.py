import pygame

class Entity:
    def __init__(self, name, health, damage):
        # Details
        self.name: str = name
        self.image: pygame.Surface = pygame.image.load(f"assets/{self.name}.png")
        # Stats
        self.health = health
        self.damage = damage

    def attack(self, target):
        target.health -= self.damage
        # Attack animation

class HostileEntity(Entity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

class NeutralEntity(Entity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

class PassiveEntity(Entity):
    def __init__(self, name, health):
        super().__init__(name, health, 0)

class BossEntity(Entity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)