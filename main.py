import pygame

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))

# Title/Icon
pygame.display.set_caption("Alien Armada")
icon = pygame.image.load('Alien dude.png')
pygame.display.set_icon(icon)


# Keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #RGB - Red, Green, Blue, goes up to 255
    screen.fill((0, 0, 128))
    pygame.display.update()