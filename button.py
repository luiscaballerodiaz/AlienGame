import pygame.font


class Button:
    """A class to create a button to control the game start"""

    def __init__(self, ai_settings, screen):
        """ Iniatilize button to start the game"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.width = 250
        self.height = 60
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 42)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

    def draw_button(self, msg):
        """Draw the start button in the screen"""
        button_image = self.font.render(msg, True, self.text_color, self.button_color)
        button_rect = button_image.get_rect()
        button_rect.center = self.rect.center
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(button_image, button_rect)
