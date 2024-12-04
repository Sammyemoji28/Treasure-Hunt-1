
import pygame
import random
import time
import sys

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Treasure Hunt")

WIDTH = 600
HEIGHT = 600

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (135,206,235)
GREEN = (103,146,103)
RED = (187,17,68)

FPS = 30
clock = pygame.time.Clock()

gridSize = 20
cellSize = WIDTH//gridSize
obstacleNum = 25
score = 0

treasurePos = []
obstaclePos = []
playerPos = [gridSize//2, gridSize//2]

font = pygame.font.SysFont("calibri", 30)
text = font.render(f"Score : {str(score)}", False, BLUE)

def drawGrid():
    for x in range(0, WIDTH, cellSize): # - 3 parameters : starting #, ending #, size
        pygame.draw.line(screen, WHITE, (x,0), (x,HEIGHT))
    for y in range(0, HEIGHT,cellSize):
        pygame.draw.line(screen, WHITE, (0,y), (WIDTH, y))

def makePlayer():
    pygame.draw.rect(screen, BLUE, (playerPos[0] * cellSize, playerPos[1] * cellSize, cellSize, cellSize))

def makeTreasure():
    for pos in treasurePos:
        pygame.draw.rect(screen, GREEN, (pos[0] * cellSize, pos[1] * cellSize, cellSize, cellSize))

def makeObstacles():
    for pos in obstaclePos:
        pygame.draw.rect(screen, RED, (pos[0] * cellSize, pos[1] * cellSize, cellSize, cellSize))

while True:
    screen.fill(BLACK)
    drawGrid()
    makePlayer()
    makeTreasure()
    makeObstacles()
    screen.blit(text, (30,30))
    clock.tick(FPS)
    pygame.display.flip()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and playerPos[0] > 0:
        playerPos[0] -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
