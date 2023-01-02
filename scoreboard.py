import pygame.font


class Scoreboard:
    """A class to report scoring and other game information"""

    def __init__(self, ai_settings, screen):
        """ Iniatilize score keeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.text_color = (30, 30, 30)
        self.font_big = pygame.font.SysFont(None, 72)
        self.font = pygame.font.SysFont(None, 48)
        self.font_small = pygame.font.SysFont(None, 30)
        # Render for the game over message
        self.msg_image = self.font_big.render('GAME OVER', True, self.text_color, self.ai_settings.bg_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.centerx = self.screen_rect.centerx
        self.msg_rect.top = self.screen_rect.centery / 2

    def draw_board(self):
        """Draw score and the rest of renders to the screen"""
        # Draw score
        score = str(self.ai_settings.score)
        score_image = self.font.render(score, True, self.text_color, self.ai_settings.bg_color)
        score_rect = score_image.get_rect()
        score_rect.right = self.screen_rect.right - 120
        score_rect.top = 20
        self.screen.blit(score_image, score_rect)
        # Draw level
        level = str(self.ai_settings.level)
        level_image = self.font.render(level, True, self.text_color, self.ai_settings.bg_color)
        level_rect = level_image.get_rect()
        level_rect.right = self.screen_rect.right - 20
        level_rect.top = 20
        self.screen.blit(level_image, level_rect)
        # Draw game active messages
        if self.ai_settings.game_active:
            msg1 = f'Deaths for next level: {str(self.ai_settings.level_hits - self.ai_settings.aliens_dead)}'
            try:
                accuracy = round(100 * self.ai_settings.aliens_hit / self.ai_settings.bullets_fired)
            except ZeroDivisionError:
                accuracy = 0
            msg2 = f'Aliens hit / Bullets fired = {str(self.ai_settings.aliens_hit)} / ' \
                   f'{str(self.ai_settings.bullets_fired)} = {str(accuracy)} %'
            msg1_image = self.font_small.render(msg1, True, self.text_color, self.ai_settings.bg_color)
            msg1_rect = msg1_image.get_rect()
            msg1_rect.centerx = self.screen_rect.centerx
            msg1_rect.top = 10
            msg2_image = self.font_small.render(msg2, True, self.text_color, self.ai_settings.bg_color)
            msg2_rect = msg2_image.get_rect()
            msg2_rect.centerx = self.screen_rect.centerx
            msg2_rect.top = 40
            self.screen.blit(msg1_image, msg1_rect)
            self.screen.blit(msg2_image, msg2_rect)
        # Draw game over message
        if self.ai_settings.game_over:
            self.screen.blit(self.msg_image, self.msg_rect)
