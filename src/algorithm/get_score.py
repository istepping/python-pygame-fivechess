from common.manager import *


# score_white-score_black,OK
def get_score2(m, n, chessboard):
    white_score = get_score_row(m, n, WHITE_CHESS, chessboard) + get_score_portrait(m, n, WHITE_CHESS,
                                                                                    chessboard) + get_score_rightdown(m,
                                                                                                                      n,
                                                                                                                      WHITE_CHESS,
                                                                                                                      chessboard) + get_score_leftdown(
        m, n, WHITE_CHESS, chessboard)
    black_score = get_score_row(m, n, BLACK_CHESS, chessboard) + get_score_portrait(m, n, BLACK_CHESS,
                                                                                    chessboard) + get_score_rightdown(m,
                                                                                                                      n,
                                                                                                                      BLACK_CHESS,
                                                                                                                      chessboard) + get_score_leftdown(
        m, n, BLACK_CHESS, chessboard)
    return white_score - black_score


def white_score(m, n, chessboard):
    print("行:", get_score_row(m, n, WHITE_CHESS, chessboard),end=",")
    print("列:", get_score_portrait(m, n, WHITE_CHESS, chessboard),end=",")
    print("右斜:", get_score_rightdown(m, n, WHITE_CHESS, chessboard),end=",")
    print("左斜:", get_score_leftdown(m, n, WHITE_CHESS, chessboard),end=",")
    print(" ")


def get_score_portrait(m, n, chess, chessboard):
    new_chessboard = conver_ij(chessboard)
    return get_score_row(n, m, chess, new_chessboard)


def get_score_leftdown(m, n, chess, chessboard):
    result = [[0 for i in range(BOARD_HEIGHT)] for i in range(BOARD_WIDTH)]
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            result[BOARD_WIDTH - 1 - i][j] = chessboard[i][j]
    return get_score_rightdown(BOARD_WIDTH - 1 - m, n, chess, result)


def conver_ij(chessboard):
    result = [[0 for i in range(BOARD_HEIGHT)] for i in range(BOARD_WIDTH)]
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            result[j][i] = chessboard[i][j]
    return result


# 增量式评估算法-给定一位置返回影响的路径分值,m:横坐标，n:纵坐标
def get_score_row(m, n, chess, chessboard):
    score = 0
    # 横向
    i = 0
    while i < BOARD_WIDTH:
        if chessboard[i][n] == chess:
            # 左侧堵住
            if i - 1 < 0 or (i - 1 >= 0 and chessboard[i - 1][n] == other_chess(chess)):
                if i + 1 < BOARD_WIDTH and chessboard[i + 1][n] == chess:
                    if i + 2 < BOARD_WIDTH and chessboard[i + 2][n] == NONE_CHESS:
                        score += SCORE5
                        i += 3
                        continue
                    elif i + 2 < BOARD_WIDTH and chessboard[i + 2][n] == chess:
                        if i + 3 < BOARD_WIDTH and chessboard[i + 3][n] == NONE_CHESS:
                            score += SCORE4
                            i += 4
                            continue
                        elif i + 3 < BOARD_WIDTH and chessboard[i + 3][n] == chess:
                            # 10000形式
                            if i + 4 < BOARD_WIDTH and chessboard[i + 4][n] == NONE_CHESS:
                                score += SCORE3
                                i += 5
                                continue
                            elif i + 4 < BOARD_WIDTH and chessboard[i + 4][n] == chess:
                                score += SCORE1
                                i += 5
                                continue
                            else:
                                i += 5
                                continue
                        else:
                            i += 4
                            continue
                    else:
                        i += 3
                        continue
            # 左侧未堵住
            else:
                if i + 1 < BOARD_WIDTH and chessboard[i + 1][n] == NONE_CHESS:
                    score += SCORE5
                    i += 2
                    continue
                elif i + 1 < BOARD_WIDTH and chessboard[i + 1][n] == chess:
                    # 00 局势
                    if i + 2 < BOARD_WIDTH and chessboard[i + 2][n] == NONE_CHESS:
                        score += SCORE4
                        i += 3
                        continue
                    elif i + 2 < BOARD_WIDTH and chessboard[i + 2][n] == chess:
                        # 000 局势
                        if i + 3 < BOARD_WIDTH and chessboard[i + 3][n] == NONE_CHESS:
                            score += SCORE3
                            i += 4
                            continue
                        elif i + 3 < BOARD_WIDTH and chessboard[i + 3][n] == chess:
                            # 0000 局势
                            if i + 4 < BOARD_WIDTH and chessboard[i + 4][n] == NONE_CHESS:
                                score += SCORE2
                                i += 5
                                continue
                            elif i + 4 < BOARD_WIDTH and chessboard[i + 4][n] == chess:
                                # 00000 局势
                                score += SCORE1
                                i += 5
                                continue
                            else:
                                score += SCORE3
                                i += 5
                                continue
                        else:
                            score += SCORE4
                            i += 4
                            continue
                    else:
                        score += SCORE5
                        i += 3
                        continue
                else:
                    i += 2
                    continue

        i += 1
    return score


def get_score_rightdown(m, n, chess, chessboard):
    score = 0
    # 找起点
    while n > 0 and m > 0:
        m -= 1
        n -= 1
    i = 0
    while m + i < BOARD_WIDTH and n + i < BOARD_HEIGHT:
        if chessboard[m + i][n + i] == chess:
            # 左侧堵住,10
            if i == 0 or (i > 0 and chessboard[m + i - 1][n + i - 1] == other_chess(chess)):
                # print("堵住")
                if m + i + 1 < BOARD_WIDTH and n + i + 1 < BOARD_HEIGHT and chessboard[m + i + 1][n + i + 1] == chess:
                    # 局势 100
                    if m + i + 2 < BOARD_WIDTH and n + i + 2 < BOARD_HEIGHT and chessboard[m + i + 2][
                        n + i + 2] == NONE_CHESS:
                        score += SCORE5
                        i += 3
                        continue
                    elif m + i + 2 < BOARD_WIDTH and n + i + 2 < BOARD_HEIGHT and chessboard[m + i + 2][
                        n + i + 2] == chess:
                        # 局势1000
                        if m + i + 3 < BOARD_WIDTH and n + i + 3 < BOARD_HEIGHT and chessboard[m + i + 3][
                            n + i + 3] == NONE_CHESS:
                            score += SCORE4
                            i += 4
                            continue
                        elif m + i + 3 < BOARD_WIDTH and n + i + 3 < BOARD_HEIGHT and chessboard[m + i + 3][
                            n + i + 3] == chess:
                            # 局势 10000
                            if m + i + 4 < BOARD_WIDTH and n + i + 4 < BOARD_HEIGHT and chessboard[m + i + 4][
                                n + i + 4] == NONE_CHESS:
                                score += SCORE3
                                i += 5
                                continue
                            elif m + i + 4 < BOARD_WIDTH and n + i + 4 < BOARD_HEIGHT and chessboard[m + i + 4][
                                n + i + 4] == chess:
                                # 局势 100000
                                score += SCORE1
                                i += 5
                                continue
                            else:
                                i += 5
                                continue
                        else:
                            i += 4
                            continue
                    else:
                        i += 3
                        continue
            # 左侧未堵住
            else:
                # print("未堵住")
                if m + i + 1 < BOARD_WIDTH and n + i + 1 < BOARD_HEIGHT and chessboard[m + i + 1][
                    n + i + 1] == NONE_CHESS:
                    score += SCORE5
                    i += 2
                    continue
                elif m + i + 1 < BOARD_WIDTH and n + i + 1 < BOARD_HEIGHT and chessboard[m + i + 1][n + i + 1] == chess:
                    # 局势 00
                    if m + i + 2 < BOARD_WIDTH and n + i + 2 < BOARD_HEIGHT and chessboard[m + i + 2][
                        n + i + 2] == NONE_CHESS:
                        score += SCORE4
                        i += 3
                        continue
                    elif m + i + 2 < BOARD_WIDTH and n + i + 2 < BOARD_HEIGHT and chessboard[m + i + 2][
                        n + i + 2] == chess:
                        # 局势 000
                        if m + i + 3 < BOARD_WIDTH and n + i + 3 < BOARD_HEIGHT and chessboard[m + i + 3][
                            n + i + 3] == NONE_CHESS:
                            score += SCORE3
                            i += 4
                            continue
                        elif m + i + 3 < BOARD_WIDTH and n + i + 3 < BOARD_HEIGHT and chessboard[m + i + 3][
                            n + i + 3] == chess:
                            # 局势 0000
                            if m + i + 4 < BOARD_WIDTH and n + i + 4 < BOARD_HEIGHT and chessboard[m + i + 4][
                                n + i + 4] == NONE_CHESS:
                                score += SCORE2
                                i += 5
                                continue
                            elif m + i + 4 < BOARD_WIDTH and n + i + 4 < BOARD_HEIGHT and chessboard[m + i + 4][
                                n + i + 4] == chess:
                                # 局势 00000
                                score += SCORE1
                                i += 5
                                continue
                            else:
                                score += SCORE3
                                i += 5
                                continue
                        else:
                            score += SCORE4
                            i += 4
                            continue
                    else:
                        score += SCORE5
                        i += 3
                        continue
                else:
                    i += 2
                    continue
        i += 1
    return score


def other_chess(chess):
    return (chess % 2) + 1


# 评分算法,chess(黑白棋),chessboard(当前棋盘局势)
def get_score(chess, chessboard):
    score = 0
    # 遍历棋盘
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if chessboard[i][j] == chess:
                print((i, j))
                # 横向
                if i + 4 < BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][j] == chess and \
                        CHESS_BOARD[i + 3][j] == chess and CHESS_BOARD[i + 4][j] == chess:
                    print("横5")
                    score += SCORE1
                    continue
                if i - 1 >= 0 and i + 4 < BOARD_WIDTH and CHESS_BOARD[i - 1][j] == NONE_CHESS and CHESS_BOARD[i + 1][
                    j] == chess and CHESS_BOARD[i + 2][j] == chess and \
                        CHESS_BOARD[i + 3][j] == chess and CHESS_BOARD[i + 4][j] == NONE_CHESS:
                    print("横4")
                    score += SCORE2
                    continue
                if (i - 1 >= 0 and i + 3 < BOARD_WIDTH and CHESS_BOARD[i - 1][j] == NONE_CHESS and CHESS_BOARD[i + 1][
                    j] == chess and CHESS_BOARD[i + 2][j] == chess and CHESS_BOARD[i + 3][j] == NONE_CHESS) \
                        or ((i - 1 < 0 or (i - 1 >= 0 and CHESS_BOARD[i - 1][j] != chess and CHESS_BOARD[i - 1][
                    j] != NONE_CHESS)) and i + 4 < BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and
                            CHESS_BOARD[i + 2][j] == chess and \
                            CHESS_BOARD[i + 3][j] == chess and CHESS_BOARD[i + 4][j] == NONE_CHESS) \
                        or (
                        i + 3 < BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][j] == chess and \
                        CHESS_BOARD[i + 3][j] == chess and (i + 4 == BOARD_WIDTH or (
                        i + 4 < BOARD_WIDTH and CHESS_BOARD[i + 4][j] != chess and CHESS_BOARD[i + 4][
                    j] != NONE_CHESS))):
                    print("横3")
                    score += SCORE3
                if (i - 1 >= 0 and i + 2 < BOARD_WIDTH and CHESS_BOARD[i - 1][j] == NONE_CHESS and CHESS_BOARD[i + 1][
                    j] == chess and CHESS_BOARD[i + 2][j] == NONE_CHESS) \
                        or ((i - 1 < 0 or (
                        i - 1 >= 0 and CHESS_BOARD[i - 1][j] != chess and CHESS_BOARD[i - 1][j] != NONE_CHESS)) and (
                                    i + 3 < BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][
                                j] == chess and CHESS_BOARD[i + 3][j] == NONE_CHESS)) \
                        or (
                        i + 2 < BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][j] == chess and (
                        i + 3 == BOARD_WIDTH or (
                        i + 3 < BOARD_WIDTH and CHESS_BOARD[i + 3][j] != chess and CHESS_BOARD[i + 3][
                    j] != NONE_CHESS))):
                    print("横2")
                    score += SCORE4
                    continue
                if (i - 1 >= 0 and i + 1 < BOARD_WIDTH and CHESS_BOARD[i + 1][j] == NONE_CHESS) \
                        or ((i - 1 < 0 or (
                        i - 1 >= 0 and CHESS_BOARD[i - 1][j] != chess and CHESS_BOARD[i - 1][j] != NONE_CHESS)) and (
                                    i + 2 < BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][
                                j] == NONE_CHESS)) \
                        or (i + 1 < BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and (i + 2 == BOARD_WIDTH or (
                        i + 2 < BOARD_WIDTH and CHESS_BOARD[i + 2][j] != chess and CHESS_BOARD[i + 2][
                    j] != NONE_CHESS))):
                    print("横1")
                    score += SCORE5
                    continue
                # 纵向
                if j + 4 < BOARD_HEIGHT and CHESS_BOARD[i][j + 1] == chess and CHESS_BOARD[i][j + 2] == chess and \
                        CHESS_BOARD[i][j + 3] == chess and CHESS_BOARD[i][j + 4] == chess:
                    score += SCORE1
                # 右斜
                if i + 4 < BOARD_WIDTH and j + 4 < BOARD_HEIGHT and CHESS_BOARD[i + 1][j + 1] == chess and \
                        CHESS_BOARD[i + 2][j + 2] == chess and CHESS_BOARD[i + 3][j + 3] == chess and \
                        CHESS_BOARD[i + 4][j + 4] == chess:
                    score += SCORE1
                # 左斜
                if i - 4 >= 0 and j + 4 >= 0 and CHESS_BOARD[i - 1][j + 1] == chess and CHESS_BOARD[i - 2][
                    j + 2] == chess and CHESS_BOARD[i - 3][j + 3] == chess and CHESS_BOARD[i - 4][j + 4] == chess:
                    score += SCORE1

    return score


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
