import pygame
import sys
class Main:
    def __init__(self, scr_size):
        pygame.init()
        pygame.freetype.init()
        self.size = scr_size
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.process_stopped = False
        self.score = 0

    def quit(self, e):
        if e.type == pygame.QUIT:
            self.process_stopped = True
            sys.exit(0)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                self.process_stopped = True
                sys.exit(0)
