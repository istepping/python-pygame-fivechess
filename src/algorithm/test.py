import algorithm.get_score
import algorithm.robot
import algorithm.max_min
from common.manager import *
import algorithm.utils
# 构造构造棋盘
board = [[0 for i in range(15)] for i in range(15)]  # 二维列表
board[2][2] = 2
board[3][2] = 2
board[4][2] = 2
board[2][3] = 1
board[3][3] = 1
board[4][3] = 1
# print(algorithm.get_score.get_score(1, board))
# 循环测试
# for i in range(10):
#     i+=3
#     print(i,end=',')
# print("评估函数测试")


# 机器人落点测试
# print(algorithm.max_min.max_min(WHITE_CHESS, MIN, MAX, 0, 0, board, 1))
def is_empty():
    algorithm.utils.print_board(CHESS_BOARD)
    print(15, algorithm.robot.is_empty(15))
    print(13, algorithm.robot.is_empty(13))
    print(11, algorithm.robot.is_empty(11))
    print(9, algorithm.robot.is_empty(9))
    print(7, algorithm.robot.is_empty(7))

