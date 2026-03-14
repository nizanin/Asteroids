from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import pygame
from logger import log_state
import game_state
from ui import enter_name, show_leaderboard, end_menu
from leaderboard import save_score




def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 50)

    while True:   # <-- pętla restartu gry
        game_start_time = pygame.time.get_ticks()
        game_state.SCORE = 0
        clock = pygame.time.Clock()
        dt = 0
        log_timer = 0

        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        bullets = pygame.sprite.Group()

        Player.containers = (updatable, drawable)
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable)
        Shot.containers = (updatable, drawable, bullets)
        


        player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

        asteroid_field = AsteroidField()

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.fill(color="black")
            
            for item in drawable:
                item.draw(screen)  
            updatable.update(dt)

            log_timer += dt
            if log_timer > 1:
                log_state()
                log_timer = 0

            for asteroid in asteroids:
                if asteroid.collision(player):
                    game_time = (pygame.time.get_ticks() - game_start_time)/1000
                    nickname = enter_name(screen, font)
                    save_score(nickname, game_state.SCORE, game_time)
                    show_leaderboard(screen, font)
                    choice = end_menu(screen, font)
                    if choice == "quit":
                        pygame.quit()
                        return
                    running = False
                    break
                for bullet in bullets:
                    if asteroid.collision(bullet):
                        asteroid.split()
                        bullet.kill()
                
            pygame.display.flip()
            dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()