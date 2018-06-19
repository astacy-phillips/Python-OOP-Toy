import math

from pygame.math import Vector2


class Ball:
    """
    base class for bouncing objects
    """

    def __init__(self, bounds, position, velocity, color, radius):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.radius = radius

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        # screen width
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius:
            self.velocity.x *= -1
        # screen height
        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius:
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(
            self.position.x), int(self.position.y)], self.radius)


class BouncingBall(Ball):
    """
    ball effected by gravity
    """
    # TODO: Fix rounding error that makes it bounce higher
    gravity = .1

    def update(self):
        # This function will override the the function in Ball
        self.velocity.y += self.gravity
        # Now that you've done your class specific stuff, call your parent's update func
        super().update()


class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    # TODO:

    def update(self):
        # TODO: cycle back and forth so color doesn't pop
        r = (self.color[0] + 1) % 256
        g = (self.color[1] - 1) % 256
        b = (self.color[2] + 1) % 256
        self.color = [r, g, b]

        super().update()


class BouncingRainbow(BouncingBall, RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """
    # TODO:
    pass


class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    # TODO:
    pass


class KineticBouncing(KineticBall, BouncingBall):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    And is affected by gravity
    """
    pass


class AllTheThings(BouncingBall, RainbowBall, KineticBall):
    """
    A ball that does everything!
    """
    pass
