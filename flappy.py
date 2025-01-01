#Flappy Bird With Pygame

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Bird properties
BIRD_WIDTH = 40
BIRD_HEIGHT = 30
bird_x = 50
bird_y = WINDOW_HEIGHT // 2
bird_velocity = 0
GRAVITY = 0.5
JUMP_STRENGTH = -10

# Pipe properties
PIPE_WIDTH = 60
PIPE_GAP = 150
pipe_x = WINDOW_WIDTH
pipe_height = random.randint(100, 400)
PIPE_SPEED = 3

# Game variables
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = JUMP_STRENGTH

    # Update bird position
    bird_velocity += GRAVITY
    bird_y += bird_velocity

    # Update pipe position
    pipe_x -= PIPE_SPEED
    if pipe_x < -PIPE_WIDTH:
        pipe_x = WINDOW_WIDTH
        pipe_height = random.randint(100, 400)
        score += 1

    # Check for collisions
    bird_rect = pygame.Rect(bird_x, bird_y, BIRD_WIDTH, BIRD_HEIGHT)
    upper_pipe = pygame.Rect(pipe_x, 0, PIPE_WIDTH, pipe_height)
    lower_pipe = pygame.Rect(pipe_x, pipe_height + PIPE_GAP, PIPE_WIDTH, WINDOW_HEIGHT)

    if bird_rect.colliderect(upper_pipe) or bird_rect.colliderect(lower_pipe):
        running = False
    
    if bird_y < 0 or bird_y > WINDOW_HEIGHT:
        running = False

    # Draw everything
    window.fill(BLACK)
    
    # Draw bird
    pygame.draw.rect(window, WHITE, bird_rect)
    
    # Draw pipes
    pygame.draw.rect(window, GREEN, upper_pipe)
    pygame.draw.rect(window, GREEN, lower_pipe)
    
    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    window.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(60)

# Quit game
pygame.quit()
