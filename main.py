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

#внесение объектов таймер и время
start_time = time.time()
current_time = start_time

time_text = Label(20, 0, 100, 20, LIGHT_BLUE)
time_text.set_text(TIME, size, BlUE)
time_text.write(5, 25)

timer = Label(40, 70, 100, 20, LIGHT_BLUE)
timer.set_text('0', 40, BlUE)
timer.write(0,0)

score_text = Label(380, 0, 50, 50, LIGHT_BLUE)
score_text.set_text('Счёт:', 45, BlUE)
score_text.write(20, 20)

score = Label(430, 55, 50, 40, LIGHT_BLUE)
score.set_text('0', 40, BlUE)
score.write(0, 0)

#   создание списка карточек
for i in range(number_cards):
    new_card = Label(x_start, 170, 70, 100, YELLOW)
    new_card.outline(DARK_BLUE, 10)
    new_card.set_text(TEXTCARD, 26)
    cards.append(new_card)
    x_start += 100
#игровой цикл
while True:
#изменение надписи клик по карточкам
    if wait == 0:
        wait = 20
        random_card = randint(1,number_cards)
        for i in range (number_cards):
            cards[i].set_color(YELLOW)
            if (i + 1) == random_card:
                cards[i].write(10, 40)
            else:
                cards[i].draw()
    else:
        wait -= 1

#обработка карты в которую попала мышь и добавка/убавка баллов
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(number_cards):
                if cards[i].collidepoint(x, y):
                    if (i + 1) == random_card:
                        cards[i].set_color(GREEN)
                        points += 1
                    else:
                        cards[i].set_color(RED)
                        points -= 1
                    cards[i].draw()
                    score.set_text(str(points), 40, BlUE)
                    score.write(0,0)
#победа или проигрыш
    new_time = time.time()

    if new_time - start_time >= 11:
        mw = Label(0, 0, 500, 500, LIGHT_RED)
        mw.set_text("Время вышло!", 60, BLACK)
        mw.write(110, 180)
        break


pygame.display.update()