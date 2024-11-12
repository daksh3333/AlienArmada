import math
import random
import pygame
from pygame import mixer

# Initialize pygame
pygame.init()

# Create screen (width, height)
screen = pygame.display.set_mode((800, 600))

# Add Backdrop
backdrop = pygame.image.load('SPACE.png')

# Background sound
mixer.music.load('music.wav')
mixer.music.play(-1)

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
missiles = []
missileY_change = 0.3

# Player 1
playerimage = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Score
score_val = 0
font = pygame.font.Font('freesansbold.ttf', 32)
over_text = pygame.font.Font('freesansbold.ttf', 72)

testX = 10
testY = 10

def game_over_text():
    over_text_display = over_text.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text_display, (200, 250))

def show_score(x, y):
    score = font.render("Score: " + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerimage, (x, y))

def enemy(x, y, i):
    screen.blit(enemyimage[i], (x, y))

def fire_missile(x, y):
    missiles.append([x + 16, y + 10])

def isCollision(enemyX, enemyY, missileX, missileY):
    distance = math.sqrt((math.pow(enemyX - missileX, 2)) + (math.pow(enemyY - missileY, 2)))
    return distance < 27

# Main Game Loop
running = True
while running:
    screen.fill((0, 0, 128))  # RGB background
    screen.blit(backdrop, (0, 0))  # Backdrop image

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check left/right movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            # Fire missile on space key
            if event.key == pygame.K_SPACE:
                launch_sound = mixer.Sound('laser.wav')
                launch_sound.play()
                fire_missile(playerX, playerY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Update player position
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement and collision
    for i in range(number_of_enemies):
        if enemyY[i] > 450:  # Game over condition
            for j in range(number_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # Check collisions with each missile
        for missile in missiles[:]:
            if isCollision(enemyX[i], enemyY[i], missile[0], missile[1]):
                boom_sound = mixer.Sound('explosion.wav')
                boom_sound.play()
                missiles.remove(missile)  # Remove missile on collision
                score_val += 1
                enemyX[i] = random.randint(0, 734)
                enemyY[i] = random.randint(50, 150)
                enemyX_change[i] += 0.02  # Increase difficulty

        # Draw enemy
        enemy(enemyX[i], enemyY[i], i)

    # Missile movement and display
    for missile in missiles[:]:
        missile[1] -= missileY_change
        if missile[1] <= 0:
            missiles.remove(missile)  # Remove missile if off-screen
        else:
            screen.blit(missileimage, (missile[0], missile[1]))

    # Draw player and show score
    player(playerX, playerY)
    show_score(testX, testY)

    pygame.display.update()  # Refresh display
