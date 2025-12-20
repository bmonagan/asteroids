import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x , y, radius):
        super().__init__(x,y,radius)
        self.rotation = 0

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,SHOT_RADIUS,LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt

    def rotate(self,dt):
        self.rotation += (PLAYER_SHOOT_SPEED * dt)
