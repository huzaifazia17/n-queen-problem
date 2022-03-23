from ChessBoard import ChessBoard
import time

""" 
Create a chessboard object
During each Iteration, colunmns are checked to see in which first available row a queen may be placed. 
This is done using another loop inside the while loop. If such a column exists then place the queen there and stop the inner loop
If a column was not found or the board is full, then we need to backtrack. Incase the board is ful then it should be displayed first.
The backtracking works by removing the queen from the last filled row and have the next iteration try column values above the column values of the queen just removed.
"""
# Create file to store solutions
f = open("8QueenIterativeSolutions.txt", "a")
# Clear file from last run solutions
f.truncate(0)


def iterativeNQueenSolution(size, f):
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
                chessboard.displayBoard(f)
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
    print("Soultion have been generated in iterativeSolutions.txt")
    print('The Number of solutions:', numOfSoln)


n = int(input('Please enter number of queens and size of board (n): '))
start = time.time()
iterativeNQueenSolution(n, f)
end = time.time()
totalTime = end - start
print("Runtime for solution iteratively is: " + str(totalTime))
f.close()
