import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # Циан
    (255, 255, 0),  # Желтый
    (255, 165, 0),  # Оранжевый
    (0, 0, 255),    # Синий
    (0, 255, 0),    # Зеленый
    (255, 0, 0),    # Красный
    (128, 0, 128)   # Фиолетовый
]

# Формы фигур
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]   # J
]

# Звуки
pygame.mixer.init()
rotate_sound = pygame.mixer.Sound("rotate.wav")
clear_sound = pygame.mixer.Sound("clear.wav")
game_over_sound = pygame.mixer.Sound("game_over.wav")

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Тетрис")

# Часы для управления FPS
clock = pygame.time.Clock()

class Tetris:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.game_over = False
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.paused = False

    def new_piece(self):
        shape = random.choice(SHAPES)
        color = random.choice(COLORS)
        return {
            'shape': shape,
            'color': color,
            'x': self.width // 2 - len(shape[0]) // 2,
            'y': 0
        }

    def valid_move(self, piece, x, y):
        for i, row in enumerate(piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    new_x = x + j
                    new_y = y + i
                    if new_x < 0 or new_x >= self.width or new_y >= self.height or (new_y >= 0 and self.grid[new_y][new_x]):
                        return False
        return True

    def place_piece(self):
        for i, row in enumerate(self.current_piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece['y'] + i][self.current_piece['x'] + j] = self.current_piece['color']
        self.clear_lines()
        self.current_piece = self.next_piece
        self.next_piece = self.new_piece()
        if not self.valid_move(self.current_piece, self.current_piece['x'], self.current_piece['y']):
            self.game_over = True
            game_over_sound.play()

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.grid) if all(row)]
        for i in lines_to_clear:
            del self.grid[i]
            self.grid.insert(0, [0 for _ in range(self.width)])
        if lines_to_clear:
            clear_sound.play()
            self.lines_cleared += len(lines_to_clear)
            self.score += len(lines_to_clear) ** 2 * 100
            if self.lines_cleared >= self.level * 10:
                self.level += 1

    def move(self, dx, dy):
        new_x = self.current_piece['x'] + dx
        new_y = self.current_piece['y'] + dy
        if self.valid_move(self.current_piece, new_x, new_y):
            self.current_piece['x'] = new_x
            self.current_piece['y'] = new_y

    def rotate(self):
        piece = self.current_piece
        shape = piece['shape']
        new_shape = [list(row) for row in zip(*shape[::-1])]
        if self.valid_move({'shape': new_shape, 'x': piece['x'], 'y': piece['y']}, piece['x'], piece['y']):
            piece['shape'] = new_shape
            rotate_sound.play()

    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, cell, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        for i, row in enumerate(self.current_piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.current_piece['color'], ((self.current_piece['x'] + j) * BLOCK_SIZE, (self.current_piece['y'] + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        # Отрисовка следующей фигуры
        font = pygame.font.SysFont("comicsans", 20)
        label = font.render("Next Piece", 1, WHITE)
        screen.blit(label, (SCREEN_WIDTH - 120, 10))
        for i, row in enumerate(self.next_piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.next_piece['color'], (SCREEN_WIDTH - 120 + j * BLOCK_SIZE, 50 + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        # Отрисовка счета и уровня
        score_label = font.render(f"Score: {self.score}", 1, WHITE)
        level_label = font.render(f"Level: {self.level}", 1, WHITE)
        screen.blit(score_label, (10, SCREEN_HEIGHT - 60))
        screen.blit(level_label, (10, SCREEN_HEIGHT - 30))

        if self.paused:
            pause_label = font.render("PAUSED", 1, WHITE)
            screen.blit(pause_label, (SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2 - 20))

def main():
    game = Tetris(SCREEN_WIDTH // BLOCK_SIZE, SCREEN_HEIGHT // BLOCK_SIZE)
    fall_time = 0
    fall_speed = 0.5

    while not game.game_over:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move(-1, 0)
                if event.key == pygame.K_RIGHT:
                    game.move(1, 0)
                if event.key == pygame.K_DOWN:
                    game.move(0, 1)
                if event.key == pygame.K_UP:
                    game.rotate()
                if event.key == pygame.K_p:
                    game.paused = not game.paused

        if not game.paused:
            delta_time = clock.get_rawtime() / 1000
            fall_time += delta_time
            if fall_time >= fall_speed / game.level:
                fall_time = 0
                game.move(0, 1)
                if not game.valid_move(game.current_piece, game.current_piece['x'], game.current_piece['y'] + 1):
                    game.place_piece()

        game.draw(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()