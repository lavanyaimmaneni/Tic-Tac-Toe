import pygame, sys
 
pygame.init()
 
WIDTH, HEIGHT = 900, 900
 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

BOARD = pygame.image.load("Board.png")
X_IMG = pygame.image.load("X.png")
O_IMG = pygame.image.load("O.png")

BG_COLOR = (214, 201, 227)

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
game_board = [[[None, None], [None, None], [None, None]],
                    [[None, None], [None, None], [None, None]],
                    [[None, None], [None, None], [None, None]]]

to_move = 'X'

SCREEN.fill(BG_COLOR)
SCREEN.blit(BOARD, (64, 64))

pygame.display.update()

def Tic_board(board, ximg, oimg):
    global game_board
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                game_board[i][j][0] = ximg
                game_board[i][j][1] = ximg.get_rect(center = (j * 300 + 150, i * 300 + 150))
            elif board[i][j] == 'O':
                game_board[i][j][0] = oimg
                game_board[i][j][1] = oimg.get_rect(center = (j * 300 + 150, i * 300 + 150))

def add_XO(board, game_board, to_move):
    current_pos = pygame.mouse.get_pos()
    converted_x = (current_pos[0] - 65) / 835 * 2
    converted_y = current_pos[1] / 835 * 2
    if board[round(converted_y)][round(converted_x)] != 'O' and board[round(converted_y)][round(converted_x)] != 'X':
        board[round(converted_y)][round(converted_x)] = to_move
        if to_move == 'O':
            to_move = 'X'
        else:
            to_move = 'O'
    
    Tic_board(board, X_IMG, O_IMG)

    for i in range(3):
        for j in range(3):
            if game_board[i][j][0] is not None:
                SCREEN.blit(game_board[i][j][0], game_board[i][j][1])
    
    return board, to_move

game_finished = False

def check_win(board):
    winner = None
    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)):
            winner = board[row][0]
            for i in range(0, 3):
                game_board[row][i][0] = pygame.image.load(f"green {winner}.png")
                SCREEN.blit(game_board[row][i][0], game_board[row][i][1])
            pygame.display.update()
            return winner

    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner =  board[0][col]
            for i in range(0, 3):
                game_board[i][col][0] = pygame.image.load(f"green {winner}.png")
                SCREEN.blit(game_board[i][col][0], game_board[i][col][1])
            pygame.display.update()
            return winner
   
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner =  board[0][0]
        game_board[0][0][0] = pygame.image.load(f"green {winner}.png")
        SCREEN.blit(game_board[0][0][0], game_board[0][0][1])
        game_board[1][1][0] = pygame.image.load(f"green {winner}.png")
        SCREEN.blit(game_board[1][1][0], game_board[1][1][1])
        game_board[2][2][0] = pygame.image.load(f"green {winner}.png")
        SCREEN.blit(game_board[2][2][0], game_board[2][2][1])
        pygame.display.update()
        return winner
          
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner =  board[0][2]
        game_board[0][2][0] = pygame.image.load(f"green {winner}.png")
        SCREEN.blit(game_board[0][2][0], game_board[0][2][1])
        game_board[1][1][0] = pygame.image.load(f"green {winner}.png")
        SCREEN.blit(game_board[1][1][0], gamel_board[1][1][1])
        game_board[2][0][0] = pygame.image.load(f"green {winner}.png")
        SCREEN.blit(game_board[2][0][0], game_board[2][0][1])
        pygame.display.update()
        return winner
    
    if winner is None:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    return None
        return "DRAW"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board, to_move = add_XO(board, game_board, to_move)

            if game_finished:
                board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                game_board = [[[None, None], [None, None], [None, None]],
                                    [[None, None], [None, None], [None, None]],
                                    [[None, None], [None, None], [None, None]]]

                to_move = 'X'

                SCREEN.fill(BG_COLOR)
                SCREEN.blit(BOARD, (64, 64))

                game_finished = False

                pygame.display.update()
            
            if check_win(board) is not None:
                game_finished = True
            
            pygame.display.update()
