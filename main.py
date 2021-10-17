import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner - A Game by Ram Kumar")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# Background (no animation)
sky_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/ground.png")
text_surface = test_font.render("My game", False, "Black")

# Animated objects
snail_surface = pygame.image.load("graphics/snail/snail1.png")
snail_X_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Draw all or elements.
    # Update everything.

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    snail_X_pos -= 4
    screen.blit(snail_surface, (snail_X_pos, 250))

    pygame.display.update()
    clock.tick(60)
