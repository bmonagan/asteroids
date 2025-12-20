import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    
    def split(self):
        self.kill() 
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            speed1 = random.randint(40,100)
            speed2 = random.randint(40,100)
            velocity = pygame.Vector2(1, 0)
            first_vel = pygame.math.Vector2.rotate(velocity*speed1,angle)
            second_vel = pygame.math.Vector2.rotate(velocity*speed2,-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_ast =  Asteroid(self.position.x, self.position.y, new_radius)
            second_ast = Asteroid(self.position.x, self.position.y, new_radius)
            first_ast.velocity = first_vel
            second_ast.velocity = second_vel
            

        
