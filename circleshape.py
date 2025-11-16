import pygame
from constants import LINE_WIDTH

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self,"containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius


    def draw(self, screen):
        pass



    
    def update(self, dt):
        pass


    def collides_with_self(self, other):
        
        dist_to = pygame.math.Vector2.distance_to(self.position, other.position)
        if dist_to < (self.radius + other.radius):
            return True
        return False