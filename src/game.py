import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, GAME_OVER_FONT
from functions import drawText, gameOver
from world import *
from menu import Menu

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock: pygame.time.Clock = pygame.time.Clock() 
        self.running: bool = True
        self.playing: bool = True

        self.menu = Menu(self.screen)
        
        #TODO: Move this to a function called from the menu.
        self.world: World = World(self.screen, sectors)
        self.world.generate("Shattered Desert")

    def handleEvents(self) -> None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_i:
                        print(self.world.tileOffset)

    def run(self) -> None:
        while self.running:
            # Event Handling
            self.handleEvents()

            if self.playing:
                # Update Game
                if self.world.player.isAlive:
                    self.world.update()
                    
                # Draw Game
                self.world.draw()
                if not self.world.player.isAlive:
                    gameOver(self.screen)
            else:
                # Update Menu
                self.menu.update()

                # Draw Menu
                self.menu.draw()
            
            # Game State Update
            pygame.display.update()
            self.clock.tick(FPS)