import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from world import *

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock() 
        self.running = True
        
        self.world = World(self.screen)
        self.world.generate(SECTOR_0)
    
    def run(self) -> None:
        while self.running:
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Update
            self.world.update()
            # Draw
            self.world.draw()
            pygame.display.update()
            self.clock.tick(FPS)