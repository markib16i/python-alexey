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
transmission = 1
rotation_speed = 10

while True:
    dt = clock.tick(FPS) / 1000

    # Очередь событий мы разбираем в начале каждого кадра
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                transmission *= -1
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        facing.rotate_ip(rotation_speed * dt)
    if keys[pygame.K_RIGHT]:
        facing.rotate_ip(-rotation_speed * dt)
    if keys[pygame.K_a]:  # Газ
        velocity += transmission * facing * acceleration * dt
    if keys[pygame.K_z]:  # Тормоз
        if velocity.length() > 0:
            velocity -= velocity.normalize() * brake_force * dt
        if velocity.length() < brake_force * dt:
            velocity = pygame.Vector2()

    position += -velocity * dt

    screen.blit(track, position)
    screen.blit(car1, (725, 465))

    # Рисуем весь кадр
    pygame.display.flip()
    # Задержка между кадрами, чтобы не перегружать процессор, в конце кадра
