def print_board(chessboard):
    for i in range(len(chessboard)):
        for j in range(len(chessboard)):
            print(chessboard[i][j],end=",")
        print(" ")
