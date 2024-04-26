import pygame
from player import Player
from entities import *
from settings import TILE_SIZE

class World:
    def __init__(self, screen) -> None:
        self.screen: pygame.Surface = screen
        print("Creating a new world")
        self.tiles: list = []
        self.entities: list = []
        self.player: Player = None

    def generate(self, sector) -> None:
        print("Generating {sector}")
        self.player: Player = Player("Player")
        self.entities.append(self.player)
        for y, row in enumerate(sector):
            for x, tile in enumerate(row):
                # Tiles
                if tile == "r":
                    self.tiles.append(Rock(x * TILE_SIZE, y * TILE_SIZE))
                # Entities
                if tile == "p":
                    self.player.pos.xy = (x * TILE_SIZE, y * TILE_SIZE)
        
    def update(self) -> None:
        for tile in self.tiles:
            tile.update()
        for entity in self.entities:
            entity.update()
    
    def draw(self) -> None:
        for tile in self.tiles:
            tile.draw()
        for entity in self.entities:
            entity.draw()
            
class Tile:
    def __init__(self, screen, x, y) -> None:
        self.screen: pygame.Surface = screen
        self.x: int = x
        self.y: int = y
        self.image: pygame.Surface = pygame.image.load(f"assets/tiles/tile{self.name}.png")
        
    def update(self) -> None:
        pass
    
    def draw(self) -> None:
        self.screen.blit(self.image, (self.x, self.y))
        
class Dirt(Tile):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.name: str = "Dirt"
        
class Grass(Tile):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.name: str = "Grass"
        
class Rock(Tile):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.name: str = "Rock"
            
SECTOR_0: list = [
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
]