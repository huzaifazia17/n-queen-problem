class ChessBoard:
    # Deine the size of the board  (NxN)
    def __init__(self, size):
        self.size = size
        self.columns = []

    # Get Size of board
    def getSize(self):
        return self.size

    # Get number of queens in column
    def queensCount(self):
        return len(self.columns)

    # Move queen to next row
    def changeRow(self, column):
        self.columns.append(column)

    # Remove queen from current row
    def removeQueenFromCurrentRow(self):
        return self.columns.pop()

    # Check if the row of next column over is safe
    def checkNextRowColumn(self, column):
        row = len(self.columns)

        # Check the column
        for currentColumn in self.columns:
            if column == currentColumn:
                return False

        # Check the diagonal
        for currentRow, currentColumn in enumerate(self.columns):
            if currentColumn - currentRow == column - row:
                return False

        # Check inverse diagonal
        for currentRow, currentColumn in enumerate(self.columns):
            if ((self.size - currentColumn) - currentRow
                    == (self.size - column) - row):
                return False

        return True

    # Display Chessboard
    def displayBoard(self):
        for row in range(self.size):
            for column in range(self.size):
                if column == self.columns[row]:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()
