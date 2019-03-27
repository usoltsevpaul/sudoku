class Solution:
    def solveSudoku(self, board):
        self.board = board
        self.options = {}
        self.initialize()
        self.solve()

    def solve(self):
        minIndex, key = 10, (-1, -1)
        for k in self.options:
            if len(self.options[k]) > 0 and len(self.options[k]) < minIndex and self.board[k[0]][k[1]] == '.':
                key, minIndex = k, len(self.options[k])
        if key == (-1, -1):
            return True
        for option in self.options[key]:
            if self.isValidOption(key, option):
                self.board[key[0]][key[1]] = option
                if self.solve():
                    return True
                self.board[key[0]][key[1]] = '.'
        return False

    def isValidOption(self, key, option):
        rowItems = self.board[key[0]]
        colItems = [row[key[1]] for row in self.board]
        sqrItems = self.getSqr(key[0], key[1], self.board)
        return option not in rowItems and option not in colItems and option not in sqrItems

    def initialize(self):
        for row in range(9):
            rowItems = self.board[row]
            for col in range(9):
                colItems = [row[col] for row in self.board]
                sqrItems = self.getSqr(row, col, self.board)
                self.options[(row, col)] = []
                if self.board[row][col] == '.':
                    possible = ['1','2','3','4','5','6','7','8','9']
                    for option in possible:
                        if (option not in rowItems and option not in colItems and option not in sqrItems):
                            self.options[(row, col)].append(option)
    
    def getSqr(self, row, col, board):
        rowRange = int(row / 3) * 3
        colRange = int(col / 3) * 3
        lst = []
        for r in range(rowRange, rowRange + 3):
            for c in range(colRange, colRange + 3):
                lst.append(board[r][c])
        return lst

###
input1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
output1 = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
input2 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
output2 = [["5","1","9","7","4","8","6","3","2"],["7","8","3","6","5","2","4","1","9"],["4","2","6","1","3","9","8","7","5"],["3","5","7","9","8","6","2","4","1"],["2","6","4","3","1","7","5","9","8"],["1","9","8","5","2","4","3","6","7"],["9","7","5","8","6","3","1","2","4"],["8","3","2","4","9","1","7","5","6"],["6","4","1","2","7","5","9","8","3"]]
input3 = [[".",".",".","2",".",".",".","6","3"],["3",".",".",".",".","5","4",".","1"],[".",".","1",".",".","3","9","8","."],[".",".",".",".",".",".",".","9","."],[".",".",".","5","3","8",".",".","."],[".","3",".",".",".",".",".",".","."],[".","2","6","3",".",".","5",".","."],["5",".","3","7",".",".",".",".","8"],["4","7",".",".",".","1",".",".","."]]
output3 = [["8","5","4","2","1","9","7","6","3"],["3","9","7","8","6","5","4","2","1"],["2","6","1","4","7","3","9","8","5"],["7","8","5","1","2","6","3","9","4"],["6","4","9","5","3","8","1","7","2"],["1","3","2","9","4","7","8","5","6"],["9","2","6","3","8","4","5","1","7"],["5","1","3","7","9","2","6","4","8"],["4","7","8","6","5","1","2","3","9"]]
input4 = [[".",".",".",".",".","7",".",".","9"],[".","4",".",".","8","1","2",".","."],[".",".",".","9",".",".",".","1","."],[".",".","5","3",".",".",".","7","2"],["2","9","3",".",".",".",".","5","."],[".",".",".",".",".","5","3",".","."],["8",".",".",".","2","3",".",".","."],["7",".",".",".","5",".",".","4","."],["5","3","1",".","7",".",".",".","."]]
output4 = [["3","1","2","5","4","7","8","6","9"],["9","4","7","6","8","1","2","3","5"],["6","5","8","9","3","2","7","1","4"],["1","8","5","3","6","4","9","7","2"],["2","9","3","7","1","8","4","5","6"],["4","7","6","2","9","5","3","8","1"],["8","6","4","1","2","3","5","9","7"],["7","2","9","8","5","6","1","4","3"],["5","3","1","4","7","9","6","2","8"]]
solution = Solution()
test = 4
import timeit

def toTime():
    if test == 1:
        return solution.solveSudoku(input1)
    if test == 2:
        return solution.solveSudoku(input2)
    if test == 3:
        return solution.solveSudoku(input3)
    if test == 4:
        return solution.solveSudoku(input4)

if test == 1:
    print(timeit.timeit(toTime, number=1))
    print('RESULTS 1 -----------------------------------', input1==output1)
    for r in input1:
        print(r)

if test == 2:
    print(timeit.timeit(toTime, number=1))
    print('RESULTS 2 -----------------------------------', input2==output2)
    for r in input2:
        print(r)

if test == 3:
    print(timeit.timeit(toTime, number=1))
    print('RESULTS 3 -----------------------------------', input3==output3)
    for r in input3:
        print(r)

if test == 4:
    print(timeit.timeit(toTime, number=1))
    print('RESULTS 4 -----------------------------------', input4==output4)
    for r in input4:
        print(r)