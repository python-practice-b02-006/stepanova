import pygame

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode([640, 480])

pygame.display.set_caption("My first pygame app window caption")

done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    pygame.draw.line(screen, BLUE, [100, 50], [100, 150], 5)
    pygame.draw.line(screen, BLUE, [400, 50], [400, 150], 5)

    pygame.draw.lines(screen, BLUE, False, [[270, 150], [270, 50], [320, 50], [320, 150]])

    pygame.draw.ellipse(screen, BLUE, [50, 70, 100, 60], 5)
    pygame.draw.ellipse(screen, BLUE, [350, 70, 100, 60], 5)
    pygame.draw.ellipse(screen, BLUE, [170, 50, 70, 100], 5)

    pygame.display.flip()

pygame.quit()
