import pygame
import random
from player import Player
from entities import *
from settings import TILE_SIZE
from functions import loadAndScaleImage

class World:
    def __init__(self, screen) -> None:
        self.screen: pygame.Surface = screen
        print("Creating a new world")
        self.backgroundTiles: list = []
        self.foregroundTiles: list = []
        self.entities: list = []
        self.player: Player = None

    def generate(self, sector) -> None:
        print(f"Generating Sector: Shattered Desert")
        self.player: Player = Player(self.screen, "Player", (0, 0))
        self.entities.append(self.player)
        for y, row in enumerate(sectors["Shattered Desert"]):
            for x, tile in enumerate(row):
                # Foreground Tiles
                if tile == "r":
                    self.foregroundTiles.append(Stone(self.screen, x * TILE_SIZE, y * TILE_SIZE))
                else:
                    self.foregroundTiles.append(None)
                # Entities
                if tile == "p":
                    self.player.pos.xy = (x * TILE_SIZE, y * TILE_SIZE)
                # Background Tiles
                randInt: int = random.randint(0, 1)
                if randInt == 0:
                    self.backgroundTiles.append(Dirt(self.screen, x * TILE_SIZE, y * TILE_SIZE))
                elif randInt == 1:
                    self.backgroundTiles.append(Grass(self.screen, x * TILE_SIZE, y * TILE_SIZE))
                    
        
    def update(self) -> None:
        for tile in self.backgroundTiles:
            if tile:
                tile.update()
        for tile in self.foregroundTiles:
            if tile:
                tile.update()
        for entity in self.entities:
            entity.update()
        self.player.update()
    
    def draw(self) -> None:
        for tile in self.backgroundTiles:
            if tile:
                tile.draw()
        for tile in self.foregroundTiles:
            if tile:
                tile.draw()
        for entity in self.entities:
            entity.draw()
        self.player.draw()
            
class Tile:
    def __init__(self, screen: pygame.Surface, x: int, y: int) -> None:
        self.screen: pygame.Surface = screen
        self.x: int = x
        self.y: int = y
        self.image: pygame.Surface = loadAndScaleImage(f"src/assets/img/tiles/tile{self.name}.png", (TILE_SIZE, TILE_SIZE))
        
    def update(self) -> None:
        pass
    
    def draw(self) -> None:
        self.screen.blit(self.image, (self.x, self.y))
        
class Dirt(Tile):
    def __init__(self, screen: pygame.Surface, x: int, y: int) -> None:
        self.name: str = "Dirt"
        super().__init__(screen, x, y)
        
class Grass(Tile):
    def __init__(self, screen: pygame.Surface, x: int, y: int) -> None:
        self.name: str = "Grass"
        super().__init__(screen, x, y)
        
class Stone(Tile):
    def __init__(self, screen: pygame.Surface, x, y) -> None:
        self.name: str = "Stone"
        super().__init__(screen, x, y)
            
sectors: dict[str, list] = {"Shattered Desert": [
    "rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr",
    "r                              r",
    "r p                            r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "r                              r",
    "rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr",
]}