from ChessBoard import ChessBoard
import time


def iterativeNQueenSolution(size):
    chessboard = ChessBoard(size)
    numOfSoln = 0
    row = 0
    column = 0

    # while true iterate over rows
    while True:
        while column < size:
            # If next column is available then:
            if chessboard.checkNextRowColumn(column):
                # Change row of queen, place queen in next row
                chessboard.changeRow(column)
                row += 1
                column = 0
                break
            else:
                column += 1

        # If no empty columnn OR board is full
        if (column == size or row == size):
            # Solution achieved if the board is full
            if row == size:
                chessboard.displayBoard()
                print()
                numOfSoln += 1
                # To check runtime of one solution
                # if(numOfSoln == 1):
                # return
                # Backtracking algorithim
            try:
                previousColumn = chessboard.removeQueenFromCurrentRow()
            except IndexError:
                # All queens have been removed and no more possible configurations
                break
            # Try last row
            row -= 1
            # Start checking at 1 + value of the column in the previous row)
            column = 1 + previousColumn

    print('The Number of solutions:', numOfSoln)


n = int(input('Please enter number of queens and size of board (n): '))
start = time.time()
iterativeNQueenSolution(n)
end = time.time()
totalTime = end - start
print("Runtime for 1 solution iteratively is: " + str(totalTime))
