from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius)

    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(0)
        self.position += forward + (self.velocity * dt)
    
    def split(self):
        self.kill()
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        if new_radius < ASTEROID_MIN_RADIUS:
            return

        new_angle = random.uniform(20,50)
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        forward1 = self.velocity.rotate(new_angle)
        forward2 = self.velocity.rotate(-new_angle)
        asteroid1.velocity = forward1 * 1.2
        asteroid2.velocity = forward2 * 1.2
        return (asteroid1, asteroid2)


    def kill(self):
        pygame.sprite.Sprite.kill(self)


