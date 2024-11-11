import pygame

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))

# Keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False