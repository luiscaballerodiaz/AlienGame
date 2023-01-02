import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from scoreboard import Scoreboard
from button import Button
import game_functions as gf


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.name)

    ship = Ship(ai_settings, screen)
    board = Scoreboard(ai_settings, screen)
    button = Button(ai_settings, screen)
    button.message = 'PLAY'
    bullets = Group()
    aliens = Group()
    lives = []
    gf.initialize_lives(ai_settings, screen, lives)

    # Start the main loop of the game
    while True:
        if ai_settings.game_active:
            pygame.mouse.set_visible(False)
        else:
            pygame.mouse.set_visible(True)
        gf.check_events(ai_settings, screen, ship, bullets, aliens, button, lives)  # Watch for user keyboad events
        gf.create_aliens_fleet(ai_settings, screen, aliens, ship)  # Manage the alien fleet creation
        gf.update_sprites(ai_settings, ship, aliens, bullets)  # Update position for sprites
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, lives, board, button)  # Update screen
        gf.check_end_game(ai_settings, aliens, ship, bullets, lives, button)  # End of game check


run_game()
