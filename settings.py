class Settings:
    """Class to store all settings for the alien game"""

    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.name = 'ALIEN INVASION'
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed_factor = 2.5
        self.nships = 3
        # Bullets settings
        self.bullet_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 2
        self.bullets_fired = 0
        # Aliens setting
        self.alien_score = 5
        self.alien_shoots_to_die = 1
        self.alien_nmax = 6
        self.alien_speed_factor = 1
        self.alien_delta_speed = 0.05
        self.alien_max_speed = 1.5
        self.alien_lines_down = 60
        self.alien_delta_lines = 4
        self.alien_max_down = 100
        self.alien_spam_time_min = 1
        self.alien_spam_time_max = 2.5
        self.alien_delta_time = 0.15
        self.ini_time = 0
        self.spam_time = 0
        # Operational and score settings
        self.aliens_dead = 0
        self.aliens_hit = 0
        self.level_hits = 10
        self.score = 0
        self.level = 1
        self.game_active = False
        self.game_over = False
        # Create copies for initialization after reset
        self.bullets_fired_copy = self.bullets_fired
        self.alien_speed_factor_copy = self.alien_speed_factor
        self.alien_lines_down_copy = self.alien_lines_down
        self.alien_spam_time_max_copy = self.alien_spam_time_max
        self.aliens_dead_copy = self.aliens_dead
        self.aliens_hit_copy = self.aliens_hit
        self.score_copy = self.score
        self.level_copy = self.level

    def reset_settings(self):
        self.alien_spam_time_max = self.alien_spam_time_max_copy
        self.alien_lines_down = self.alien_lines_down_copy
        self.alien_speed_factor = self.alien_speed_factor_copy
        self.score = self.score_copy
        self.level = self.level_copy
        self.bullets_fired = self.bullets_fired_copy
        self.aliens_dead = self.aliens_dead_copy
        self.aliens_hit = self.aliens_hit_copy
