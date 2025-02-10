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

#создание класса Area для отслеживания координат объектов
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height) #прямоугольник
        self.fill_color = color #цвет прямоугольника
    def set_color(self, new_color):
        self.fill_color = new_color #задать цвет
    def draw(self):
        pygame.draw.rect(window, self.fill_color, self.rect) #заполнить прямоугольник цветом
    def outline(self, frame_color, thickness=5):
        pygame.draw.rect(window, frame_color, self.rect, thickness) #сделать обводку другим цветом
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

#создание класса Label для заполнения карточки текстом
class Label(Area):
    def set_text(self, text, size=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', size).render(text, True, text_color)
    def write(self, shift_x=0, shift_y=0):
        self.draw()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

#   создание списка карточек
number_cards = 4
x_start = 50
cards = []


