from random import *
import time
import pygame
pygame.init()

# кадры в секунду
fps = 40

#текст для отображения 
TEXTCARD = 'CLICK'
TIME = 'Время:'
COUNTER = 'Счет'

#размер текста
size = 50

#цвета для использования
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BlUE = (0, 0, 255)
ORANGE = (255, 123, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 100)
LIGHT_BLUE = (200, 255, 255)

# исходные
wait = 0
points = 0

#создание окна и закрашивание
window = pygame.display.set_mode((500, 500)) #создание фонового окна
window.fill(LIGHT_BLUE)
clock = pygame.time.Clock()

