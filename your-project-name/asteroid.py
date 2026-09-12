from random import uniform
from typing import override

import pygame  # pyright: ignore[reportMissingImports]

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        # Need to split
        log_event("asteroid_split")

        angle = uniform(20, 50)
        a1_v = self.velocity.rotate(angle)
        a2_v = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        Asteroid(self.position[0], self.position[1], new_radius).velocity = a1_v * 1.2
        Asteroid(self.position[0], self.position[1], new_radius).velocity = a2_v * 1.2
