from ChessBoard import ChessBoard
import time

# Check if chess board is full and if is, it displays the board and returns 1
# Else, one by one each column is tried to see if a queen can be properly placed in the next row
# If an available column if found the function is recursively called  and then the queen is removed

# Create file to store solutions
f = open("8QueenRecursiveSolutions.txt", "a")
# Clear file from last run solutions
f.truncate(0)


def recursiveNQueenSolution(chessboard, f):
    size = chessboard.getSize()
    numOfSoln = 0

    # if board is full, display solution
    if size == chessboard.queensCount():
        chessboard.displayBoard(f)
        return 1

    # Recursive Algorthim to solve N-queen problem
    for column in range(size):  # loop through each column
        # If next column is free then:
        if chessboard.checkNextRowColumn(column):
            chessboard.changeRow(column)  # Move queen to next row
            numOfSoln += recursiveNQueenSolution(chessboard, f)
            chessboard.removeQueenFromCurrentRow()  # Remove queen from occupied row

    return numOfSoln


n = int(input('Please enter number of queens and size of board (n): '))
start = time.time()
chessboard = ChessBoard(n)
numOfSoln = recursiveNQueenSolution(chessboard, f)
end = time.time()
totalTime = end - start
print("Soultion have been generated in recursiveSolutions.txt")
print("Runtime for solution recursively is: " + str(totalTime))
print('The Number of solutions:', numOfSoln)
f.close()
