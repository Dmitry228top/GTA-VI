# Импорт необходимых модулей
import math as m
import sys
import os
from datetime import date, time
import datetime
from random import choice
import pygame.display
import pygame.event
import pygame
import random
import time

# Импорт пользовательских классов
from classes.player import Player

# Глобальные переменные для настройки игры
speed = 1
WIDTH = 1000  # Ширина экрана
HEIGHT = 1000  # Высота экрана
FPS = 150  # Частота кадров в секунду

# Цвета, используемые в игре
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Инициализация Pygame и миксера для звука
pygame.init()
pygame.mixer.init()

# Создание окна игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GTA VI")  # Название окна

# Создание объекта для управления временем (FPS)
clock = pygame.time.Clock()

# Загрузка изображения персонажа Sans и его масштабирование
sans_surface = pygame.image.load("images/sans.jpg")
sans_surface.set_colorkey((255, 255, 255))  # Установка цвета прозрачности
sans_surface = pygame.transform.scale(sans_surface, (120, 100))
sans_rect = sans_surface.get_rect(center=(500, 500))

# Создание экземпляров класса Player для главного героя и второго персонажа
player = Player(image="images/sans.jpg", width=50, height=50)
bro = Player(image="images/bro.jpg", width=100, height=100)

# Создание группы спрайтов для второго персонажа
group_1 = pygame.sprite.Group(bro)

# Переменные для координат объектов на экране
x = 0
y = 0

# Координаты круга на экране
xCircle = 500
yCircle = 240

# Основной игровой цикл
running = True
while running:
    # Проверка столкновения между игроком и группой спрайтов
    if pygame.sprite.spritecollide(player, group_1, False):
        print("Домика нить")  # Вывод сообщения при столкновении
        bro.x = random.randint(100, WIDTH)  # Случайное перемещение второго персонажа
        bro.y = random.randint(100, HEIGHT)
        player.speed += 1  # Увеличение скорости игрока

    # Отслеживание нажатых клавиш
    keys = pygame.key.get_pressed()  # Получаем список нажатых клавиш
    if keys[pygame.K_d]:
        player.x = player.x + player.speed  # Движение вправо
    elif keys[pygame.K_a]:
        player.x = player.x - player.speed  # Движение влево
    if keys[pygame.K_s]:
        player.y = player.y + player.speed  # Движение вниз
    elif keys[pygame.K_w]:
        player.y = player.y - player.speed  # Движение вверх

    # Обработка движения объекта по границам экрана
    if x >= WIDTH + 50:
        x = -50
    elif x <= -50:
        x = WIDTH
    if y >= HEIGHT - 200:
        y = -50
    elif y <= -200:
        y = HEIGHT

    # Отрисовка фона
    screen.fill(WHITE)

    # Отрисовка второго персонажа и игрока
    bro.drow(screen=screen)
    player.drow(screen=screen)

    # Обработка событий Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Завершение игры при закрытии окна

    # Проверка столкновения объекта с кругом
    if x < xCircle < x + 50 and y < yCircle < y + 200:
        xCircle = random.randint(0, WIDTH)  # Случайное перемещение круга
        yCircle = random.randint(0, HEIGHT)

    # Ограничение FPS
    clock.tick(FPS)

    # Обновление экрана
    pygame.display.update()

# Завершение работы Pygame
pygame.quit()