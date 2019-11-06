import pygame
import time
from Game_physics.Movement import *

pygame.init()
screen = pygame.display.set_mode((920, 640))
screen_width = screen.get_width()
screen_height = screen.get_height()
done = False
Fps = 120
gravity = 1
ground = body(list_id=0, pos_x=0, pos_y=screen_height - 50, vel_x=0, vel_y=0, acc_x=0, acc_y=0, height=5000,
              width=screen_width / 2, obj_type='Static')
plate = body(list_id=1, pos_x=screen_width / 2, pos_y=screen_height - 100, vel_x=0, vel_y=0, acc_x=0, acc_y=0,
             height=5000, width=screen_width / 2, obj_type='Static')
rectangle = body(2, pos_x=80, pos_y=0, vel_x=0, vel_y=0, acc_x=0, acc_y=gravity, mass=60, height=50, width=50)
bodies = [ground, plate, rectangle]
for obj in bodies:
    obj.correct_mass(bodies)
move_right = False
move_left = False
start_time = time.time()
while not done:
    while time.time() < (1 / Fps) + start_time:
        continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
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
    screen.fill((0, 0, 0))
    rectangle.check_collision(bodies)
    rectangle.update_position()

    print('x:' + str(rectangle.hit_x_list) + '\n' + 'y' + str(rectangle.hit_y_list))
    x = rectangle.position[0]
    y = rectangle.position[1]
    w = rectangle.width
    h = rectangle.height
    pygame.draw.rect(screen, (255, 0, 0), (x, y, w, h))
    pygame.draw.rect(screen, (255, 255, 0), (ground.position[0], ground.position[1], ground.width, ground.height))
    pygame.draw.rect(screen, (255, 255, 0), (plate.position[0], plate.position[1], plate.width, plate.height))
    pygame.display.update()
    start_time = time.time()

pygame.quit()
