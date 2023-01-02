import pygame


class Ship:
    """Class to manage all ship actions/methods and parameters/attributes"""

    def __init__(self, ai_settings, screen):
        """Ship initialization and sets the starting position"""
        # Load the image and get its rect
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Define the starting position bottom centered of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.x = float(self.rect.centerx)
        # Initialize moving flags
        self.moving_right = False
        self.moving_left = False

    def draw_ship(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)

    def is_hit(self, alien):
        if alien.rect.bottom >= self.screen_rect.bottom or (self.rect.centery <= alien.rect.bottom and
                                                            self.rect.left <= alien.rect.left and
                                                            self.rect.right >= alien.rect.right):
            return True
        return False

    def center_ship(self):
        """Update ship position to center"""
        self.rect.centerx = self.screen_rect.centerx
        self.x = self.rect.centerx

    def update(self):
        """Update ship position depending on user input"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.x
