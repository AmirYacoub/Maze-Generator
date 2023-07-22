import sys
from time import sleep

import pygame
import random

global POS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (77, 75, 82)
RED = (255, 0, 0)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
START = (0, 0)
POS = (0, 0)
END = (580, 580)
traversed = []
squares = []
path = []


def main():
    global SCREEN, CLOCK, SCREEN2
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREEN2 = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN2.fill(BLACK)
    SCREEN.fill(WHITE)
    drawGrid()
    pos = POS

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if len(traversed) == 900:
                    if event.key == pygame.K_LEFT:
                        x,y = pos
                        rect = pygame.Rect(x - 19, y + 1, 18, 18)
                        pygame.draw.rect(SCREEN2, RED, rect)
                if event.key == pygame.K_RIGHT:
                    x, y = pos
                    rect = pygame.Rect(x + 21 , y + 1, 18, 18)
                    pygame.draw.rect(SCREEN2, RED, rect)

        if len(traversed) != 900:
            x, y = pos
            rect = pygame.Rect(x + 1, y + 1, 18, 18)
            pygame.draw.rect(SCREEN, GREY, rect)
            pos = traverse(pos)
        if len(traversed) == 900:
            x, y = pos
            rect = pygame.Rect(x + 1, y + 1, 18, 18)
            pygame.draw.rect(SCREEN, GREY, rect)


        pygame.display.update()


def drawGrid():
    blockSize = 20  # Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            above = True
            below = True
            right = True
            left = True
            if x == 0:
                left = False
            elif x == 580:
                right = False
            if y == 0:
                above = False
            elif y == 580:
                below = False
            pygame.draw.rect(SCREEN, BLACK, rect, 1)


def traverse(pos):
    global r
    choices = [1, 2, 3, 4]
    print(choices)
    x, y = pos
    if (x, y) not in traversed:
        traversed.append((x, y))
    path.append((x, y))
    p = True
    while p:
        z = False
        r = random.choice(choices)
        if r == 1 and y == 0:
            if 1 in choices:
                choices.remove(1)
                z = True
        elif r == 1 and checkVisited(x, y - 20, traversed):
            if 1 in choices:
                choices.remove(1)
                z = True

        if r == 2 and y == 580:
            if 2 in choices:
                choices.remove(2)
            z = True
        elif r == 2 and checkVisited(x, y + 20, traversed):
            if 2 in choices:
                choices.remove(2)
                z = True

        if r == 3 and x == 580:
            if 3 in choices:
                choices.remove(3)
                z = True
        elif r == 3 and checkVisited(x + 20, y, traversed):
            if 3 in choices:
                choices.remove(3)
                z = True

        if r == 4 and x == 0:
            if 4 in choices:
                choices.remove(4)
                z = True

        elif r == 4 and checkVisited(x - 20, y, traversed):
            if 4 in choices:
                choices.remove(4)
                z = True

        if len(choices) == 0:
            print("Done")
            print(len(traversed))
            x1, y1 = returnPath(x, y, path)
            return x1, y1

        if not z:
            print("found")
            p = False

    if r == 1:
        print(r)
        rect = pygame.Rect(x + 1, y - 19, 18, 18)
        pygame.draw.line(SCREEN, GREY, (x + 1, y), (x + 18, y), width=3)
        pygame.draw.rect(SCREEN2, RED, rect)
        traversed.append((x, y - 20))
        return x, y - 20
    elif r == 2:
        print(r)
        rect = pygame.Rect(x + 1, y + 21, 18, 18)
        pygame.draw.line(SCREEN, GREY, (x + 1, y + 20), (x + 18, y + 20), width=3)
        pygame.draw.rect(SCREEN2, RED, rect)
        traversed.append((x, y + 20))
        return x, y + 20
    elif r == 3:
        print(r)
        rect = pygame.Rect(x + 21, y + 1, 18, 18)
        pygame.draw.line(SCREEN, GREY, (x + 20, y + 1), (x + 20, y + 18), width=3)
        pygame.draw.rect(SCREEN2, RED, rect)
        traversed.append((x + 20, y))
        return x + 20, y
    elif r == 4:
        print(r)
        rect = pygame.Rect(x - 19, y + 1, 18, 18)
        pygame.draw.line(SCREEN, GREY, (x, y + 1), (x, y + 18), width=3)
        pygame.draw.rect(SCREEN2, RED, rect)
        traversed.append((x - 20, y))
        return x - 20, y


# 1 up 2 down 3 right 4 left

def checkVisited(x, y, cells):
    if (x, y) in cells:
        return True
    return False


def returnPath(x, y, path):
    pos = path[path.index((x, y)) - 1]
    return pos


main()
