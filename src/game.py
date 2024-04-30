import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, GAME_OVER_FONT
from functions import drawText, gameOver
from world import *

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock: pygame.time.Clock = pygame.time.Clock() 
        self.running: bool = True
        
        self.world: World = World(self.screen, sectors)
        self.world.generate("Shattered Desert")
    
    def run(self) -> None:
        while self.running:
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_i:
                        print(self.world.tileOffset)
            
            # Update
            if self.world.player.isAlive:
                self.world.update()
                
            # Draw
            self.world.draw()
            if not self.world.player.isAlive:
                gameOver(self.screen)
            
            # Game State Update
            pygame.display.update()
            self.clock.tick(FPS)