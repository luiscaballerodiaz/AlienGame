import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage the bullets fired by the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at ship current position"""
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        # Create a bullet rect at (0, 0) and then set it to ship position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.centery = ship.rect.centery
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up to the screen"""
        self.y -= self.ai_settings.bullet_speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """"Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.ai_settings.bullet_color, self.rect)
