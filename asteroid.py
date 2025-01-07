import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = "white"
        width = 2

        pygame.draw.circle(screen, color, self.position, self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        random_angle = random.uniform(20, 50)
        
        new_deg1 = self.velocity.rotate(random_angle) * 1.2
        new_deg2 = self.velocity.rotate(-random_angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)

        ast1.velocity = new_deg1
        ast2.velocity = new_deg2
        
        self.kill()