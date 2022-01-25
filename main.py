import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
snake_color = (0, 0, 0)
text_color = snake_color
extra_speed_color = (255, 0, 255)
extra_slow_color = (0, 0, 255)
food_color = (255, 51, 0)
background_color = (157, 204, 0)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def player_score(score):
    value = score_font.render("Twoje punkty: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, snake_color, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    text = font_style.render(msg, True, color)
    dis.blit(text, [dis_width / 6, dis_height / 3])


def gameLoop(snake_speed):
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_lenght = 1

    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    extra_speed_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    extra_speed_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    extra_slow_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    extra_slow_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(background_color)
            message("Przegrałeś! C-graj ponownie Q-zamknij", text_color)
            player_score(snake_lenght - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        snake_speed = 15
                        gameLoop(snake_speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(background_color)
        pygame.draw.rect(dis, food_color, [food_x, food_y, snake_block, snake_block])
        pygame.draw.rect(dis, extra_speed_color, [extra_speed_x, extra_speed_y, snake_block, snake_block])
        pygame.draw.rect(dis, extra_slow_color, [extra_slow_x, extra_slow_y, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > snake_lenght:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_list)
        player_score(snake_lenght - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            snake_lenght += 1
        if x1 == extra_speed_x and y1 == extra_speed_y:
            extra_speed_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            extra_speed_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            snake_lenght += 1
            snake_speed += 2
        if x1 == extra_slow_x and y1 == extra_slow_y:
            extra_slow_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            extra_slow_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            snake_lenght += 1
            snake_speed -= 2
        clock.tick(snake_speed)
    pygame.quit()
    quit()
gameLoop(snake_speed)