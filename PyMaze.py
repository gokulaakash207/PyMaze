import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 30, 30
CELL_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()

def generate_perfect_maze(rows, cols):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]

    def neighbors(r, c):
        dirs = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        random.shuffle(dirs)
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 < nr < rows and 0 < nc < cols and maze[nr][nc] == 1:
                yield nr, nc, dr // 2, dc // 2

    stack = [(1, 1)]
    maze[1][1] = 0

    while stack:
        r, c = stack[-1]
        moved = False
        for nr, nc, mr, mc in neighbors(r, c):
            if maze[nr][nc] == 1:
                maze[r + mr][c + mc] = 0
                maze[nr][nc] = 0
                stack.append((nr, nc))
                moved = True
                break
        if not moved:
            stack.pop()

    maze[1][1] = 0
    maze[rows - 2][cols - 2] = 0
    return maze

# Generate 5 different levels upfront
levels = [generate_perfect_maze(ROWS, COLS) for _ in range(5)]

current_level = 0
maze = levels[current_level]
player_x, player_y = 1, 1
goal_x, goal_y = COLS - 2, ROWS - 2
player_speed = 1
game_won = False
all_levels_complete = False

# Movement timing (in ms)
move_delay = 65 # increase this value to make movement slower
last_move_time = 0

def load_level(level_num):
    global maze, player_x, player_y, goal_x, goal_y, game_won, current_level, all_levels_complete, last_move_time
    if level_num >= len(levels):
        all_levels_complete = True
        return
    current_level = level_num
    maze = levels[current_level]
    player_x, player_y = 1, 1
    goal_x, goal_y = COLS - 2, ROWS - 2
    game_won = False
    last_move_time = pygame.time.get_ticks()

load_level(current_level)

def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            if maze[row][col] == 1:
                pygame.draw.rect(screen, GRAY, (x, y, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)
            else:
                pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))

def draw_player():
    x = player_x * CELL_SIZE + CELL_SIZE // 2
    y = player_y * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, BLUE, (x, y), CELL_SIZE // 3)

def draw_goal():
    x = goal_x * CELL_SIZE + CELL_SIZE // 2
    y = goal_y * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, GREEN, (x, y), CELL_SIZE // 3)

def can_move(x, y):
    if 0 <= y < len(maze) and 0 <= x < len(maze[0]):
        return maze[y][x] == 0
    return False

def draw_text(text, font_size, color, x, y):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

running = True
while running:
    dt = clock.tick(60)  # still cap at 60 FPS
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and game_won:
            if event.key == pygame.K_SPACE:
                if all_levels_complete:
                    levels = [generate_perfect_maze(ROWS, COLS) for _ in range(5)]
                    all_levels_complete = False
                    load_level(0)
                else:
                    load_level(current_level + 1)

    if not game_won:
        # Only allow a move every move_delay ms
        if current_time - last_move_time >= move_delay:
            keys = pygame.key.get_pressed()
            moved = False
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                if can_move(player_x, player_y - player_speed):
                    player_y -= player_speed
                    moved = True
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                if can_move(player_x, player_y + player_speed):
                    player_y += player_speed
                    moved = True
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if can_move(player_x - player_speed, player_y):
                    player_x -= player_speed
                    moved = True
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if can_move(player_x + player_speed, player_y):
                    player_x += player_speed
                    moved = True

            if moved:
                last_move_time = current_time

    if player_x == goal_x and player_y == goal_y:
        game_won = True
        if current_level == len(levels) - 1:
            all_levels_complete = True

    screen.fill(WHITE)
    draw_maze()
    draw_goal()
    draw_player()

    draw_text(f"Level {current_level + 1}/{len(levels)} - Use Arrow Keys or WASD to move", 24, BLACK, WIDTH // 2, 20)

    if game_won:
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 150, HEIGHT // 2 - 50, 300, 100))
        pygame.draw.rect(screen, BLACK, (WIDTH // 2 - 150, HEIGHT // 2 - 50, 300, 100), 3)
        if all_levels_complete:
            draw_text("All Levels Complete!", 40, GREEN, WIDTH // 2, HEIGHT // 2 - 20)
            draw_text("Press SPACE to restart game", 24, BLACK, WIDTH // 2, HEIGHT // 2 + 20)
        else:
            draw_text("Level Complete!", 40, GREEN, WIDTH // 2, HEIGHT // 2 - 20)
            draw_text("Press SPACE for next level", 24, BLACK, WIDTH // 2, HEIGHT // 2 + 20)

    pygame.display.flip()

pygame.quit()
sys.exit()
