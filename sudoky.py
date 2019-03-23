input1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
output1 = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
input2 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
output2 = [["5","1","9","7","4","8","6","3","2"],["7","8","3","6","5","2","4","1","9"],["4","2","6","1","3","9","8","7","5"],["3","5","7","9","8","6","2","4","1"],["2","6","4","3","1","7","5","9","8"],["1","9","8","5","2","4","3","6","7"],["9","7","5","8","6","3","1","2","4"],["8","3","2","4","9","1","7","5","6"],["6","4","1","2","7","5","9","8","3"]]

import itertools

class Solution:
    allOptions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self):
        self.toSolve = 9 * 9
        self.options = [[[]] * 9] * 9
        #^ above is wrong, the * screwes things up

    def solveSudoku(self, board):
        self.initializeSudoku(board)
        iteration = 0
        while self.toSolve > 0:
            iteration += 1
            if self.easyCheck(board):
                continue
            # if self.intermediateCheck(board):
            #     continue
            # self.complexCheck(board)
            print (iteration)
            if iteration >= 10:
                break

    def removeOptions(self, toRemove, optionsList):
        for remove in toRemove:
            for item in optionsList:
                for spot in item:
                    if spot.count(remove) > 0:
                        spot.remove(remove)

    def nakedSingle(self, board):
        for r in range(9):
            for c in range(9):
                if self.options[r][c] != '.' and len(self.options[r][c]) == 1:
                    board[r][c] = self.options[r][c][0]
                    self.removeOptions(self.options[r][c], [self.getRow(r, self.options), self.getCol(c, self.options), self.getSqr(r, c, self.options)])
                    self.options[r][c] = '.'
                    return True
        return False

    def hiddenSingle(self, board):
        for r in range(9):
            for c in range(9):
                if self.options[r][c] != '.':
                    rowOptions = self.getRow(r, self.options)
                    colOptions = self.getCol(c, self.options)
                    sqrOptions = self.getSqr(r, c, self.options)
                    for option in self.options[r][c]:
                        if rowOptions.count(option) == 1 or colOptions.count(option) == 1 or sqrOptions.count(option) == 1:
                            board[r][c] = option
                            self.removeOptions([option], [rowOptions, colOptions, sqrOptions])
                            self.options[r][c] = '.'
                            return True
        return False

    def pointingPair(self, board):
        found = False
        return found

    def easyCheck(self, board):
        return self.nakedSingle(board) or self.hiddenSingle(board) or self.pointingPair(board)

    # def intermediateCheck(self, board): # TODO
    #     return self.nakedPair(board) or self.hiddenPair(board) or self.pointingTriple(board)

    # def complexCheck(self, board): # TODO
    #     return self.nakedTriple(board) or self.hiddenTriple(board) # Could add Quads and Quints

    def initializeSudoku(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    self.toSolve -= 1
                    self.options[r][c] = '.'
                else:
                    row = self.getRow(r, board)
                    col = self.getCol(c, board)
                    sqr = self.getSqr(r, c, board)
                    self.options[r][c] = [option for option in Solution.allOptions if option not in row and option not in col and option not in sqr]
    
    def getRow(self, row, board):
        return board[row]

    def getCol(self, col, board):
        return [row[col] for row in board]

    def getSqr(self, row, col, board):
        rowRange = int(row / 3) * 3
        colRange = int(col / 3) * 3
        lst = []
        for r in range(rowRange, rowRange + 3):
            for c in range(colRange, colRange + 3):
                lst.append(board[r][c])
        return lst

#--------------------------------------------------------------------------------------------------------------------------------------
solution = Solution()
solution.solveSudoku(input1)
print('RESULTS 1 -----------------------------------', input1==output1)
for r in input1:
    print(r)
for r in solution.options:
    print(r)
if input1==output1:
    solution.solveSudoku(input2)
    print('RESULTS 2 -----------------------------------', input2==output2)
    for r in input2:
        print(r)

# def getSudokuCol(self, colIndex, board):
#     lst = []
#     for r in range(9):
#         if board[r][colIndex] != '.':
#             lst.append(board[r][colIndex])
#     return lst
        
# def getSudokuRow(self, rowIndex, board):
#     lst = []
#     for c in range(9):
#         if board[rowIndex][c] != '.':
#             lst.append(board[rowIndex][c])
#     return lst
    
# def getSudokuSqr(self, rowIndex, colIndex, board):
#     lst = []
#     rowStart, colStart = int(rowIndex/3)*3, int(colIndex/3)*3
#     for r in range(rowStart, rowStart+3):
#         for c in range(colStart, colStart+3):
#             if board[r][c] != '.':
#                 lst.append(board[r][c])
#     return lst

# def getSudokuOtherRows(self, rowIndex, board):
#     lst = []
#     rowStart = int(rowIndex/3)*3
#     for r in range(rowStart, rowStart+3):
#         if r != rowIndex:
#             lst.append(self.getSudokuRow(r, board))
#     return lst

# def getSudokuOtherCols(self, colIndex, board):
#     lst = []
#     colStart = int(colIndex/3)*3
#     for c in range(colStart, colStart+3):
#         if c != colIndex:
#             lst.append(self.getSudokuCol(c, board))
#     return lst

# def solveSudoku(self, board):
#     empties = 1
#     iteration = 0
#     while empties > 0 and iteration != 20:
#         empties = 0
#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == '.':
#                     rows = self.getSudokuRow(r, board)
#                     cols = self.getSudokuCol(c, board)
#                     sqr = self.getSudokuSqr(r, c, board)
#                     allOptions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#                     options = [value for value in allOptions if value not in rows and value not in cols and value not in sqr]
#                     if iteration == 49:
#                         print (options)
#                     if len(options) == 1:
#                         board[r][c] = options[0]
#                     else:
#                         found = False
#                         for option in options:
#                             otherRows = self.getSudokuOtherRows(r, board)
#                             otherCols = self.getSudokuOtherCols(c, board)
                            
#                             if option in otherRows[0] and option in otherRows[1] and option in otherCols[0] and option in otherCols[1]:
#                                 found = True
#                                 board[r][c] = option
#                                 break
#                         if not found:
#                             empties += 1
#         iteration += 1