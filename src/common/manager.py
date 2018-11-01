from common.screen import *

WHITE_CHESS = 1  # 白棋
BLACK_CHESS = 2  # 黑棋
NONE_CHESS = 0  # 空位
CHESS_BOARD = [[0 for i in range(BOARD_WIDTH)] for i in range(BOARD_HEIGHT)]  # 二维列表
SCORE1 = 10000000  # 连五
SCORE2 = 100000  # 活四
SCORE3 = 50000  # 活三,半活四
SCORE4 = 100  # 活二,半活三
SCORE5 = 10  # 活一，半活二

SEARCH_DEEP = 4
WHITE_MAP = []  # 记录白棋路径
BLACK_MAP = []  # 记录黑棋路径

# 最大最小
MAX = 1000000000
MIN = -1000000000

