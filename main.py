import pygame
import random
import math


#initialize pygame
pygame.init()

#create screen (width, height)
screen = pygame.display.set_mode((800,600))

#Add Backdrop
backdrop = pygame.image.load('SPACE.png')

# Title/Icon
pygame.display.set_caption("Alien Armada")
icon = pygame.image.load('Alien dude.png')
pygame.display.set_icon(icon)
score = 0
#Enemy
enemyimage = pygame.image.load('img.png')
enemyX = random.randint(0,734)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40

#Missile
missileimage = pygame.image.load('missiles.png')
missileX = 0
missileY = 480
missileX_change = 0
missileY_change = 0.3
missile_state = "loaded"


#Player 1
playerimage = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerimage, (x, y) )

def enemy(x,y):
    screen.blit(enemyimage, (x, y) )

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
#Keep the window open
running = True
while running:

    #RGB - Red, Green, Blue, goes up to 255
    screen.fill((0, 0, 128))

    #Put backdrop image onto the window
    screen.blit(backdrop, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check left/right when keystroke is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

            # Missile Movement
            if event.key == pygame.K_SPACE and missile_state == "loaded":
                missileX = playerX
                missileY = playerY
                fire_missile(missileX,missileY)
                missile_state = "launched"


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #Update position
    playerX +=  playerX_change
    enemyX += enemyX_change

    #Player Bounds and movement
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #Enemy Bounds and movement
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    #Missile Movement
    if missile_state == "launched":
        fire_missile(missileX, missileY)
        missileY -= missileY_change
        # Reset missile when it moves off the screen
        if missileY <= 0:
            missileY = 480
            missile_state = "loaded"

    #Collision
    collision = isCollision(enemyX, enemyY, missileX, missileY)
    if collision:
        missileY = 480
        bullet_state = "loaded"
        score +=1
        print(score)
        enemyX = random.randint(0, 734)
        enemyY = random.randint(50, 150)


    #Draw
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    #Update the display
    pygame.display.update()