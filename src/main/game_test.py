import algorithm.get_score
from common.manager import *


def test1():
    # print("当前评分(横):", algorithm.get_score.get_score_row(3,2,WHITE_CHESS, chessboard=CHESS_BOARD))
    # print("当前评分(纵):", algorithm.get_score.get_score_portrait(3,2,WHITE_CHESS, chessboard=CHESS_BOARD))
    # print("当前评分(右下):", algorithm.get_score.get_score_rightdown(3, 2, WHITE_CHESS, chessboard=CHESS_BOARD))
    # print("当前评分(左下):", algorithm.get_score.get_score_leftdown(11, 2, BLACK_CHESS, chessboard=CHESS_BOARD))
     print("当前评分:", algorithm.get_score.get_score2(3, 2, CHESS_BOARD))