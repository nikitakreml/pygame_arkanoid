import pygame


class Menu:
    def __init__(self, font_type, screen):
        self.opened = True
        self.restart = False
        self.load_scr = pygame.image.load('Assets/menu_load_screen.png')
        self.line_scr = pygame.image.load('Assets/menu_back_line.png')
        self.screen = screen
        self.font_type = font_type
        self.line_scr = pygame.transform.scale(self.line_scr, [self.screen.get_width(), self.screen.get_height()])
        self.load_scr = pygame.transform.scale(self.load_scr, [self.screen.get_width(), self.screen.get_height()])
        self.font = pygame.font.Font(font_type, 32)

        self.play_button = self.font.render('PLAY', True, (255, 255, 255))
        self.play_rect = self.play_button.get_rect()
        self.play_rect.x = self.screen.get_width() / 2
        self.play_rect.y = self.screen.get_height() / 2

        self.game_over = self.font.render('GAME OVER', True, (255, 255, 255))
        self.game_over_rect = self.game_over.get_rect()
        self.game_over_rect.x = self.screen.get_width() // 2
        self.game_over_rect.y = self.screen.get_height() // 2 - 100


    def create_text_field(self, text):
        text_field = self.font.render(text, True, (255, 255, 255))
        return text_field

    def text_render(self, text_to_render, position):
        self.screen.blit(text_to_render, position)

    def controls(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = e.pos
            if self.play_rect.x <= mouse_x <= self.play_rect.right and self.play_rect.top <= mouse_y <= self.play_rect.bottom:
                self.opened = False

            if self.game_over_rect.x <= mouse_x <= self.game_over_rect.right and self.game_over_rect.top <= mouse_y <= self.game_over_rect.bottom:
                self.opened = False
                self.restart = True

