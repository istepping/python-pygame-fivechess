from common.screen import *
import algorithm.get_score

WHITE_CHESS = 1  # 白棋
BLACK_CHESS = 2  # 黑棋
NONE_CHESS = 0  # 空位
CHESS_BOARD = [[0 for i in range(BOARD_WIDTH)] for i in range(BOARD_HEIGHT)]  # 二维列表
SCORE1 = 100000  # 连五
SCORE2 = 10000  # 活四
SCORE3 = 1000  # 活三,半活四
SCORE4 = 100  # 活二,半活三
SCORE5 = 10  # 活一，半活二

SEARCH_DEEP = 2
SEARCH_DEEP2 = 3
WHITE_MAP = []  # 记录白棋路径
BLACK_MAP = []  # 记录黑棋路径
SCORE_LIST = [[0 for i in range(BOARD_WIDTH)] for i in range(BOARD_HEIGHT)]  # 二维列表,值为分数值
# 最大最小
MAX = 1000000000
MIN = -1000000000


def update_score(i, j):
    score = algorithm.get_score.get_score2(i, j, CHESS_BOARD)
    for m in range(len(SCORE_LIST)):
        SCORE_LIST[m][j] = score
        SCORE_LIST[i][m] = score
    m, n = i, j
    while m - 1 >= 0 and j - 1 >= 0:
        SCORE_LIST[m - 1][n - 1] = score
        m -= 1
        n -= 1
    m, n = i, j
    while m + 1 < BOARD_WIDTH and n + 1 < BOARD_HEIGHT:
        SCORE_LIST[m + 1][n + 1] = score
        m += 1
        n += 1
    m, n = i, j
    while m + 1 < BOARD_WIDTH and j - 1 >= 0:
        SCORE_LIST[m + 1][j - 1] = score
        m += 1
        n -= 1
    m, n = i, j
    while m - 1 >= 0 and n + 1 < BOARD_HEIGHT:
        SCORE_LIST[m - 1][n + 1] = score
        m -= 1
        n += 1
