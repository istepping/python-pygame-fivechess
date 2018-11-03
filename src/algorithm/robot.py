import algorithm.max_min
from algorithm.utils import *
import random
from common.manager import *


def chess2(chess):
    pos = pre_chess2(chess)
    pre_board = pre_chessboard2(pre_chessboard())
    algorithm.max_min.pre_deep(pre_board)
    # print("预处理棋盘")
    # print_board(pre_board)
    if pos[0] < 0:
        node = algorithm.max_min.max_min2(chess, MIN, MAX, 0, 0, pre_board, 0)
        pos = node["i"], node["j"]
    return pos


def chess1(chess):
    pos = pre_chess(chess)
    # print("预处理:",pos)
    pre_board = pre_chessboard()
    # algorithm.max_min.pre_deep(pre_board)
    if pos[0] < 0:
        node = algorithm.max_min.max_min(chess, MIN, MAX, 0, 0, pre_board, 0)
        pos = node["i"], node["j"]
        # print("robot_pos",pos)
    return pos


def pre_chess2(chess):
    first_chess = chess_first(chess)
    if first_chess[0] >= 0:
        return first_chess
    first_white = is_first(chess)
    if first_white[0] >= 0:
        return first_white
    first_black = is_first(other_chess(chess))
    if first_black[0] >= 0:
        return first_black
    second_white = is_second(chess)
    if second_white[0] >= 0:
        return second_white
    second_black = is_second(other_chess(chess))
    if second_black[0] >= 0:
        return second_black
    third_chess = is_third(chess)
    if third_chess[0] >= 0:
        return third_chess
    third_other_chess = is_third(other_chess(chess))
    if third_other_chess[0] >= 0:
        return third_other_chess
    return -1, -1


# 预处理
def pre_chess(chess):
    first_chess = chess_first(chess)
    if first_chess[0] >= 0:
        return first_chess
    first_white = is_first(chess)
    if first_white[0] >= 0:
        return first_white
    first_black = is_first(other_chess(chess))
    if first_black[0] >= 0:
        return first_black
    second_white = is_second(chess)
    if second_white[0] >= 0:
        return second_white
    second_black = is_second(other_chess(chess))
    if second_black[0] >= 0:
        return second_black
    return -1, -1


def chess_first(chess):
    if len(WHITE_MAP) + len(BLACK_MAP) <= 4:
        choice_point = [(6, 6), (8, 6), (7, 7), (6, 8), (8, 8)]
        choice = random.randint(0, 4)
        if CHESS_BOARD[choice_point[choice][0]][choice_point[choice][1]] == NONE_CHESS:
            return choice_point[choice]
        else:
            for i in choice_point:
                if CHESS_BOARD[i[0]][i[1]] == NONE_CHESS:
                    return i

    return -1, -1


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


# 加强棋力，活二判断,己方优先,优先级3
def is_third(chess):
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if CHESS_BOARD[i][j] == NONE_CHESS:
                CHESS_BOARD[i][j] = chess  # 预落子
                if three_num(chess) + f_four_num(chess) > 1:
                    CHESS_BOARD[i][j] = NONE_CHESS
                    return i, j
                CHESS_BOARD[i][j] = NONE_CHESS
    return -1, -1


def three_num(chess):
    num = 0
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if CHESS_BOARD[i][j] == chess:
                # 横向
                if i + 3 < BOARD_WIDTH and i - 1 >= 0 and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][
                    j] == chess and \
                        CHESS_BOARD[i - 1][j] == NONE_CHESS and CHESS_BOARD[i + 3][j] == NONE_CHESS:
                    if (i + 4 < BOARD_WIDTH and CHESS_BOARD[i + 4][j] == NONE_CHESS) or (
                            i - 2 >= 0 and CHESS_BOARD[i - 2][j] == NONE_CHESS):
                        num += 1
                # 纵向
                if j + 3 < BOARD_HEIGHT and j - 1 >= 0 and CHESS_BOARD[i][j + 1] == chess and CHESS_BOARD[i][
                    j + 2] == chess and \
                        CHESS_BOARD[i][j - 1] == NONE_CHESS and CHESS_BOARD[i][j + 3] == NONE_CHESS:
                    if (j + 4 < BOARD_WIDTH and CHESS_BOARD[i][j + 4] == NONE_CHESS) or (
                            j - 2 >= 0 and CHESS_BOARD[i][j - 2] == NONE_CHESS):
                        num += 1
                # 右斜
                if i + 3 < BOARD_WIDTH and j + 3 < BOARD_HEIGHT and i - 1 >= 0 and j - 1 >= 0 and CHESS_BOARD[i + 1][
                    j + 1] == chess and \
                        CHESS_BOARD[i + 2][j + 2] == chess and CHESS_BOARD[i - 1][j - 1] == NONE_CHESS and \
                        CHESS_BOARD[i + 3][j + 3] == NONE_CHESS:
                    if (j + 4 < BOARD_HEIGHT and i + 4 < BOARD_WIDTH and CHESS_BOARD[i + 4][j + 4] == NONE_CHESS) or (
                            j - 2 >= 0 and i - 2 >= 0 and CHESS_BOARD[i - 2][j - 2] == NONE_CHESS):
                        num += 1
                # 左斜
                if i - 3 >= 0 and j + 3 < BOARD_HEIGHT and CHESS_BOARD[i - 1][
                    j + 1] == chess and i + 1 < BOARD_WIDTH and j - 1 >= 0 and CHESS_BOARD[i - 2][
                    j + 2] == chess and CHESS_BOARD[i + 1][j - 1] == NONE_CHESS and CHESS_BOARD[i - 3][
                    j + 3] == NONE_CHESS:
                    if (j + 4 < BOARD_HEIGHT and i - 4 >= 0 and CHESS_BOARD[i - 4][j + 4] == NONE_CHESS) or (
                            j - 2 >= 0 and i + 2 < BOARD_WIDTH and CHESS_BOARD[i + 2][j - 2] == NONE_CHESS):
                        num += 1
    return num


def f_four_num(chess):
    num = 0
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if CHESS_BOARD[i][j] == chess:
                # 横向
                if i + 3 < BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][j] == chess and \
                        CHESS_BOARD[i + 3][j] == chess:
                    if (i + 4 < BOARD_WIDTH and CHESS_BOARD[i + 4][j] == NONE_CHESS) or (
                            i - 1 >= 0 and CHESS_BOARD[i - 1][j] == NONE_CHESS):
                        num += 1
                # 纵向
                if j + 3 < BOARD_HEIGHT and CHESS_BOARD[i][j + 1] == chess and CHESS_BOARD[i][j + 2] == chess and \
                        CHESS_BOARD[i][j + 3] == chess:
                    if (j + 4 < BOARD_HEIGHT and CHESS_BOARD[i][j + 4] == NONE_CHESS) or (
                            j - 1 >= 0 and CHESS_BOARD[i][j - 1] == NONE_CHESS):
                        num += 1
                # 右斜
                if i + 3 < BOARD_WIDTH and j + 3 < BOARD_HEIGHT and CHESS_BOARD[i + 1][j + 1] == chess and \
                        CHESS_BOARD[i + 2][j + 2] == chess and CHESS_BOARD[i + 3][j + 3] == chess:
                    if (j + 4 < BOARD_HEIGHT and i + 4 < BOARD_WIDTH and CHESS_BOARD[i + 4][j + 4] == NONE_CHESS) or (
                            j - 1 >= 0 and i - 1 >= 0 and CHESS_BOARD[i - 1][j - 1] == NONE_CHESS):
                        num += 1
                # 左斜
                if i - 3 >= 0 and j + 3 < BOARD_HEIGHT and CHESS_BOARD[i - 1][j + 1] == chess and CHESS_BOARD[i - 2][
                    j + 2] == chess and CHESS_BOARD[i - 3][j + 3] == chess:
                    if (j + 4 < BOARD_HEIGHT and i - 4 >= 0 and CHESS_BOARD[i - 4][j + 4] == NONE_CHESS) or (
                            j - 1 >= 0 and i + 1 < BOARD_WIDTH and CHESS_BOARD[i + 1][j - 1] == NONE_CHESS):
                        num += 1
    return num


# 深层预处理棋盘 OK
def pre_chessboard2(chessboard):
    if len(WHITE_MAP) + len(BLACK_MAP) <= 4:
        return chessboard
    # print("棋盘")
    # print_board(chessboard)
    top = (7, 0)
    get_top = False
    bottom = (7, 14)
    get_bottom = False
    left = (0, 7)
    get_left = False
    right = (14, 7)
    get_right = False
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if chessboard[i][j] == WHITE_CHESS or chessboard[i][j] == BLACK_CHESS:
                left = i, j
                get_left = True
                break
        if get_left:
            break
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if chessboard[j][i] == WHITE_CHESS or chessboard[j][i] == BLACK_CHESS:
                top = j, i
                get_top = True
                break
        if get_top:
            break
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if chessboard[BOARD_WIDTH - 1 - i][j] == WHITE_CHESS or chessboard[BOARD_WIDTH - 1 - i][j] == BLACK_CHESS:
                right = BOARD_WIDTH - 1 - i, j
                # print("right", right)
                get_right = True
                break
        if get_right:
            break
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if chessboard[j][BOARD_HEIGHT - 1 - i] == WHITE_CHESS or chessboard[j][BOARD_HEIGHT - 1 - i] == BLACK_CHESS:
                bottom = j, BOARD_HEIGHT - 1 - i
                get_bottom = True
                break
        if get_bottom:
            break
    # print("left", left)
    # print("right", right)
    # print("top", top)
    # print("bottom", bottom)
    L = [left[0], top[1]]
    R = [right[0], bottom[1]]
    if L[0] - 1 >= 0:
        L[0] -= 1
    if L[1] - 1 >= 0:
        L[1] -= 1
    if R[0] + 1 < BOARD_WIDTH:
        R[0] += 1
    if R[1] + 1 < BOARD_HEIGHT:
        R[1] += 1
    # print("L=", L, end=',')
    # print("R=", R)
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if (not (i >= L[0] and i <= R[0] and j >= L[1] and j <= R[1])) and chessboard[i][j] == NONE_CHESS:
                chessboard[i][j] = 3
    return chessboard


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


def other_chess(chess):
    return (chess % 2) + 1
