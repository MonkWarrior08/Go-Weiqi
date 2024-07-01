import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
BOARD_SIZE = 19
CELL_SIZE = 40
STONE_SIZE = 38
MARGIN = 40
BOARD_COLOR = (220, 179, 92)  # Light wood color
LINE_COLOR = (0, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Calculate window size
WINDOW_SIZE = (BOARD_SIZE * CELL_SIZE + 2 * MARGIN, BOARD_SIZE * CELL_SIZE + 2 * MARGIN + 60)

# Set up the display
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Go (Weiqi) Game")

class GoGame:
    def __init__(self):
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
        self.current_player = 1
        self.players = ["Dimi", "Alice"]
        self.score = {1: 0, 2: 0}

    def place_stone(self, x, y):
        if self.board[y][x] != 0:
            return False
        
        self.board[y][x] = self.current_player
        
        captures = self.check_captures(x, y)
        self.score[self.current_player] += captures
        
        self.current_player = 3 - self.current_player  # Switch player (1 -> 2, 2 -> 1)
        return True

    def check_captures(self, x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        captures = 0
        for dx, dy in directions:
            captures += self.capture_group(x + dx, y + dy)
        return captures

    def capture_group(self, x, y):
        if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
            return 0
        if self.board[y][x] == 0 or self.board[y][x] == self.current_player:
            return 0
        
        group = self.find_group(x, y)
        if not any(self.has_liberties(gx, gy) for gx, gy in group):
            for gx, gy in group:
                self.board[gy][gx] = 0
            return len(group)
        return 0

    def find_group(self, x, y):
        color = self.board[y][x]
        group = set()
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in group:
                continue
            group.add((cx, cy))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and self.board[ny][nx] == color:
                    stack.append((nx, ny))
        return group

    def has_liberties(self, x, y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and self.board[ny][nx] == 0:
                return True
        return False

def draw_board():
    screen.fill(BOARD_COLOR)
    
    # Draw the outer border
    pygame.draw.rect(screen, LINE_COLOR, (MARGIN - 1, MARGIN - 1, 
                     BOARD_SIZE * CELL_SIZE + 2, BOARD_SIZE * CELL_SIZE + 2), 2)
    
    for i in range(BOARD_SIZE):
        # Draw horizontal lines
        pygame.draw.line(screen, LINE_COLOR, 
                         (MARGIN - 1, MARGIN + i * CELL_SIZE),
                         (MARGIN + BOARD_SIZE * CELL_SIZE, MARGIN + i * CELL_SIZE))
        # Draw vertical lines
        pygame.draw.line(screen, LINE_COLOR,
                         (MARGIN + i * CELL_SIZE, MARGIN - 1),
                         (MARGIN + i * CELL_SIZE, MARGIN + BOARD_SIZE * CELL_SIZE))

    # Draw star points (hoshi)
    star_points = [3, 9, 15]
    for x in star_points:
        for y in star_points:
            pygame.draw.circle(screen, BLACK, 
                               (MARGIN + x * CELL_SIZE, MARGIN + y * CELL_SIZE), 5)

def draw_stones(board):
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if board[y][x] != 0:
                color = BLACK if board[y][x] == 1 else WHITE
                pygame.draw.circle(screen, color,
                                   (MARGIN + x * CELL_SIZE, MARGIN + y * CELL_SIZE),
                                   STONE_SIZE // 2)

def draw_score(game):
    font = pygame.font.Font(None, 36)
    black_score = font.render(f"Dimi (Black): {game.score[1]}", True, BLACK)
    white_score = font.render(f"Alice (White): {game.score[2]}", True, BLACK)
    screen.blit(black_score, (10, WINDOW_SIZE[1] - 50))
    screen.blit(white_score, (WINDOW_SIZE[0] // 2 + 10, WINDOW_SIZE[1] - 50))

def main():
    game = GoGame()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                board_x = int((x - MARGIN + CELL_SIZE / 2) // CELL_SIZE)
                board_y = int((y - MARGIN + CELL_SIZE / 2) // CELL_SIZE)
                if 0 <= board_x < BOARD_SIZE and 0 <= board_y < BOARD_SIZE:
                    game.place_stone(board_x, board_y)

        draw_board()
        draw_stones(game.board)
        draw_score(game)

        current_player = game.players[game.current_player - 1]
        color = "Black" if game.current_player == 1 else "White"
        turn_text = pygame.font.Font(None, 36).render(f"{current_player}'s turn ({color})", True, BLACK)
        screen.blit(turn_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
