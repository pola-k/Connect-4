import numpy as np
import pygame

rows = 6
columns = 7
pygame.init()
screen = pygame.display.set_mode((1280, 720))  # 1280 720
pygame.display.set_caption("Connect 4")
clock = pygame.time.Clock()
running = True
initialised = False
turn = 2
board = []
get_column_index = []
end_game = False
total_slots = rows * columns
filled = 0
changed = False
valid = False
x = 0
y = 0
font = pygame.font.Font(None, 60)


def initialise(row, column):
    return np.zeros((row, column), dtype=int)


def change_turns(player):
    if player == 1:
        player = 2
    else:
        player = 1
    return player


def check_winner(board, row, cols, player):

    count = 0
    for i in range(0, columns):
        if board[row][i] == player:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0

    count = 0
    for i in range(0, rows):
        if board[i][cols] == player:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0

    count = 0

    start_row = row
    start_col = cols
    end_row = row
    end_col = cols

    while start_row > 0 and start_col > 0:
        start_row -= 1
        start_col -= 1

    while end_row < rows and end_col < columns:
        end_row += 1
        end_col += 1

    while start_row < end_row and start_col < end_col:
        if board[start_row][start_col] == player:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0
        start_row += 1
        start_col += 1

    count = 0

    start_row = row
    start_col = cols
    end_row = row
    end_col = cols

    while (start_row + 1) < rows and (start_col - 1) > 0:
        start_row += 1
        start_col -= 1

    while (end_row - 1) > 0 and (end_col + 1) < columns:
        end_row -= 1
        end_col += 1

    while start_row >= end_row and start_col <= end_col:
        if board[start_row][start_col] == player:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0
        start_row -= 1
        start_col += 1

    return False


def play(board, player, index, row, cols):
    index[cols] -= 1
    board[row][cols] = player
    return check_winner(board, row, cols, player)


def display_board(board):
    x = 0
    for c in range(0, columns):
        x += 150
        y = 120
        for r in range(0, rows):
            if board[r][c] == 0:
                pygame.draw.circle(screen, "white", (x, y), 30)
            elif board[r][c] == 1:
                pygame.draw.circle(screen, "red", (x, y), 30)
            else:
                pygame.draw.circle(screen, "yellow", (x, y), 30)
            y += 90


while running:
    if not end_game and filled < total_slots:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not changed:
                    turn = change_turns(turn)
                    changed = True

                x, y = event.pos
                x = x / 150
                x = round(x)
                x -= 1
                if ((x >= 0) and (x < columns)) and get_column_index[x] >= 0:
                    changed = False
                    valid = True
                    y = get_column_index[x]

        if not initialised:
            board = initialise(rows, columns)
            turn = 2
            get_column_index = np.full(columns, rows - 1)
            initialised = True

        screen.fill("blue")
        display_board(board)
        pygame.display.flip()
        if valid:
            end_game = play(board, turn, get_column_index, y, x)
            filled += 1
            valid = False
    else:
        count = 0
        while count < 1000:
            if end_game:
                if turn == 1:
                    text = font.render("Player 1 Wins", True, "black")
                else:
                    text = font.render("Player 2 Wins", True, "black")
            else:
                text = font.render("Match Drawn", True, "black")
            screen.fill("white")
            screen.blit(text, (640, 360))
            pygame.display.flip()
            count += 1
        running = False

pygame.quit()
