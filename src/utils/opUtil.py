# 主文件
# 系统模块

# 自定义模块
from common.manager import *
from common.res import *
import pygame


def game_over(screen, chess_image):
    success_image = pygame.image.load(success_image_filename).convert()
    screen.blit(success_image, (BOARD_MIDDLE_X -50, BOARD_END_Y+10))
    screen.blit(chess_image, (BOARD_MIDDLE_X - 10, BOARD_END_Y+70))


# chess_board棋盘,chess检测的棋子,返回True,False
def is_success(chess):
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if CHESS_BOARD[i][j] == chess:
                # 横向
                if i + 4 < BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][j] == chess and \
                        CHESS_BOARD[i + 3][j] == chess and CHESS_BOARD[i + 4][j] == chess:
                    return True
                # 纵向
                if j + 4 < BOARD_HEIGHT and CHESS_BOARD[i][j + 1] == chess and CHESS_BOARD[i][j + 2] == chess and \
                        CHESS_BOARD[i][j + 3] == chess and CHESS_BOARD[i][j + 4] == chess:
                    return True
                # 右斜
                if i + 4 < BOARD_WIDTH and j + 4 < BOARD_HEIGHT and CHESS_BOARD[i + 1][j + 1] == chess and \
                        CHESS_BOARD[i + 2][j + 2] == chess and CHESS_BOARD[i + 3][j + 3] == chess and \
                        CHESS_BOARD[i + 4][j + 4] == chess:
                    return True
                # 左斜
                if i - 4 >= 0 and j + 4 >= 0 and CHESS_BOARD[i - 1][j + 1] == chess and CHESS_BOARD[i - 2][
                    j + 2] == chess and CHESS_BOARD[i - 3][j + 3] == chess and CHESS_BOARD[i - 4][j + 4] == chess:
                    return True
    return False


def chess_on_board(event, screen, turn_image, turn):
    x, y = event.pos
    # 棋范围内,5为1/4棋子位移，提高边缘点击体验
    if x >= (BOARD_START_X - 5) and x <= (BOARD_END_X + 5) and y >= (BOARD_START_Y - 5) and y <= (BOARD_END_Y + 5):
        # 最近棋盘坐标
        board_i, board_j = round((x - BOARD_START_X) / SHIFT_X), round((y - BOARD_START_Y) / SHIFT_Y)
        # print("棋盘位置",(board_i,board_j))
        # 已有棋子
        if CHESS_BOARD[board_i][board_j] != 0:
            return False
        # 实际落子开始坐标
        board_x, board_y = BOARD_START_X + board_i * SHIFT_X, BOARD_START_Y + board_j * SHIFT_Y
        # print("坐标",(board_x,board_y))
        # 调整中心,减去棋子的一般=半
        board_x, board_y = board_x - 10, board_y - 10
        # print("调整坐标",(board_x, board_y))
        screen.blit(turn_image, (board_x, board_y))
        CHESS_BOARD[board_i][board_j] = turn
        return True
    return False
