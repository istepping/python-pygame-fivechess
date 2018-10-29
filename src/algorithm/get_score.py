from common.manager import *


# 评分算法,chess(黑白棋),chessboard(当前棋盘局势)
def get_score(chess, chessboard):
    score = 0
    # 遍历棋盘
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if chessboard[i][j] == chess:
                print((i,j))
                # 横向
                if i + 4 < BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][j] == chess and \
                        CHESS_BOARD[i + 3][j] == chess and CHESS_BOARD[i + 4][j] == chess:
                    print("横5")
                    score += SCORE1
                    continue
                if i-1>=0 and i+4<BOARD_WIDTH and CHESS_BOARD[i - 1][j]==NONE_CHESS and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][j] == chess and \
                        CHESS_BOARD[i + 3][j] == chess and CHESS_BOARD[i + 4][j] == NONE_CHESS:
                    print("横4")
                    score+=SCORE2
                    continue
                if (i-1>=0 and i+3<BOARD_WIDTH and CHESS_BOARD[i - 1][j]==NONE_CHESS and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][j] == chess and CHESS_BOARD[i + 3][j] == NONE_CHESS) \
                        or ((i-1<0 or (i-1>=0 and CHESS_BOARD[i - 1][j]!=chess and CHESS_BOARD[i-1][j]!=NONE_CHESS)) and i+4<BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][j] == chess and \
                        CHESS_BOARD[i + 3][j] == chess and CHESS_BOARD[i + 4][j] == NONE_CHESS) \
                        or (i+3<BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][j] == chess and \
                        CHESS_BOARD[i + 3][j] == chess and (i+4==BOARD_WIDTH or (i+4<BOARD_WIDTH and CHESS_BOARD[i + 4][j] != chess and CHESS_BOARD[i + 4][j] != NONE_CHESS))):
                    print("横3")
                    score+=SCORE3
                if (i-1>=0 and i+2<BOARD_WIDTH and CHESS_BOARD[i - 1][j]==NONE_CHESS and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][j] == NONE_CHESS) \
                        or ((i-1<0 or (i-1>=0 and CHESS_BOARD[i - 1][j]!=chess and CHESS_BOARD[i - 1][j]!=NONE_CHESS))and (i+3<BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][j] == chess and CHESS_BOARD[i+3][j]==NONE_CHESS))\
                        or (i+2<BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][j] == chess and (i+3==BOARD_WIDTH or (i+3<BOARD_WIDTH and CHESS_BOARD[i + 3][j] != chess and CHESS_BOARD[i + 3][j] != NONE_CHESS))):
                    print("横2")
                    score+=SCORE4
                    continue
                if (i-1>=0 and i+1<BOARD_WIDTH and CHESS_BOARD[i+1][j]==NONE_CHESS)\
                    or ((i-1<0 or (i-1>=0 and CHESS_BOARD[i - 1][j]!=chess and CHESS_BOARD[i - 1][j]!=NONE_CHESS))and (i+2<BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and CHESS_BOARD[i + 2][j] == NONE_CHESS))\
                    or (i+1<BOARD_WIDTH and CHESS_BOARD[i + 1][j] == chess and (i+2==BOARD_WIDTH or (i+2<BOARD_WIDTH and CHESS_BOARD[i + 2][j] != chess and CHESS_BOARD[i + 2][j] != NONE_CHESS))):
                    print("横1")
                    score+=SCORE5
                    continue
                # 纵向
                if j + 4 < BOARD_HEIGHT and CHESS_BOARD[i][j + 1] == chess and CHESS_BOARD[i][j + 2] == chess and \
                        CHESS_BOARD[i][j + 3] == chess and CHESS_BOARD[i][j + 4] == chess:
                    score+=SCORE1
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