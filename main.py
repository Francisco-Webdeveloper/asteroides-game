import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_tracker = pygame.time.Clock()
    dt = 0

    # create groups:
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = time_tracker.tick(60) / 1000
        updatable.update(dt)

        for sprite in asteroids:

            for shot in shots:
                collision_shot_asteroid = sprite.collide(shot)
                if collision_shot_asteroid:
                    shot.kill()
                    sprite.split()

            collision_player_asteroid = sprite.collide(player)
            if collision_player_asteroid:
                print("Game over!")
                sys.exit()

if __name__ == "__main__":
    main()