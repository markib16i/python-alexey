import pygame

DISPLAY_SIZE = (1200, 975)
FPS = 40

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(DISPLAY_SIZE)
track = pygame.image.load('track1.png')
car1 = pygame.image.load('car1.png')
car2 = pygame.image.load('car2.png')

position = pygame.Vector2(
    DISPLAY_SIZE[0] - 1920,
    DISPLAY_SIZE[1] / 2 - 545
)
velocity = pygame.Vector2()
facing = pygame.Vector2(-1, 0)
acceleration = 100
brake_force = 300


while True:
    dt = clock.tick(FPS) / 1000

    # Очередь событий мы разбираем в начале каждого кадра
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Acceleration in the direction of facing
        velocity += facing * acceleration * dt  # TODO: Vector addition
    if keys[pygame.K_z]:  # Braking till 0
          velocity -= facing * brake_force * dt
          if facing.dot(velocity) < 0:  # TODO: Vector dot product
            velocity = pygame.Vector2()

    position += -velocity * dt

    # if keys[pygame.K_UP]:
    #     coordinates[1] += speed
    # if keys[pygame.K_LEFT]:  # Acceleration in the direction of facing
    #     speed += acceleration
    # if keys[pygame.K_DOWN]:
    #     coordinates[1] -= speed
    # if keys[pygame.K_RIGHT]:
    #     coordinates[0] -= speed
    # coordinates[0] += speed
    # if speed > 0:
    #     speed -= acceleration

    screen.fill(color=pygame.Color('magenta'))
    screen.blit(track, position)
    screen.blit(car1, (725, 465))

    # Рисуем весь кадр
    pygame.display.flip()
    # Задержка между кадрами, чтобы не перегружать процессор, в конце кадра
