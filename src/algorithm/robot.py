import algorithm.max_min
import algorithm.utils
from common.manager import *


def chess1():
    pos = pre_chess()
    # print("预处理:",pos)
    pre_board = pre_chessboard()
    algorithm.max_min.pre_deep(pre_board)
    if pos[0] < 0:
        node = algorithm.max_min.max_min(WHITE_CHESS, MIN, MAX, 0, 0, pre_board, 0)
        pos = node["i"], node["j"]
        # print("robot_pos",pos)
    return pos


# 预处理
def pre_chess():
    first_white=is_first(WHITE_CHESS)
    if first_white[0]>=0:
        return first_white
    first_black=is_first(BLACK_CHESS)
    if first_black[0]>=0:
        return first_black
    second_white=is_second(WHITE_CHESS)
    if second_white[0]>=0:
        return second_white
    second_black=is_second(BLACK_CHESS)
    if second_black[0]>=0:
        return second_black
    return -1,-1

# 是否有半活四，活四，返回堵住点, 优先级1
def is_first(chess):
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if CHESS_BOARD[i][j] == chess:
                # 横向
                if i + 3 < BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][j] == chess and \
                        CHESS_BOARD[i + 3][j] == chess:
                    if i + 4 < BOARD_WIDTH and CHESS_BOARD[i + 4][j] == NONE_CHESS:
                        return i + 4, j
                    if i - 1 >= 0 and CHESS_BOARD[i - 1][j] == NONE_CHESS:
                        return i - 1, j
                # 纵向
                if j + 3 < BOARD_HEIGHT and CHESS_BOARD[i][j + 1] == chess and CHESS_BOARD[i][j + 2] == chess and \
                        CHESS_BOARD[i][j + 3] == chess:
                    if j + 4 < BOARD_HEIGHT and CHESS_BOARD[i][j + 4] == NONE_CHESS:
                        return i, j + 4
                    if j - 1 >= 0 and CHESS_BOARD[i][j - 1] == NONE_CHESS:
                        return i, j - 1
                # 右斜
                if i + 3 < BOARD_WIDTH and j + 3 < BOARD_HEIGHT and CHESS_BOARD[i + 1][j + 1] == chess and \
                        CHESS_BOARD[i + 2][j + 2] == chess and CHESS_BOARD[i + 3][j + 3] == chess:
                    if j + 4 < BOARD_HEIGHT and i + 4 < BOARD_WIDTH and CHESS_BOARD[i + 4][j + 4] == NONE_CHESS:
                        return i + 4, j + 4
                    if j - 1 >= 0 and i - 1 >= 0 and CHESS_BOARD[i - 1][j - 1] == NONE_CHESS:
                        return i - 1, j - 1
                # 左斜
                if i - 3 >= 0 and j + 3 < BOARD_HEIGHT and CHESS_BOARD[i - 1][j + 1] == chess and CHESS_BOARD[i - 2][
                    j + 2] == chess and CHESS_BOARD[i - 3][j + 3] == chess:
                    if j + 4 < BOARD_HEIGHT and i - 4 >= 0 and CHESS_BOARD[i - 4][j + 4] == NONE_CHESS:
                        return i - 4, j + 4
                    if j - 1 >= 0 and i + 1 < BOARD_WIDTH and CHESS_BOARD[i + 1][j - 1] == NONE_CHESS:
                        return i + 1, j - 1
    return (-1, -1)


# 是否有活三，返回堵住点 ,优先级2
def is_second(chess):
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if CHESS_BOARD[i][j] == chess:
                # 横向
                if i + 3 < BOARD_WIDTH and i - 1 >= 0 and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][
                    j] == chess and \
                        CHESS_BOARD[i - 1][j] == NONE_CHESS and CHESS_BOARD[i + 3][j] == NONE_CHESS:
                    if i + 4 < BOARD_WIDTH and CHESS_BOARD[i + 4][j] == NONE_CHESS:
                        return i + 3, j
                    if i - 2 >= 0 and CHESS_BOARD[i - 2][j] == NONE_CHESS:
                        return i - 1, j
                # 纵向
                if j + 3 < BOARD_HEIGHT and j - 1 >= 0 and CHESS_BOARD[i][j + 1] == chess and CHESS_BOARD[i][
                    j + 2] == chess and \
                        CHESS_BOARD[i][j - 1] == NONE_CHESS and CHESS_BOARD[i][j + 3] == NONE_CHESS:
                    if j + 4 < BOARD_WIDTH and CHESS_BOARD[i][j + 4] == NONE_CHESS:
                        return i, j + 3
                    if j - 2 >= 0 and CHESS_BOARD[i][j - 2] == NONE_CHESS:
                        return i, j - 1
                # 右斜
                if i + 3 < BOARD_WIDTH and j + 3 < BOARD_HEIGHT and i - 1 >= 0 and j - 1 >= 0 and CHESS_BOARD[i + 1][
                    j + 1] == chess and \
                        CHESS_BOARD[i + 2][j + 2] == chess and CHESS_BOARD[i - 1][j - 1] == NONE_CHESS and \
                        CHESS_BOARD[i + 3][j + 3] == NONE_CHESS:
                    if j + 4 < BOARD_HEIGHT and i + 4 < BOARD_WIDTH and CHESS_BOARD[i + 4][j + 4] == NONE_CHESS:
                        return i + 3, j + 3
                    if j - 2 >= 0 and i - 2 >= 0 and CHESS_BOARD[i - 2][j - 2] == NONE_CHESS:
                        return i - 1, j - 1
                # 左斜
                if i - 3 >= 0 and j + 3 < BOARD_HEIGHT and CHESS_BOARD[i - 1][
                    j + 1] == chess and i + 1 < BOARD_WIDTH and j - 1 >= 0 and CHESS_BOARD[i - 2][
                    j + 2] == chess and CHESS_BOARD[i + 1][j - 1] == NONE_CHESS and CHESS_BOARD[i - 3][
                    j + 3] == NONE_CHESS:
                    if j + 4 < BOARD_HEIGHT and i - 4 >= 0 and CHESS_BOARD[i - 4][j + 4] == NONE_CHESS:
                        return i - 3, j + 3
                    if j - 2 >= 0 and i + 2 < BOARD_WIDTH and CHESS_BOARD[i + 2][j - 2] == NONE_CHESS:
                        return i + 1, j - 1
    return -1, -1


# 预处理棋盘 OK
def pre_chessboard():
    width = BOARD_WIDTH
    chessboard = [[0 for i in range(BOARD_WIDTH)] for i in range(BOARD_HEIGHT)]
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            chessboard[i][j] = CHESS_BOARD[i][j]
    num = 0  # 记录需要处理的空矩形数
    while width > 5:
        if is_empty(width):
            num += 1
        width -= 2
    width = BOARD_WIDTH
    while num > 1:
        m = (BOARD_WIDTH - width) // 2
        n = (BOARD_WIDTH - width) // 2
        for i in range(width):
            chessboard[m + i][n] = 3
            chessboard[m][n + i] = 3
            chessboard[m + width - 1][n + i] = 3
            chessboard[m + i][n + width - 1] = 3
        num -= 1
        width -= 2
    return chessboard


# 判断一周是否为空 OK
def is_empty(width):
    # 输入错误,奇数输入
    if width % 2 == 0 and width > 5:
        return False
    num = 0
    m = (BOARD_WIDTH - width) // 2
    n = (BOARD_WIDTH - width) // 2
    for i in range(width):
        if CHESS_BOARD[m + i][n] != NONE_CHESS or CHESS_BOARD[m][n + i] != NONE_CHESS or CHESS_BOARD[m + width - 1][
            n + i] != NONE_CHESS or CHESS_BOARD[m + i][n + width - 1] != NONE_CHESS:
            num += 1

    if num < 2:
        return True
    else:
        return False
