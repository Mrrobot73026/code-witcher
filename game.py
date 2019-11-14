import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("SPACE FIGHTERS")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
# player
playerimg = pygame.image.load("space-invaders.png")
playerx = 370
playery = 480
playerx_change = 0

# enemy

enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("monster.png"))
    enemyx.append(random.randint(0, 799))
    enemyy.append(random.randint(50, 150))
    enemyx_change.append(4)
    enemyy_change.append(40)

    # bullet
bulletimg = pygame.image.load("bullet.png")
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 0.7
bullet_state = "ready"  # ready state means that you cant veiw the bullet!

score = 0


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


def isCollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt(math.pow(enemyx[i] - bulletx, 2) + math.pow(enemyy[i] - bullety, 2))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:
    screen.fill((0, 200, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            print("keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerx_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletx = playerx
                    bullet_fire(playerx, bullety)
        if event.type == pygame.KEYUP:
            print("keyup")

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0.1

    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736


    for i in range(num_of_enemies):
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 0.3
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -0.3
            enemyy[i] += enemyy_change[i]

        collision = isCollision(enemyx, enemyy, bulletx, bullety)
        if collision:
            bullety = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyx[i] = random.randint(0, 799)
            enemyy[i] = random.randint(50, 150)


        enemy(enemyx[i], enemyy[i], i)

    # bullet movement
    if bullety <= 0:
        bullety = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        bullet_fire(bulletx, bullety)
        bullety -= bullety_change

    player(playerx, playery)

    pygame.display.update()
