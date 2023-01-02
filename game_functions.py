import sys
import pygame
import time
import random

from bullet import Bullet
from alien import Alien
from ship import Ship


def check_events(ai_settings, screen, ship, bullets, aliens, button, lives):
    """Watch for user keyboad events to act accordingly"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button.rect.left <= mouse_x <= button.rect.right and button.rect.top <= mouse_y <= button.rect.bottom:
                # If game did not start yet, enables alien creation after the first shoot
                if ai_settings.game_over:
                    initialize_lives(ai_settings, screen, lives)
                    ai_settings.reset_settings()
                if not ai_settings.game_active:
                    ai_settings.game_active = True
                    ai_settings.game_over = False
                    create_aliens_fleet(ai_settings, screen, aliens, ship)
        if ai_settings.game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    # Create new bullet and add it to the bullets group
                    if len(bullets) < ai_settings.bullet_allowed:
                        new_bullet = Bullet(ai_settings, screen, ship)
                        bullets.add(new_bullet)
                        ai_settings.bullets_fired += 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False


def create_aliens_fleet(ai_settings, screen, aliens, ship):
    """Manage the alien fleet creation and its timing. Moreover, update the score depending on the level"""
    if ai_settings.game_active:
        current_time = time.time()
        if (current_time - ai_settings.ini_time) >= ai_settings.spam_time and len(aliens) < ai_settings.alien_nmax:
            x = random.randint(1, 10)
            if x <= 2:
                new_alien = Alien(ai_settings, screen, ship, 3, 1 + ai_settings.alien_shoots_to_die, 'images/alien.png')
            elif x == 10:
                new_alien = Alien(ai_settings, screen, ship, 3, ai_settings.alien_shoots_to_die, 'images/alien1.png')
            else:
                new_alien = Alien(ai_settings, screen, ship, 1, ai_settings.alien_shoots_to_die, 'images/alien5.png')
            aliens.add(new_alien)
            ai_settings.ini_time = time.time()
            ai_settings.spam_time = random.uniform(ai_settings.alien_spam_time_min, ai_settings.alien_spam_time_max)
        for alien in aliens:
            alien.score = ai_settings.alien_score * ai_settings.level


def initialize_lives(ai_settings, screen, lives):
    """Iniatilize a list with the number of positions equal to the ship lives and set a Ship instance per position"""
    if not lives:
        for i in range(ai_settings.nships):
            lives.append(Ship(ai_settings, screen))
        for live, i in zip(lives, range(ai_settings.nships)):
            live.rect.left = i * live.rect.width
            live.rect.top = live.screen_rect.top


def update_sprites(ai_settings, ship, aliens, bullets):
    """Update aliens and bullets position and remove the not needed sprites"""
    aliens.update()
    bullets.update()
    ship.update()
    if not ai_settings.game_active:
        ship.center_ship()
    aliens_copy = aliens.copy()
    bullets_copy = bullets.copy()
    for alien in aliens_copy.sprites():
        for bullet in bullets_copy.sprites():
            if bullet.rect.bottom <= ship.rect.height:
                bullets.remove(bullet)
            if alien.is_hit(bullet):
                bullets.remove(bullet)
                ai_settings.aliens_hit += 1
                if alien.shoots_received == alien.shoots_to_die:
                    ai_settings.score += alien.score * alien.score_multiplier
                    make_more_challenge(ai_settings)
                    aliens.remove(alien)


def make_more_challenge(ai_settings):
    """Make settings more challenging based on the number of aliens hit"""
    ai_settings.aliens_dead += 1
    if ai_settings.aliens_dead >= ai_settings.level_hits:
        ai_settings.aliens_dead = 0
        ai_settings.level += 1
        ai_settings.alien_speed_factor += ai_settings.alien_delta_speed
        ai_settings.alien_speed_factor = min(ai_settings.alien_speed_factor, ai_settings.alien_max_speed)
        ai_settings.alien_lines_down += ai_settings.alien_delta_lines
        ai_settings.aliens_lines_down = min(ai_settings.alien_lines_down, ai_settings.alien_max_down)
        ai_settings.alien_spam_time_max -= ai_settings.alien_delta_time
        ai_settings.alien_spam_time_max = max(ai_settings.alien_spam_time_max, ai_settings.alien_spam_time_min)


def update_screen(ai_settings, screen, ship, bullets, aliens, lives, board, button):
    """Update the screen with the new changes in the objects"""
    screen.fill(ai_settings.bg_color)  # Redraw the screen each pass in the loop
    board.draw_board()
    if not ai_settings.game_active:
        button.draw_button(button.message)
    ship.draw_ship()
    for live in lives:
        live.draw_ship()
    for alien in aliens.sprites():
        alien.draw_alien()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()  # Make the most recently drawn screen visible


def check_end_game(ai_settings, aliens, ship, bullets, lives, button):
    """Check if an alien has hit the ship"""
    for alien in aliens.sprites():
        if ship.is_hit(alien):
            ship.moving_right = False
            ship.moving_left = False
            ai_settings.game_active = False
            time.sleep(2)
            lives.remove(lives[-1])
            if not lives:
                ai_settings.game_over = True
                button.message = 'PLAY AGAIN'
            elif len(lives) == 1:
                button.message = 'USE LAST SHIP'
            else:
                button.message = 'USE NEW SHIP'
    if not ai_settings.game_active:
        aliens.empty()
        bullets.empty()
