import pygame
import math
import random
import time
pygame.init()

WIDTH, HEIGHT = 900, 500
FONT = pygame.font.SysFont('comicsans', 30)
LARGE_FONT = pygame.font.SysFont('comicsans', 40)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sorting ALGORITHM Visualizer')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ALGORITHM = 0
ALGORITHM_NAME = 'Selection Sort'
FPS = 60


def drawChart(lst):
    WINDOW.fill(WHITE)
    x = 5
    for i in lst:
        y = 100
        h = 400
        y += i
        h -= i
        pygame.draw.rect(WINDOW, BLACK, (x, y, 10, h))
        x += 14.93
    drawUI(ALGORITHM_NAME)
    pygame.display.update()

def drawUI(ALGORITHM):
    font = pygame.font.SysFont('Calibri.ttf', 70)
    label = font.render(ALGORITHM, 1, BLACK)
    text_rect = label.get_rect(center = (WIDTH  / 2, 50))
    WINDOW.blit(label, text_rect)



def generateNumbers():
    lst = []
    for i in range(60):
        lst.append(random.randint(0, 39) * 10)
    return lst

def selectionSort(chart):
    len_chart = len(chart)
    for i in range(len_chart):
        min_idx = i
        for j in range(i + 1, len_chart):
            if chart[min_idx] > chart[j]:
                drawChart(chart)
                time.sleep(0.1)
                min_idx = j
        chart[i], chart[min_idx] = chart[min_idx], chart[i]


def bubbleSort(chart):
    len_chart = len(chart)
    for j in range(len_chart-1):
        flag = False
        for i in range(len_chart - 1):
            if chart[i] > chart[i + 1]:
                chart[i], chart[i + 1] = chart[i + 1], chart[i]
                flag = True
                pos = i + 1
        drawChart(chart)
        time.sleep(0.1)
        if not(flag):
            break
        else: 
            len_chart = pos


def main():
    run = True
    clock = pygame.time.Clock()
    lst = generateNumbers()
    global ALGORITHM_NAME, ALGORITHM
    while run:
        clock.tick(FPS)
        run = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    lst = generateNumbers()

                if event.key == pygame.K_m:
                    match ALGORITHM:
                        case 0:
                            ALGORITHM += 1
                        case 1:
                            ALGORITHM += 1

                if event.key == pygame.K_SPACE:
                    match ALGORITHM:
                        case 0:
                            sorting = True
                            selectionSort(lst)
                        case 1:
                            sorting = True
                            bubbleSort(lst)

            else:
                match ALGORITHM:
                    case 0:
                        ALGORITHM_NAME = 'Selection Sort'
                    case 1:
                        ALGORITHM_NAME = 'Bubble Sort'
                    case _:
                        ALGORITHM = 0
        drawChart(lst)
        
    pygame.quit()

if __name__ == '__main__':
    main()