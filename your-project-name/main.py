import sys

import pygame  # pyright: ignore[reportMissingImports]

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (  # pyright: ignore[reportMissingImports]
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from logger import log_event, log_state  # pyright: ignore[reportMissingImports]
from player import Player  # pyright: ignore[reportMissingImports]
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # spawn player in middle of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        log_state()
        screen.fill("black")

        updatable.update(dt)
        for d in drawable:
            d.draw(screen)

        # Events ----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for s in shots:
                if a.collides_with(s):
                    log_event("asteroid_shot")
                    a.split()
                    s.kill()

        # Tick ----
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
