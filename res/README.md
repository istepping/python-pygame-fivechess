# 系统工作
1. 棋盘落子位置:
 * 获取点击位置(mouse_x,mouse_y)
 * 相对棋盘位置(mouse_x-BOARD_START_X,mouse-BOARD_START_Y)->(mouse_board_x,mouse_board_y)
 * 取整计算最近位置:棋盘坐标位置(round(mouse_board_x/SHIFT_X),round(mouse_board_y/SHIFT_Y))
2. 算杀:
 * 白子为例
 * 遍历棋盘 横，竖，右斜，左斜判断
 * 满足条件退出