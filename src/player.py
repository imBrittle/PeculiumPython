import pygame
from spells import *
from settings import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_FONT
from functions import loadAndScaleImage, drawText

class Player():
    def __init__(self, screen, tileOffset, spellObjects, name, pos) -> None:
        print(f"Loaded player: {name} @ {pos}")
        self.screen: pygame.Surface = screen
        # Details
        self.name: str = name
        self.image: pygame.Surface = loadAndScaleImage("src/assets/img/entities/playerTemp.png", (TILE_SIZE, TILE_SIZE))
        self.dimensions: pygame.Vector2 = pygame.Vector2(self.image.get_width(), self.image.get_height())
        self.pos: pygame.Vector2 = pygame.Vector2(pos)
        self.posCentre: pygame.Vector2 = self.pos + self.dimensions.xy / 2
        self.drawPos: pygame.Vector2 = pygame.Vector2(pos)
        self.drawPosCentre: pygame.Vector2 = self.drawPos + self.dimensions.xy / 2
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.direction: pygame.Vector2 = pygame.Vector2(0, 0)
        self.spellObjects: list = spellObjects
        self.tileOffset: pygame.Vector2 = tileOffset
        # Stats
        self.maxHealth: int = 100
        self.health: int = self.maxHealth
        self.maxSpeed: pygame.Vector2 = pygame.Vector2(8, 8)
        self.speed: pygame.Vector2 = self.maxSpeed
        # Spells
        self.spells = [SpellBurn(self.screen, self.spellObjects), None, None, None]
        self.activeSpell: Spell = self.spells[0]
        # States
        self.isAlive: bool = True
        
    def attack(self) -> None:
        mousePos: tuple = pygame.mouse.get_pos()
        offsetMousePos: tuple = mousePos[0] + self.tileOffset.x, mousePos[1] + self.tileOffset.y
        self.activeSpell.attack(offsetMousePos, self.posCentre)
        
    def update(self, tileCount: tuple) -> None:
        # Health
        if self.health <= 0:
            self.isAlive = False
        
        prevSpell = self.activeSpell.name if self.activeSpell else "None"
        # Key Input
        keys: list = pygame.key.get_pressed()
        mb: list = pygame.mouse.get_pressed(num_buttons = 5)
        # Movement
        self.direction.xy = (0, 0)
        if keys[pygame.K_w]:
            self.direction.y = -1
        if keys[pygame.K_s]:
            self.direction.y = 1
        if keys[pygame.K_a]:
            self.direction.x = -1
        if keys[pygame.K_d]:
            self.direction.x = 1
        # Spells
        if keys[pygame.K_q]:
            self.activeSpell = self.spells[0]
        if keys[pygame.K_e]:
            self.activeSpell = self.spells[1]
        if keys[pygame.K_c]:
            self.activeSpell = self.spells[2]
        if keys[pygame.K_x]:
            self.activeSpell = self.spells[3]
        if self.activeSpell and mb[0] and self.activeSpell.currentCooldown == 0:
            self.attack()
        if self.activeSpell:
            if self.activeSpell.name != prevSpell:
                print(f"Active Spell: {self.activeSpell.name}")
        else:
            if prevSpell != "None":
                print("Active Spell: None")
                
        # Dev Controls
        if keys[pygame.K_MINUS]:
            self.health -= 1
        if keys[pygame.K_EQUALS]:
            self.health += 1
        
        # Normalise Vector
        if self.direction.length() != 0:
            self.direction = self.direction.normalize()
        # Update Position
        self.velocity.xy = (self.direction.x * self.speed.x, self.direction.y * self.speed.y)
        
        # Update Tile Offset Y
        self.tileOffset.y = self.posCentre.y - SCREEN_HEIGHT / 2
        
        # Update Tile Offset X
        self.tileOffset.x = self.posCentre.x - SCREEN_WIDTH / 2
        
        # Clamp tileOffset within game world bounds
        horizontalPixels: int = TILE_SIZE * tileCount[0]
        verticalPixels: int = TILE_SIZE * tileCount[1]
        
        self.tileOffset.x = max(0, min(self.tileOffset.x, horizontalPixels - SCREEN_WIDTH))
        self.tileOffset.y = max(0, min(self.tileOffset.y, verticalPixels - SCREEN_HEIGHT))
        
        # Update Position
        self.pos += self.velocity
        self.posCentre = self.pos + self.dimensions.xy / 2
        # Update Draw Position
        self.drawPos = self.pos - self.tileOffset
        self.drawPosCentre = self.drawPos + self.dimensions.xy / 2
        
        # Update Spells
        for spell in self.spells:
            if spell:
                spell.update()
                
    def drawUI(self) -> None:
        # Draw Health Bar
        pygame.draw.rect(self.screen, (255, 0, 0), (10, 10, 200, 20))
        pygame.draw.rect(self.screen, (0, 255, 0), (10, 10, 200 * (self.health / self.maxHealth), 20))
        # Draw Active Spell
        if self.activeSpell:
            self.screen.blit(self.activeSpell.image, (SCREEN_WIDTH - 50, 10))
        drawText(self.screen, f"Active Spell: {self.activeSpell.name if self.activeSpell else 'None'}", (SCREEN_WIDTH - 250, 10), DEFAULT_FONT, (255, 255, 255), None)
        # Draw Cooldown
        if self.activeSpell:
            drawText(self.screen, f"Cooldown: {self.activeSpell.currentCooldown}", (SCREEN_WIDTH - 250, 40), DEFAULT_FONT, (255, 255, 255), None)
        # Draw Position
        drawText(self.screen, f"Position: {self.pos}", (10, 40), DEFAULT_FONT, (255, 255, 255), None)
        
    def draw(self) -> None:
        # Draw UI
        self.drawUI()
        # Draw Spells
        for spell in self.spells:
            if spell:
                spell.draw()
        # Draw Player
        self.screen.blit(self.image, self.drawPos)