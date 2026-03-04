import pygame

DISPLAY_SIZE = (1200, 975)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(DISPLAY_SIZE)
track = pygame.image.load('track1.png')
car1 = pygame.image.load('car1.png')
car2 = pygame.image.load('car2.png')

# Высота 950, ширина 1920
# Старт 1400, 545

while True:
    # Очередь событий мы разбираем в начале каждого кадра
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        print('up')
    if keys[pygame.K_LEFT]:
        print('left')
    if keys[pygame.K_DOWN]:
        print('down')
    if keys[pygame.K_RIGHT]:
        print('right')


    screen.fill(color=pygame.Color('magenta'))
    screen.blit(track, (DISPLAY_SIZE[0] - 1920, DISPLAY_SIZE[1] / 2 - 545))
    screen.blit(car1, (725, 465))
    # Рисуем весь кадр
    pygame.display.flip()
    # Задержка между кадрами, чтобы не перегружать процессор, в конце кадра
    clock.tick(30)
