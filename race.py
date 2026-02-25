import pygame

DISPLAY_SIZE = (1200, 975)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(DISPLAY_SIZE)
track = pygame.image.load('track1.png')
# Высота 950, ширина 1920
# Старт 1400, 545

while True:
    # Очередь событий мы разбираем в начале каждого кадра
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(color=pygame.Color('magenta'))
    screen.blit(track, (DISPLAY_SIZE[0] - 1920, DISPLAY_SIZE[1] / 2 - 545))

    # Рисуем весь кадр
    pygame.display.flip()
    # Задержка между кадрами, чтобы не перегружать процессор, в конце кадра
    clock.tick(30)
