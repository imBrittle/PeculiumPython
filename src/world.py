import pygame
import random
from player import Player
from entities import *
from settings import TILE_SIZE
from functions import loadAndScaleImage, onScreen

class World:
    def __init__(self, screen, sectors) -> None:
        self.screen: pygame.Surface = screen
        print("Creating a new world")
        self.backgroundTiles: list = []
        self.foregroundTiles: list = []
        self.entities: list = []
        self.player: Player = None
        self.tileOffset: pygame.Vector2 = pygame.Vector2(0, 0)
        self.sectors: dict = sectors
        self.tileCount: tuple = (0, 0)

    def generate(self, sector) -> None:
        print(f"Generating Sector: {sector}")
        self.player: Player = Player(self.screen, "Player", (0, 0))
        tileCountX: int = 0
        tileCountY: int = 0
        for y, row in enumerate(sectors[sector]):
            tileCountX = 0
            tileCountY += 1
            for x, tile in enumerate(row):
                tileCountX += 1
                # Foreground Tiles
                if tile == "r":
                    self.foregroundTiles.append(Stone(self.screen, x * TILE_SIZE, y * TILE_SIZE))
                else:
                    self.foregroundTiles.append(None)
                # Entities
                if tile == "p":
                    self.player.pos.xy = (x * TILE_SIZE, y * TILE_SIZE)
                if tile == "s":
                    self.entities.append(PyrusSpirit(self.screen, (x * TILE_SIZE, y * TILE_SIZE)))
                # Background Tiles
                randInt: int = random.randint(0, 1)
                if randInt == 0:
                    self.backgroundTiles.append(Dirt(self.screen, x * TILE_SIZE, y * TILE_SIZE))
                elif randInt == 1:
                    self.backgroundTiles.append(Grass(self.screen, x * TILE_SIZE, y * TILE_SIZE))
        self.tileCount = (tileCountX, tileCountY)
        print("Tile Count: " + str(self.tileCount))
                    
        
    def update(self) -> None:
        for tile in self.backgroundTiles:
            if tile:
                tile.update(self.tileOffset)
        for tile in self.foregroundTiles:
            if tile:
                tile.update(self.tileOffset)
        for entity in self.entities:
            entity.update(self.tileOffset)
        self.tileOffset = self.player.update(self.tileOffset, self.tileCount)
    
    def draw(self) -> None:
        for tile in self.backgroundTiles:
            if tile:
                tile.draw(self.tileOffset)
        for tile in self.foregroundTiles:
            if tile:
                tile.draw(self.tileOffset)
        for entity in self.entities:
            entity.draw(self.tileOffset)
        self.player.draw(self.tileOffset)
            
class Tile:
    def __init__(self, screen: pygame.Surface, x: int, y: int) -> None:
        self.screen: pygame.Surface = screen
        self.x: int = x
        self.y: int = y
        self.image: pygame.Surface = loadAndScaleImage(f"src/assets/img/tiles/tile{self.name}.png", (TILE_SIZE, TILE_SIZE))
        
    def update(self, tileOffset) -> None:
        pass
    
    def draw(self, tileOffset) -> None:
        self.screen.blit(self.image, (self.x - tileOffset.x, self.y - tileOffset.y))
        
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
    "rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr",
    "r                                                              r",
    "r p   s                                                        r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "r                                                              r",
    "rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr",
]}