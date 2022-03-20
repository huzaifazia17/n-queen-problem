from ChessBoard import ChessBoard
import time

# Check if chess board is full and if is, it displays the board and returns 1
# Else, one by one each column is tried to see if a queen can be properly placed in the next row
# If an available column if found the function is recursively called  and then the queen is removed


def recursiveNQueenSolution(chessboard):
    size = chessboard.getSize()
    numOfSoln = 0
    # To check runtime of one solution
    # if(numOfSoln == 1):
    # return

    # if board is full, display solution
    if size == chessboard.queensCount():
        chessboard.displayBoard()
        print()
        return 1

    # Recursive Algorthim to solve N-queen problem
    for column in range(size):  # loop through each column
        # If next column is free then:
        if chessboard.checkNextRowColumn(column):
            chessboard.changeRow(column)  # Move queen to next row
            numOfSoln += recursiveNQueenSolution(chessboard)
            chessboard.removeQueenFromCurrentRow()  # Remove queen from occupied row

    return numOfSoln


n = int(input('Please enter number of queens and size of board (n): '))
start = time.time()
chessboard = ChessBoard(n)
numOfSoln = recursiveNQueenSolution(chessboard)
end = time.time()
totalTime = end - start
print("Runtime for 1 solution iteratively is: " + str(totalTime))
print('The Number of solutions:', numOfSoln)
