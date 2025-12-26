import sys
import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,PLAYER_RADIUS,LINE_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import display_score, setup_font
def main():
    print(f'Starting Asteroids with pygame version: {pygame.version.ver}')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,PLAYER_RADIUS)
    score_font = setup_font(74)
    pygame.display.set_caption("Score")
    current_score = 0
    

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for ast in asteroids:
            if player.collides_with(ast):
                log_event("player_hit")
                if player.lives > 0:
                    player.lives -= 1
                    print(f"{player.lives} lives remaining")
                else :
                    print("Game Over!")
                    sys.exit()
            for shot in shots:
                if shot.collides_with(ast):
                    log_event("asteroid_shot")
                    shot.kill()
                    ast.split()


        screen.fill("black")
        display_score(screen, score_font, current_score, 20, 20)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
