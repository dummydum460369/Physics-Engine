import pygame
import time
from Movement import *

pygame.init()
screen = pygame.display.set_mode((800, 720))
# gravity = 46346.4566929
gravity = 0.01
ground = body(2, 0, 720, 0, 0, 0, 0, 10000, 128000, type='Static')
wall1 = body('owo', 800, 0, 0, 0, 0, 0, 800, 720, type='Static')
wall2 = body('-w-', -2, 0, 0, 0, 0, 0, 2, 720, type='Static')
rectangle = body(3, pos_x=640, pos_y=0, vel_x=0, vel_y=0, acc_x=0, acc_y=gravity, height=50, width=50)
#rectangle2 = body(4, pos_x=640, pos_y=200, vel_x=0, vel_y=0, acc_x=0, acc_y=gravity, height=50, width=200)
bodies = [rectangle, ground, wall2]
running = True
start_time = time.time()
move_left = False
move_right = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rectangle.position[0] += -5
                move_left = True
            if event.key == pygame.K_RIGHT:

                move_right = True
            if event.key == pygame.K_SPACE:
                rectangle.velocity[1] = -25
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                rectangle.velocity[0] = 0
                move_left = False
            if event.key == pygame.K_RIGHT:
                rectangle.velocity[0] = 0
                move_right = False
    if move_right:
        rectangle.position[0] += 5
    if move_left:
        rectangle.position[0] -= 5
    while time.time() < 1 / 120 + start_time:
        continue
    start_time = time.time()
    screen.fill((0, 0, 0))
    print('x:', rectangle.hit_x_list)
    print('y:', rectangle.hit_y_list)
    rectangle.check_collision(bodies)
    rectangle.update_position()
    #rectangle2.update_position()
    rectangle.check_collision(bodies)
    #rectangle2.check_collision(bodies)
    x = rectangle.position[0]
    y = rectangle.position[1]
    w = rectangle.width
    h = rectangle.height
    pygame.draw.rect(screen, (255, 0, 0), (x, y, w, h))
    pygame.draw.rect(screen, (255, 255, 0), (ground.position[0], ground.position[1], ground.width, ground.height))
    #pygame.draw.rect(screen, (255, 255, 0),
                     #(rectangle2.position[0], rectangle2.position[1], rectangle2.width, rectangle2.height))
    print(rectangle.position)
    pygame.display.update()

pygame.quit()
