import pygame  # pyright: ignore[reportMissingImports]

from constants import (  # pyright: ignore[reportMissingImports]
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
