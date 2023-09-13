import pygame
import sys
import random

username = input("Введите ваше имя: ")

pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(f'Управление персонажем: {username}')

character_x, character_y = 250, 250
character_width, character_height = 30, 30
character_speed = 0.06

object_width, object_height = 20, 20
object_x = random.randint(0, WINDOW_WIDTH - object_width)
object_y = random.randint(0, WINDOW_HEIGHT - object_height)

red_object_width, red_object_height = 20, 20
red_object_x = random.randint(0, WINDOW_WIDTH - red_object_width)
red_object_y = random.randint(0, WINDOW_HEIGHT - red_object_height)

score = 0
score_font = pygame.font.Font(None, 24)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    elif keys[pygame.K_RIGHT]:
        character_x += character_speed
    elif keys[pygame.K_UP]:
        character_y -= character_speed
    elif keys[pygame.K_DOWN]:
        character_y += character_speed

    window.fill((255, 255, 255))

    display_score = score_font.render(f'Очки: {score}', True, (0, 0, 0))
    window.blit(display_score, (10, 10))

    pygame.draw.rect(window, (0, 255, 0), (object_x, object_y, object_width, object_height))
    pygame.draw.rect(window, (0, 0, 255), (character_x, character_y, character_width, character_height))

    pygame.draw.rect(window, (255,0,0), (red_object_x, red_object_y, red_object_width, red_object_height))

    if (character_x < object_x + object_width and character_x + character_width > object_x and
            character_y < object_y + object_height and character_y + character_height > object_y):
        score += 1
        object_x = random.randint(0, WINDOW_WIDTH - object_width)
        object_y = random.randint(0, WINDOW_HEIGHT - object_height)

    if (character_x < red_object_x + red_object_width and character_x + character_width > red_object_x and
        character_y < red_object_y + red_object_height and character_y + character_height > red_object_y):
        print(f"{username}, вы проиграли! Ваш счет: {score}")
        pygame.quit()
        sys.exit()

    if score >= 10:
        print(f"Поздравляем, {username}! Вы выиграли! Ваш счет: {score}")
        pygame.quit()
        sys.exit()

    pygame.display.update()

