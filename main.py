import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner - A Game by Ram Kumar")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# Background (no animation)
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
text_surface = test_font.render("My game", False, "Black")

# Animated objects
snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
       # if event.type == pygame.MOUSEMOTION:
        #    if player_rect.collidepoint(event.pos):
         #       print("collision")

    # Draw all or elements.
    # Update everything.

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    #if player_rect.colliderect(snail_rect):
       # print("collision")
    # Note: snail_rect.colliderect(player_rect) would also work

   # mouse_pos = pygame.mouse.get_pos()
   # if player_rect.collidepoint(mouse_pos):
   #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)
