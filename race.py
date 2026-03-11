import pygame

DISPLAY_SIZE = (1200, 975)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(DISPLAY_SIZE)
track = pygame.image.load('track1.png')
car1 = pygame.image.load('car1.png')
car2 = pygame.image.load('car2.png')
coordinates = [
    DISPLAY_SIZE[0] - 1920,
    DISPLAY_SIZE[1] / 2 - 545
]
speed = 0
acceleration = 5

while True:
    # Очередь событий мы разбираем в начале каждого кадра
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        coordinates[1] += speed
    if keys[pygame.K_LEFT]:
        speed += acceleration
    if keys[pygame.K_DOWN]:
        coordinates[1] -= speed
    if keys[pygame.K_RIGHT]:
        coordinates[0] -= speed
    coordinates[0] += speed
    if speed > 0:
        speed -= acceleration

    screen.fill(color=pygame.Color('magenta'))
    screen.blit(track, coordinates)
    screen.blit(car1, (725, 465))

    # Рисуем весь кадр
    pygame.display.flip()
    # Задержка между кадрами, чтобы не перегружать процессор, в конце кадра
    clock.tick(0)
