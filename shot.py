from circleshape import CircleShape
import pygame

class Shot(CircleShape):

    def __init__(self, x, y, radius, rotation, velocity):
        super().__init__(x, y, radius)
        self.rotation = rotation
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius)

    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * (self.velocity * dt)


