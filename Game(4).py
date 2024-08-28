import sys

import pygame

pygame.font.init()

import math

width = 1200
height = 720
screen = pygame.display.set_mode((width, height))
dfs = 50
score1 = 0
score2 = 0
service1 = False
service2 = False
p1point = False
p2point = False


class shuttle:
    def __init__(self, x, y, speed, colour, radius, width, angle):
        self.x = x
        self.y = y
        self.speed = speed
        self.colour = colour
        self.radius = radius
        self.width = width
        self.angle = angle

    def draw(self):
        pygame.draw.circle(screen, self.colour, [self.x, self.y], self.radius, self.width)


class player:
    def __init__(self, x, y, width, height, speed, colour, playershot, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.colour = colour
        self.playershot = None
        self.direction = direction
        self.hitbox = (self.x, self.y, 30, 30)

    def draw(self):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x, self.y, 30, 30)
        pygame.draw.rect(screen, (255, 255, 255), self.hitbox, 2)


def drawCourt():
    # drawing court borders
    pygame.draw.line(screen, (255, 255, 255), (dfs, dfs), (width - dfs, dfs))
    pygame.draw.line(screen, (255, 255, 255), (dfs, height - dfs), (width - dfs, height - dfs))
    pygame.draw.line(screen, (255, 255, 255), (dfs, dfs), (dfs, height - dfs))
    pygame.draw.line(screen, (255, 255, 255), (width - dfs, dfs), (width - dfs, height - dfs))

    # drawing internal court lines
    pygame.draw.line(screen, (255, 255, 255), (dfs, 2 * dfs), (width - dfs, 2 * dfs))
    pygame.draw.line(screen, (255, 255, 255), (dfs, height - 2 * dfs), (width - dfs, height - 2 * dfs))
    pygame.draw.line(screen, (255, 255, 255), (2.5 * dfs, dfs), (2.5 * dfs, height - dfs))
    pygame.draw.line(screen, (255, 255, 255), (width - 2.5 * dfs, dfs), (width - 2.5 * dfs, height - dfs))
    pygame.draw.line(screen, (255, 0, 0), (width / 2, dfs), (width / 2, height - dfs))
    pygame.draw.line(screen, (255, 255, 255), (dfs, height / 2), (width / 2 - 2.5 * dfs, height / 2))
    pygame.draw.line(screen, (255, 255, 255), (width / 2 + 2.5 * dfs, height / 2), (width - dfs, height / 2))
    pygame.draw.line(screen, (255, 255, 255), (width / 2 - 2.5 * dfs, dfs), (width / 2 - 2.5 * dfs, height - dfs))
    pygame.draw.line(screen, (255, 255, 255), (width / 2 + 2.5 * dfs, dfs), (width / 2 + 2.5 * dfs, height - dfs))

    pygame.display.flip()


screen.fill((0, 135, 51))

player1 = player((dfs + width / 2) / 2, height / 2, 30, 30, 5, (0, 0, 255), None, "e")
player2 = player((width / 2 + width - dfs) / 2, height / 2, 30, 30, 5, (255, 0, 0), None, "w")
shuttle1 = shuttle((dfs + width / 2) / 2 + 45, height / 2 + 19, 0, (255, 255, 255), 10, 10, 0)

font = pygame.font.SysFont('comicsans', 20, True, False)

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 135, 51))

    text1 = font.render('Blue Score: ' + str(score1), 1, (0, 0, 0))
    screen.blit(text1, (width / 2 - 250, dfs / 5))

    text2 = font.render('Red Score: ' + str(score2), 1, (0, 0, 0))
    screen.blit(text2, (width / 2 + 125, dfs / 5))

    player1.draw()

    player2.draw()

    shuttle1.draw()

    # player direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player1.x > 0:
        player1.x -= 1
    if keys[pygame.K_d] and player1.x < width / 2 - 30:
        player1.x += 1
    if keys[pygame.K_w] and player1.y > 0:
        player1.y -= 1
    if keys[pygame.K_s] and player1.y < height - 30:
        player1.y += 1

    if keys[pygame.K_LEFT] and player2.x > width / 2:
        player2.x -= 1
    if keys[pygame.K_RIGHT] and player2.x < width - 30:
        player2.x += 1
    if keys[pygame.K_UP] and player2.y > 0:
        player2.y -= 1
    if keys[pygame.K_DOWN] and player2.y < height - 30:
        player2.y += 1
    # if keys[pygame.K_d] and player1.x < shuttle1.x:
    # shuttle1.speed = 0.50

    if shuttle1.x < width / 2 and keys[pygame.K_1] and shuttle1.speed == 0:
        shuttle1.speed = 0.5
        shuttle1.angle = - math.pi / 18
        player1.playershot = False
        player2.playershot = True
        service1 = True
        service2 = False
        p1point = False
        p2point = False

    if shuttle1.x > width / 2 and keys[pygame.K_2] and shuttle1.speed == 0:
        shuttle1.speed = 0.5
        shuttle1.angle = math.pi + math.pi / 18
        player1.playershot = True
        player2.playershot = False
        service2 = True
        service1 = False
        p1point = False
        p2point = False

    # if not(player1.playershot and shuttle1.x<width-dfs):
    #     shuttle1.speed = 0

    # shuttle direction if statements
    if keys[pygame.K_w] and keys[pygame.K_d]:
        player1.direction = "ne"
        print(player1.direction)
    elif keys[pygame.K_s] and keys[pygame.K_d]:
        player1.direction = "se"
        print(player1.direction)
    elif keys[pygame.K_s] and keys[pygame.K_a]:
        player1.direction = "sw"
        print(player1.direction)
    elif keys[pygame.K_w] and keys[pygame.K_a]:
        player1.direction = "nw"
        print(player1.direction)
    elif keys[pygame.K_d]:
        player1.direction = "e"
        print(player1.direction)
    elif keys[pygame.K_s]:
        player1.direction = "s"
        print(player1.direction)
    elif keys[pygame.K_a]:
        player1.direction = "w"
        print(player1.direction)
    elif keys[pygame.K_w]:
        player1.direction = "n"
        print(player1.direction)

    if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        player2.direction = "ne"
        print(player2.direction)
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        player2.direction = "se"
        print(player2.direction)
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        player2.direction = "sw"
        print(player2.direction)
    elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        player2.direction = "nw"
        print(player2.direction)
    elif keys[pygame.K_RIGHT]:
        player2.direction = "e"
        print(player2.direction)
    elif keys[pygame.K_DOWN]:
        player2.direction = "s"
        print(player2.direction)
    elif keys[pygame.K_LEFT]:
        player2.direction = "w"
        print(player2.direction)
    elif keys[pygame.K_UP]:
        player2.direction = "n"
        print(player2.direction)

    if (shuttle1.x > player1.x and shuttle1.x < player1.x + 30) and (
            shuttle1.y > player1.y and shuttle1.y < player1.y + 30) and player1.playershot and (not player2.playershot):
        print("Touching 1")
        if player1.direction == 'ne':
            shuttle1.angle = math.pi / 4
        elif player1.direction == 'se':
            shuttle1.angle = -math.pi / 4
        elif player1.direction == 'sw':
            shuttle1.angle = 5 * math.pi / 4
        elif player1.direction == 'nw':
            shuttle1.angle = 3 * math.pi / 4
        elif player1.direction == 'n':
            shuttle1.angle = math.pi / 2
        elif player1.direction == 'e':
            shuttle1.angle = 0
        elif player1.direction == 's':
            shuttle1.angle = 3 * math.pi / 2
        elif player1.direction == 'w':
            shuttle1.angle = math.pi
        player1.playershot = False
        player2.playershot = True

        # shuttle1.x += math.cos(shuttle1.angle)
        # shuttle1.y += math.sin(shuttle1.angle)

    elif (shuttle1.x > player2.x and shuttle1.x < player2.x + 30) and (
            shuttle1.y > player2.y and shuttle1.y < player2.y + 30) and player2.playershot and (not player1.playershot):
        print("Touching 2")
        if player2.direction == 'ne':
            shuttle1.angle = math.pi / 4
        elif player2.direction == 'se':
            shuttle1.angle = -math.pi / 4
        elif player2.direction == 'sw':
            shuttle1.angle = 5 * math.pi / 4
        elif player2.direction == 'nw':
            shuttle1.angle = 3 * math.pi / 4
        elif player2.direction == 'n':
            shuttle1.angle = math.pi / 2
        elif player2.direction == 'e':
            shuttle1.angle = 0
        elif player2.direction == 's':
            shuttle1.angle = 3 * math.pi / 2
        elif player2.direction == 'w':
            shuttle1.angle = math.pi
        player2.playershot = False
        player1.playershot = True
        # shuttle1.x += math.cos(shuttle1.angle)
        # shuttle1.y += math.sin(shuttle1.angle)

    if (shuttle1.x > player2.x and shuttle1.x < player2.x + 0.0001) and (
            shuttle1.y > player2.y and shuttle1.y < player2.y + 30):
        shuttle1.speed = -0.50
        shuttle1.x += shuttle1.speed * math.cos(shuttle1.angle)
        print('satisfied2')
    elif (shuttle1.x > player1.x and shuttle1.x < player1.x + 30) and (
            shuttle1.y > player1.y and shuttle1.y < player1.y + 30):
        shuttle1.speed = 0.50
        shuttle1.x += shuttle1.speed * math.cos(shuttle1.angle)
        print('satisfied1', shuttle1.speed)
    # else:

    if shuttle1.y < dfs:
        shuttle1.speed = 0
    if shuttle1.y > height - dfs:
        shuttle1.speed = 0
    if shuttle1.x < dfs:
        shuttle1.speed = 0
    if shuttle1.x > width - dfs:
        shuttle1.speed = 0

    if (service1 or service2) and shuttle1.x < width / 2 and shuttle1.speed == 0 and (
            shuttle1.x < dfs or shuttle1.y < dfs or shuttle1.y > height - dfs):
        score2 += 1
        p2point = True
        p1point = False
        print("Blue %d - %d Red" % (score1, score2))
        service1 = False
        service2 = False
    elif (service1 or service2) and shuttle1.x > width / 2 and shuttle1.speed == 0 and (
            shuttle1.x > width - dfs or shuttle1.y < dfs or shuttle1.y > height - dfs):
        score1 += 1
        p1point = True
        p2point = False
        print("Blue %d - %d Red" % (score1, score2))
        service1 = False
        service2 = False

    if p1point:
        # pygame.time.delay(1000)
        shuttle1.x = (dfs + width / 2) / 2 + 45
        shuttle1.y = height / 2 + 19
    if p2point:
        # pygame.time.delay(1000)
        shuttle1.x = (width / 2 + width - dfs) / 2 - 45
        shuttle1.y = height / 2 + 19

    shuttle1.y -= shuttle1.speed * math.sin(shuttle1.angle)
    shuttle1.x += shuttle1.speed * math.cos(shuttle1.angle)

    if score1 == 30 or score2 == 30:
        sys.exit()
    elif (score1 >=21 or score2 >=21) and math.fabs(score1-score2) >= 2:
        sys.exit()

    # print(shuttle1.speed)
    # else:
    #     print('satisfied')
    # shuttle1.speed = 0.5

    # if (shuttle1.x > player2.x and shuttle1.x < player2.x + 30) and (shuttle1.y > player2.y and shuttle1.y < player2.y + 30):
    #     shuttle1.speed = -0.50
    # elif (shuttle1.x > player1.x and shuttle1.x < player1.x + 30) and (shuttle1.y > player1.y and shuttle1.y < player1.y + 30):
    #     shuttle1.speed = 0.50

    # shuttle1.y -= shuttle1.speed*math.sin(shuttle1.angle)
    drawCourt()
    pygame.display.update()

    # timer after net for fall down

    # Rules of the game:
    # For service - if receiver does not contact the shuttle, shuttle should stop at the end of the court, server wins point
    #
