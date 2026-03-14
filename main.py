from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import pygame
from logger import log_state
import game_state


def game_over_screen(screen, font, score):
    while True:
        screen.fill((0, 0, 0))

        text1 = font.render("GAME OVER", True, (255, 0, 0))
        text2 = font.render(f"Score: {score}", True, (255, 255, 255))
        text3 = font.render("ENTER - restart", True, (255, 255, 255))
        text4 = font.render("ESC - quit", True, (255, 255, 255))

        screen.blit(text1, (350, 250))
        screen.blit(text2, (350, 300))
        screen.blit(text3, (350, 350))
        screen.blit(text4, (350, 400))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

                if event.key == pygame.K_RETURN:
                    return   # restart gry




def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 50)

    while True:   # <-- pętla restartu gry

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
                    game_over_screen(screen, font, game_state.SCORE)
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