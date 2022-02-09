import pygame
from random import randrange

RES = 700
SIZE = 50

print("Made for CS50 by definit.\nFinal Project!")

menu_screen = pygame.Surface((300, 100))
x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 50
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
score = 0
speed_count, snake_speed = 0, 10
over = False


pygame.init()
pygame.display.set_caption(("Snake"))
surface = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
menu_score = pygame.font.SysFont('Arial', 23, bold=True)
font_end = pygame.font.SysFont('Arial', 40, bold=True)
img = pygame.image.load('background.jpg').convert()

def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

game = True

while game == True:
    surface.blit(img, (0, 0))
    # drawing snake, apple
    [pygame.draw.rect(surface, pygame.Color('green'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
    pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))
    # show score
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    surface.blit(render_score, (5, 5))
    # snake movement
    speed_count += 1
    if not speed_count % snake_speed:
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]
    # eating food
    if snake[-1] == apple:
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length += 1
        score += 1
        snake_speed -= 1
        snake_speed = max(snake_speed, 4)
    # game over
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        over = True
        while True:
            render_end = font_end.render(f'GAME OVER! YOUR SCORE: {score}.', 1, pygame.Color('blue'))
            surface.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            close_game()

    pygame.display.flip()
    clock.tick(fps)
    close_game()
    # controls
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
    elif key[pygame.K_s]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    elif key[pygame.K_a]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
    elif key[pygame.K_d]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True, }