import algorithm.get_score

# 构造构造棋盘
board = [[0 for i in range(15)] for i in range(15)]  # 二维列表
board[2][2] = 1
board[3][2] = 1
board[4][2] = 1
board[5][2] = 1
board[6][2] = 1
print(algorithm.get_score.get_score(1, board))
