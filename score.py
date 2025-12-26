import pygame
WHITE = (255, 255, 255)

def setup_font(size):
    return pygame.font.Font(None, size)

def display_score(screen, font_object, score_value, x, y):
    score_surface = font_object.render(f"Score: {score_value}", True, WHITE)
    score_rect = score_surface.get_rect(topleft=(x, y))
    screen.blit(score_surface, score_rect)