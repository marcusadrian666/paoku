import pygame
import random
import sys

pygame.init()

# 设置游戏窗口大小
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Subway Surfer")

# 定义颜色
WHITE = (255, 255, 255)

# 定义玩家初始位置和速度
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - 100
player_speed = 5

# 定义地铁跑酷障碍物
obstacles = []

def generate_obstacle():
    size = random.randint(50, 100)
    obstacle = pygame.Rect(random.randint(0, SCREEN_WIDTH - size), -size, size, size)
    obstacles.append(obstacle)

def move_obstacles():
    for obstacle in obstacles:
        obstacle.y += player_speed

def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, WHITE, obstacle)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH:
        player_x += player_speed

    screen.fill((0, 0, 0))

    # 生成障碍物
    if random.randint(0, 100) < 3:
        generate_obstacle()

    # 移动和绘制障碍物
    move_obstacles()
    draw_obstacles()

    # 绘制玩家
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, 50, 50))

    pygame.display.flip()
    clock.tick(60)
