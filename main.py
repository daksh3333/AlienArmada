import pygame

#initialize pygame
pygame.init()

#create screen (width, height)
screen = pygame.display.set_mode((800,600))

# Title/Icon
pygame.display.set_caption("Alien Armada")
icon = pygame.image.load('Alien dude.png')
pygame.display.set_icon(icon)

#Player 1
playerimage = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerimage, (playerX, playerY) )

# Keep the window open
running = True
while running:
    #RGB - Red, Green, Blue, goes up to 255
    screen.fill((0, 0, 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player()
    pygame.display.update()