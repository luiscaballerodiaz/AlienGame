import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class to manage aliens and their movement"""

    def __init__(self, ai_settings, screen, ship, multiplier, shoots_to_die, image_path):
        """Create alien object and define its initial position"""
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Define the starting position top left of the screen
        self.rect.top = self.screen_rect.top + ship.rect.height
        self.rect.left = self.screen_rect.left
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Moving flags
        self.moving_right = True
        # Alien settings
        self.score = ai_settings.alien_score
        self.score_multiplier = multiplier
        self.shoots_to_die = shoots_to_die
        self.shoots_received = 0

    def draw_alien(self):
        """Draw the alien at its current position"""
        self.screen.blit(self.image, self.rect)

    def is_hit(self, bullet):
        if self.rect.left <= bullet.rect.left and self.rect.right >= bullet.rect.right and \
                not self.rect.bottom <= bullet.rect.top and not self.rect.top >= bullet.rect.bottom:
            self.shoots_received += 1
            return True
        return False

    def update(self):
        """Update alien position"""
        if self.moving_right:  # Moving right
            if self.rect.right >= self.screen_rect.right:
                self.moving_right = False
                self.y += self.ai_settings.alien_lines_down  # If at maximum screen limit, go to a lower line
            else:
                self.x += self.ai_settings.alien_speed_factor  # If not at screen limit, move right
        else:
            if self.rect.left <= self.screen_rect.left:
                self.moving_right = True
                self.y += self.ai_settings.alien_lines_down  # If at maximum screen limit, go to a lower line
            else:
                self.x -= self.ai_settings.alien_speed_factor  # If not at screen limit, move left
        self.rect.x = self.x
        self.rect.y = self.y
