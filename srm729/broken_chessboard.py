chessboard = ["WWB", "BWW", "BBB"]


class BrokenChessboard:
    def minimumFixes(self, board):
        minFix1, minFix2 = 0, 0
        for i in range(0, len(board), 2):
            for j in range(len(board[i])):
                if ((j % 2 == 0) and board[i][j] != "B"): minFix1 = minFix1 + 1                
                if ((j % 2 == 1) and board[i][j] != "W"): minFix1 = minFix1 + 1
                if ((j % 2 == 0) and board[i][j] != "W"): minFix2 = minFix2 + 1
                if ((j % 2 == 1) and board[i][j] != "B"): minFix2 = minFix2 + 1

        for i in range(1, len(board), 2):
            for j in range(len(board[i])):
                if ((j % 2 == 0) and board[i][j] != "W"): minFix1 = minFix1 + 1
                if ((j % 2 == 1) and board[i][j] != "B"): minFix1 = minFix1 + 1
                if ((j % 2 == 0) and board[i][j] != "B"): minFix2 = minFix2 + 1
                if ((j % 2 == 1) and board[i][j] != "W"): minFix2 = minFix2 + 1

	return min(minFix1, minFix2)

