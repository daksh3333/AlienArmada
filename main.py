import math
import random

import pygame

# initialize pygame
pygame.init()

# create screen (width, height)
screen = pygame.display.set_mode((800, 600))

# Add Backdrop
backdrop = pygame.image.load('SPACE.png')

# Title/Icon
pygame.display.set_caption("Alien Armada")
icon = pygame.image.load('Alien dude.png')
pygame.display.set_icon(icon)

# Enemy
enemyimage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 6

for i in range(number_of_enemies):
    enemyimage.append(pygame.image.load('img.png'))
    enemyX.append(random.randint(0, 734))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# Missile
missileimage = pygame.image.load('missiles.png')
missileX = 0
missileY = 480
missileX_change = 0
missileY_change = 0.3
missile_state = "loaded"

# Player 1
playerimage = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0


#score
score_val = 0
font = pygame.font.Font('freesansbold.ttf',32)

testX = 10
testY = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_val), True, (255,255,255))
    screen.blit(score, (x,y))


def player(x, y):
    screen.blit(playerimage, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimage[i], (x, y))


def fire_missile(x, y):
    global missile_state
    missile_state = "launched"
    screen.blit(missileimage, (x + 16, y + 10))


def isCollision(enemyX, enemyY, missileX, missileY):
    distance = math.sqrt((math.pow(enemyX - missileX, 2)) + (math.pow(enemyY - missileY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Keep the window open
running = True
while running:

    # RGB - Red, Green, Blue, goes up to 255
    screen.fill((0, 0, 128))

    # Put backdrop image onto the window
    screen.blit(backdrop, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check left/right when keystroke is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5

            # Missile Movement
            if event.key == pygame.K_SPACE and missile_state == "loaded":
                missileX = playerX
                missileY = playerY
                fire_missile(missileX, missileY)
                missile_state = "launched"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Update position
    playerX += playerX_change

    # Player Bounds and movement
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Bounds and movement
    for i in range(number_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], missileX, missileY)
        if collision:
            missileY = 480
            missile_state = "loaded"
            score_val += 1
            print(score_val)
            enemyX[i] = random.randint(0, 734)
            enemyY[i] = random.randint(50, 150)
            enemyX_change[i] += 0.01

        # draw enemy
        enemy(enemyX[i], enemyY[i], i)

    # Missile Movement
    if missile_state == "launched":
        fire_missile(missileX, missileY)
        missileY -= missileY_change
        # Reset missile when it moves off the screen
        if missileY <= 0:
            missileY = 480
            missile_state = "loaded"

    # Draw
    player(playerX, playerY)
    show_score(testX, testY)

    # Update the display
    pygame.display.update()

