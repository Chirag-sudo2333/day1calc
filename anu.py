import pygame
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D GTA-lite")

# Colors
GREEN = (50, 200, 50)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# Player
player_size = 40
player_x, player_y = WIDTH//2, HEIGHT//2
player_speed = 5
sprint_speed = 8
player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

# Car
car_size = 50
car_x, car_y = 200, 200
car_speed = 0
car_rect = pygame.Rect(car_x, car_y, car_size, car_size)

# NPCs
npc_size = 40
npcs = [pygame.Rect(100 + i*100, 100, npc_size, npc_size) for i in range(3)]

# Bullets
bullets = []

running = True
while running:
    screen.fill(GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            bx = player_rect.centerx
            by = player_rect.centery
            dx = mx - bx
            dy = my - by
            dist = max(1, (dx**2 + dy**2)**0.5)
            vel_x = dx / dist * 10
            vel_y = dy / dist * 10
            bullets.append({'rect': pygame.Rect(bx, by, 5,5), 'vel': (vel_x, vel_y)})

    # Keys
    keys = pygame.key.get_pressed()
    speed = sprint_speed if keys[pygame.K_LSHIFT] else player_speed

    if keys[pygame.K_w]:
        player_rect.y -= speed
    if keys[pygame.K_s]:
        player_rect.y += speed
    if keys[pygame.K_a]:
        player_rect.x -= speed
    if keys[pygame.K_d]:
        player_rect.x += speed

    # Car driving
    if keys[pygame.K_UP]:
        car_speed += 0.2
    elif keys[pygame.K_DOWN]:
        car_speed -= 0.2
    else:
        car_speed *= 0.9
    if keys[pygame.K_LEFT]:
        car_rect.x -= 0.5
    if keys[pygame.K_RIGHT]:
        car_rect.x += 0.5
    car_rect.y += car_speed

    # Draw NPCs
    for npc in npcs:
        pygame.draw.rect(screen, RED, npc)

    # Draw player
    pygame.draw.rect(screen, BLUE, player_rect)

    # Draw car
    pygame.draw.rect(screen, GRAY, car_rect)

    # Update bullets
    for b in bullets[:]:
        b['rect'].x += b['vel'][0]
        b['rect'].y += b['vel'][1]
        pygame.draw.rect(screen, YELLOW, b['rect'])
        # Check collision with NPCs
        for npc in npcs:
            if b['rect'].colliderect(npc):
                npcs.remove(npc)
                if b in bullets:
                    bullets.remove(b)
        # Remove bullet if out of screen
        if not screen.get_rect().colliderect(b['rect']):
            bullets.remove(b)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
