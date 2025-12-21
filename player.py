import pygame 
from circleshape import CircleShape
from constants import PLAYER_SPEED,PLAYER_TURN_SPEED,PLAYER_RADIUS, LINE_WIDTH, SHOT_RADIUS, PLAYER_SHOOT_SPEED,PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_INVINCIBILITY_TIMER
from shot import Shot
class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shot_cooldown = 0
        self.lives = 3
        self.invincibility_timer = PLAYER_INVINCIBILITY_TIMER
        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),LINE_WIDTH)
        
    def rotate(self,dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown -= dt
        if self.invincibility:
            self.invincibility_timer -= dt
            if self.invincibility_timer <= 0:
                self.invincibility = False
                self.invincibility_timer = PLAYER_INVINCIBILITY_TIMER
                print("can be damaged")


        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
    
    def move(self,dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    def shoot(self,dt):
        
        if self.shot_cooldown > 0:
            return
        else:
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
            bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED




        
        
    
        


        

