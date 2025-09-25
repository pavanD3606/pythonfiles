import pygame, random, sys

pygame.init()
w, h = 500, 700
win = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

wh_player = pygame.Rect(w//2 - 25, h - 60, 50, 50)
wh_blocks = []
for _ in range(5):
    x = random.randint(0, w - 50)
    y = random.randint(-700, -50)
    wh_blocks.append(pygame.Rect(x, y, 50, 50))

font = pygame.font.SysFont(None, 48)
score = 0
speed = 5

def draw():
    win.fill((20, 20, 40))
    pygame.draw.rect(win, (0, 200, 255), wh_player)
    for b in wh_blocks:
        pygame.draw.rect(win, (255, 255, 255), b)
        label = font.render("wh", True, (0, 0, 0))
        win.blit(label, (b.x + 5, b.y + 5))
    txt = font.render(f"{score}", True, (255, 255, 255))
    win.blit(txt, (10, 10))
    pygame.display.flip()

def end():
    txt = font.render("wh over", True, (255, 0, 0))
    win.blit(txt, (w//2 - txt.get_width()//2, h//2))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and wh_player.left > 0:
        wh_player.move_ip(-6, 0)
    if keys[pygame.K_RIGHT] and wh_player.right < w:
        wh_player.move_ip(6, 0)

    for b in wh_blocks:
        b.move_ip(0, speed)
        if b.top > h:
            b.top = random.randint(-700, -50)
            b.left = random.randint(0, w - 50)
            score += 1
            speed += 0.05
        if wh_player.colliderect(b):
            end()

    draw()
    clock.tick(60)

