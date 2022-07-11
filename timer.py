import pygame
pygame.font.init()
from time import time
from random import randint

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Timer to destroy Ani (Godot)")

size = 75
start = 60
font = pygame.font.SysFont(None, size)
t0 = start + time()
particles = []

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()

    t1 = time()
    timer = round(t0 - t1, 1)
    if timer < 0:
        pygame.quit()
        exit()


    try:
        rand_pos = (randint(-5, 5)  * start * 0.1 / timer, randint(-5, 5)  * start * 0.1 / timer)
    except ZeroDivisionError:
        rand_pos = (0, 0)

    surface = font.render(str(abs(timer)), True, (255, 255/start * timer, 255/start * timer))
    particles.append([[screen.get_width() // 2 + rand_pos[0], screen.get_height() // 2 + rand_pos[1]], [randint(0, 20) / 10 - 1, randint(0, 20) / 10 - 1], randint(10, 50)])
    
    for particle in particles:
        particle[0][0] += particle[1][0] + rand_pos[0]
        particle[0][1] += particle[1][1] + rand_pos[1]
        particle[2] -= 0.1
        pygame.draw.circle(screen, (0, 255 - 255/start * timer, 255 - 255/start * timer), particle[0], particle[2])
        if particle[2] <= 0:
            particles.remove(particle)
    screen.blit(surface, (screen.get_width() // 2 - surface.get_width() // 2 + rand_pos[0], screen.get_height() // 2 - surface.get_height() // 2 + rand_pos[1]))
    
    pygame.display.update()
