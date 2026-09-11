import pygame  # pyright: ignore[reportMissingImports]

from constants import (  # pyright: ignore[reportMissingImports]
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from logger import log_state  # pyright: ignore[reportMissingImports]
from player import Player  # pyright: ignore[reportMissingImports]


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

    Player.containers = (updatable, drawable)

    # spawn player in middle of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        screen.fill("black")

        updatable.update(dt)
        for d in drawable:
            d.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # tick
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
