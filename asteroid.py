from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self, radius):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_asteroid1_angle = pygame.math.Vector2.rotate(self.velocity, random_angle)
            new_asteroid2_angle = pygame.math.Vector2.rotate(self.velocity, -random_angle)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            new_asteroid2 = Asteroid(self.position, self.position.y, new_asteroid_radius)
            new_asteroid1.velocity = new_asteroid1_angle * 1.2
            new_asteroid2.velocity = new_asteroid2_angle * 1.2





