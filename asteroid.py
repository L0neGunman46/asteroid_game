import pygame
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import random as rand

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,self.radius,LINE_WIDTH)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand_angle = rand.randint(0, 60)
        v1 = self.velocity.rotate(rand_angle)
        v2 = self.velocity.rotate(-rand_angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS

        new_ast1 = Asteroid(self.position.x, self.position.y, new_rad)
        new_ast2 = Asteroid(self.position.x, self.position.y, new_rad)
        new_ast1.velocity = v1 *1.2
        new_ast2.velocity = v2 * 1.2
