import algorithm.get_score
from common.manager import *
import algorithm.utils


def max_min2(chess, alpha, beta, i, j, chessboard, search_deep):
    # algorithm.utils.print_board(chessboard)
    if is_chessboardFull(chessboard) or search_deep >= SEARCH_DEEP2:
        score = algorithm.get_score.get_score2(i, j, chessboard)
        # print("子节点评估", {"i": i, "j": j, "score": score})
        return {"i": i, "j": j, "score": score}
    if chess == WHITE_CHESS:
        # print("白棋")
        for k in range(BOARD_WIDTH):
            for r in range(BOARD_HEIGHT):
                if chessboard[k][r] == NONE_CHESS:
                    # print("预落子:",(k,r))
                    chessboard[k][r] = chess  # 落子
                    search_deep += 1  # 搜索下一层
                    result = max_min2(algorithm.get_score.other_chess(chess), alpha, beta, k, r, chessboard,
                                      search_deep)
                    chessboard[k][r] = NONE_CHESS  # 重置棋盘
                    search_deep -= 1  # 恢复搜索深度
                    # 递归回溯处理,极大，减枝
                    if result["score"] > alpha:
                        alpha = result["score"]
                        i = k
                        j = r
                    if alpha >= beta:
                        return result
        # print(search_deep,"层返回:",{"i": i, "j": j, "score": alpha})
        return {"i": i, "j": j, "score": alpha}
    else:
        # 极小搜索
        # print("黑棋")
        for k in range(BOARD_WIDTH):
            for r in range(BOARD_HEIGHT):
                if chessboard[k][r] == NONE_CHESS:
                    # print("预落子:", (k, r))
                    chessboard[k][r] = chess  # 落子
                    search_deep += 1  # 搜索下一层
                    result = max_min2(algorithm.get_score.other_chess(chess), alpha, beta, k, r, chessboard,
                                      search_deep)
                    chessboard[k][r] = NONE_CHESS  # 重置棋盘
                    search_deep -= 1  # 恢复搜索深度
                    # 递归回溯处理,极小，减枝
                    if result["score"] < beta:
                        beta = result["score"]
                        i = k
                        j = r
                    if alpha >= beta:
                        return result
        return {"i": i, "j": j, "score": beta}


def max_min(chess, alpha, beta, i, j, chessboard, search_deep):
    if is_chessboardFull(chessboard) or search_deep >= SEARCH_DEEP:
        score = algorithm.get_score.get_score2(i, j, chessboard)
        # print("子节点评估", {"i": i, "j": j, "score": score})
        return {"i": i, "j": j, "score": score}
    if chess == WHITE_CHESS:
        # 极大搜索
        # print("白棋")
        score = MIN
        for k in range(BOARD_WIDTH):
            for r in range(BOARD_HEIGHT):
                if chessboard[k][r] == NONE_CHESS:
                    # 搜索
                    # print("搜索",(k,r))
                    chessboard[k][r] = chess  # 落子
                    search_deep += 1  # 搜索下一层
                    result = max_min(algorithm.get_score.other_chess(chess), alpha, beta, k, r, chessboard, search_deep)
                    chessboard[k][r] = NONE_CHESS  # 重置棋盘
                    search_deep -= 1  # 恢复搜索深度
                    # 递归回溯处理,极大，减枝
                    if result["score"] > alpha:
                        alpha = result["score"]
                        i = k
                        j = r
                    if alpha >= beta:
                        return result
        return {"i": i, "j": j, "score": alpha}
    else:
        # 极小搜索
        # print("黑棋")
        score = MAX
        for k in range(BOARD_WIDTH):
            for r in range(BOARD_HEIGHT):
                if chessboard[k][r] == NONE_CHESS:
                    # 搜索
                    # print("搜索", (k, r))
                    chessboard[k][r] = chess  # 落子
                    search_deep += 1  # 搜索下一层
                    result = max_min(algorithm.get_score.other_chess(chess), alpha, beta, k, r, chessboard, search_deep)
                    chessboard[k][r] = NONE_CHESS  # 重置棋盘
                    search_deep -= 1  # 恢复搜索深度
                    # 递归回溯处理,极小，减枝
                    if result["score"] < beta:
                        beta = result["score"]
                        i = k
                        j = r
                    if alpha >= beta:
                        return result
        return {"i": i, "j": j, "score": beta}


def minus_max(chess, alpha, beta, i, j, chessboard, search_deep):
    node = {"i": i, "j": j, "score": MIN}  # 当前节点信息
    if is_chessboardFull(chessboard) or search_deep >= SEARCH_DEEP:
        score = algorithm.get_score.get_score2(i, j, chessboard)
        return {"i": i, "j": j, "score": score}
    # 负极大搜索,遍历每一种走法
    for k in range(BOARD_WIDTH):
        for r in range(BOARD_HEIGHT):
            if chessboard[k][r] == NONE_CHESS:
                # 搜索
                chessboard[k][r] = chess  # 落子
                search_deep += 1  # 搜索下一层
                result = minus_max(algorithm.get_score.other_chess(chess), -beta, -alpha, k, r, chessboard, search_deep)
                result["score"] *= -1  # 恢复
                # 极大
                if result["score"] > node["score"]:
                    node["i"] = k
                    node["j"] = r
                    node["score"] = result["score"]
                # 减枝
                alpha = max(alpha, node["score"])
                if result["score"] <= node["score"]:
                    return node
                chessboard[k][r] = NONE_CHESS  # 重置棋盘
                search_deep -= 1  # 恢复搜索深度
    return node


def is_chessboardFull(chessboard):
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if chessboard[i][j] == 0:
                return False
    return True


# 搜索深度预处理
def pre_deep(chessboard):
    num = 0
    global SEARCH_DEEP2
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if chessboard[i][j] == NONE_CHESS:
                num += 1
    if num < 10:
        SEARCH_DEEP2 = 6
    elif num < 30:
        SEARCH_DEEP2 = 4
    else:
        SEARCH_DEEP2 = 2
