# 主文件
# 系统模块

# 自定义模块
from common.manager import *
from common.res import *
import pygame
import algorithm.get_score

# 当前标记点
current_pos = (-1, -1)
current_chess = 0


# OK
def game_over(screen, win_chess):
    pos = SCREEN_SIZE[0] / 2 - 3, 70
    if win_chess == WHITE_CHESS:
        message = "白棋胜"
    elif win_chess == BLACK_CHESS:
        message = "黑棋胜"
    else:
        message = "平局"
    font = pygame.font.SysFont("SimHei", 32)
    text = font.render(message, True, (255, 0, 0))
    textRect=text.get_rect()
    textRect.center=pos
    screen.blit(text, textRect)
    pygame.display.update()
    # print("白棋",WHITE_MAP)
    # print("黑棋",BLACK_MAP)

def draw_five(screen,list):
    for i in list:
        board_x, board_y = BOARD_START_X + i[0] * SHIFT_X, BOARD_START_Y + i[1] * SHIFT_Y
        pygame.draw.circle(screen, (255, 0, 0), (int(board_x), int(board_y)), 4, 4)

# chess_board棋盘,chess检测的棋子,返回True,False OK
def is_success(chess,screen):
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if CHESS_BOARD[i][j] == chess:
                # 横向
                if i + 4 < BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][j] == chess and \
                        CHESS_BOARD[i + 3][j] == chess and CHESS_BOARD[i + 4][j] == chess:
                    m_list=[]
                    m_list.append((i,j))
                    m_list.append((i+1, j))
                    m_list.append((i+2, j))
                    m_list.append((i+3, j))
                    m_list.append((i+4, j))
                    draw_five(screen,m_list)
                    return chess
                # 纵向
                if j + 4 < BOARD_HEIGHT and CHESS_BOARD[i][j + 1] == chess and CHESS_BOARD[i][j + 2] == chess and \
                        CHESS_BOARD[i][j + 3] == chess and CHESS_BOARD[i][j + 4] == chess:
                    m_list=[]
                    m_list.append((i,j))
                    m_list.append((i, j+1))
                    m_list.append((i, j+2))
                    m_list.append((i, j+3))
                    m_list.append((i, j+4))
                    draw_five(screen,m_list)
                    return chess
                # 右斜
                if i + 4 < BOARD_WIDTH and j + 4 < BOARD_HEIGHT and CHESS_BOARD[i + 1][j + 1] == chess and \
                        CHESS_BOARD[i + 2][j + 2] == chess and CHESS_BOARD[i + 3][j + 3] == chess and \
                        CHESS_BOARD[i + 4][j + 4] == chess:
                    m_list=[]
                    m_list.append((i,j))
                    m_list.append((i+1, j+1))
                    m_list.append((i+2, j+2))
                    m_list.append((i+3, j+3))
                    m_list.append((i+4, j+4))
                    draw_five(screen,m_list)
                    return chess
                # 左斜
                if i - 4 >= 0 and j + 4 < BOARD_HEIGHT and CHESS_BOARD[i - 1][j + 1] == chess and CHESS_BOARD[i - 2][
                    j + 2] == chess and CHESS_BOARD[i - 3][j + 3] == chess and CHESS_BOARD[i - 4][j + 4] == chess:
                    m_list=[]
                    m_list.append((i,j))
                    m_list.append((i-1, j+1))
                    m_list.append((i-2, j+2))
                    m_list.append((i-3, j+3))
                    m_list.append((i-4, j+4))
                    draw_five(screen,m_list)
                    return chess
    if is_chessboardFull(CHESS_BOARD):
        return 3
    else:
        return False


# OK
def chess_on_board(pos, screen, turn_image, turn):
    # print("点击位置:",pos)
    x, y = pos
    # 棋范围内,5为1/4棋子位移，提高边缘点击体验
    if x >= (BOARD_START_X - 5) and x <= (BOARD_END_X + 5) and y >= (BOARD_START_Y - 5) and y <= (BOARD_END_Y + 5):
        # 最近棋盘坐标
        board_i, board_j = round((x - BOARD_START_X) / SHIFT_X), round((y - BOARD_START_Y) / SHIFT_Y)
        # print("计算落子位置",(board_i, board_j))
        return chess((board_i, board_j), screen, turn_image, turn)
    return False


# 固定棋盘位置落子
def chess(pos, screen, turn_image, turn):
    global current_chess, current_pos
    board_i = pos[0]
    board_j = pos[1]
    # print("当前棋盘",CHESS_BOARD)
    # 已有棋子
    if CHESS_BOARD[board_i][board_j] != 0:
        return False
    # 实际落子开始坐标
    board_x, board_y = BOARD_START_X + board_i * SHIFT_X, BOARD_START_Y + board_j * SHIFT_Y
    # 调整中心,减去棋子的一般=半
    board_x, board_y = board_x - 10, board_y - 10
    screen.blit(turn_image, (board_x, board_y))
    CHESS_BOARD[board_i][board_j] = turn
    # 落子成功
    if current_chess != NONE_CHESS:
        if current_chess == WHITE_CHESS:
            screen.blit(pygame.image.load(white_chess_image_filename).convert_alpha(), current_pos)
        else:
            screen.blit(pygame.image.load(black_chess_image_filename).convert_alpha(), current_pos)
    current_pos = board_x, board_y
    current_chess = turn
    pygame.draw.circle(screen, (255, 0, 0), ((int(board_x) + 10), (int(board_y)) + 10), 4, 4)
    # 记录路径
    if turn == WHITE_CHESS:
        WHITE_MAP.append((board_i, board_j))
        # algorithm.get_score.white_score(board_i, board_j, CHESS_BOARD)
    else:
        BLACK_MAP.append((board_i, board_j))
    return True


def is_chessboardFull(chessboard):
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if chessboard[i][j] == 0:
                return False
    return True
