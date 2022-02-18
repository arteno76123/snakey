import pygame
import random


DISTANCE = 20
WIDTH  = DISTANCE * 40
HEIGHT = DISTANCE * 30
BACKGROUND = (0,0,0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game_clock = pygame.time.Clock()
    game_goes_on = True
    #                   x coord                                    y coord
    snake_head = (random.randrange(DISTANCE, WIDTH, DISTANCE), random.randrange(DISTANCE, HEIGHT, DISTANCE))

    snake = [snake_head, (snake_head[0] + DISTANCE, snake_head[1])]

    dx = -DISTANCE
    dy = 0

    fruit = [random.randrange(DISTANCE, WIDTH, DISTANCE), random.randrange(DISTANCE, HEIGHT, DISTANCE)]

    while game_goes_on:
        # process input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_goes_on = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and dy != DISTANCE:
                dx = 0
                dy = -DISTANCE
            if keys[pygame.K_DOWN] and dy != -DISTANCE:
                dx = 0
                dy = DISTANCE
            if keys[pygame.K_LEFT] and dx != DISTANCE:
                dx = -DISTANCE
                dy = 0
            if keys[pygame.K_RIGHT] and dx != -DISTANCE:
                dx = DISTANCE
                dy = 0

        # update the game state
        snake.insert(0, (snake[0][0] + dx, snake[0][1] + dy))

        if tuple(fruit) == snake[0]:
            fruit = [random.randrange(DISTANCE, WIDTH, DISTANCE), random.randrange(DISTANCE, HEIGHT, DISTANCE)]
            while tuple(fruit) in snake:
                fruit = [random.randrange(DISTANCE, WIDTH, DISTANCE), random.randrange(DISTANCE, HEIGHT, DISTANCE)]

        else:
            snake.pop()


        # render
        screen.fill(BACKGROUND)
        for tiny_portion_of_the_snake_body in snake:
            pygame.draw.rect(screen, (0,230,0), (tiny_portion_of_the_snake_body[0], tiny_portion_of_the_snake_body[1], DISTANCE, DISTANCE))

        pygame.draw.circle(screen, (255, 20, 50), (fruit[0] + DISTANCE // 2, fruit[1] + DISTANCE // 2), DISTANCE // 2)
        pygame.display.update()
        game_clock.tick(10)

    pygame.quit()


if __name__ == '__main__':
    main()
