input1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
output1 = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
input2 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
output2 = [["5","1","9","7","4","8","6","3","2"],["7","8","3","6","5","2","4","1","9"],["4","2","6","1","3","9","8","7","5"],["3","5","7","9","8","6","2","4","1"],["2","6","4","3","1","7","5","9","8"],["1","9","8","5","2","4","3","6","7"],["9","7","5","8","6","3","1","2","4"],["8","3","2","4","9","1","7","5","6"],["6","4","1","2","7","5","9","8","3"]]

class Solution:
    def solveSudoku(self, board):
        print()

solution = Solution()
solution.solveSudoku(input1)
print('RESULTS 1 -----------------------------------', input1==output1)
for r in input1:
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