input1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
output1 = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
input2 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
output2 = [["5","1","9","7","4","8","6","3","2"],["7","8","3","6","5","2","4","1","9"],["4","2","6","1","3","9","8","7","5"],["3","5","7","9","8","6","2","4","1"],["2","6","4","3","1","7","5","9","8"],["1","9","8","5","2","4","3","6","7"],["9","7","5","8","6","3","1","2","4"],["8","3","2","4","9","1","7","5","6"],["6","4","1","2","7","5","9","8","3"]]
input3 = [[".",".",".","2",".",".",".","6","3"],["3",".",".",".",".","5","4",".","1"],[".",".","1",".",".","3","9","8","."],[".",".",".",".",".",".",".","9","."],[".",".",".","5","3","8",".",".","."],[".","3",".",".",".",".",".",".","."],[".","2","6","3",".",".","5",".","."],["5",".","3","7",".",".",".",".","8"],["4","7",".",".",".","1",".",".","."]]
output3 = [["8","5","4","2","1","9","7","6","3"],["3","9","7","8","6","5","4","2","1"],["2","6","1","4","7","3","9","8","5"],["7","8","5","1","2","6","3","9","4"],["6","4","9","5","3","8","1","7","2"],["1","3","2","9","4","7","8","5","6"],["9","2","6","3","8","4","5","1","7"],["5","1","3","7","9","2","6","4","8"],["4","7","8","6","5","1","2","3","9"]]

class Solution:
    allOptions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self):
        self.toSolve = 9 * 9
        self.options = []
        for r in range(9):
            self.options.append([])
            for c in range(9):
                self.options[r].append([])

    def solveSudoku(self, board):
        self.initializeSudoku(board)
        iteration = 0
        while self.toSolve > 0:
            iteration += 1
            if self.easyCheck(board):
                continue
            if self.intermediateCheck(board):
                continue
            # self.complexCheck(board)
            print (iteration)
            if iteration >= 20:
                break

    def removeOptions(self, toRemove, optionsList):
        removed = 0
        for remove in toRemove:
            for item in optionsList:
                for spot in item:
                    if spot.count(remove) > 0:
                        spot.remove(remove)
                        removed += 1
        return removed

    def nakedSingle(self, board):
        for r in range(9):
            for c in range(9):
                if self.options[r][c] != '.' and len(self.options[r][c]) == 1:
                    board[r][c] = self.options[r][c][0]
                    self.toSolve -= 1
                    self.removeOptions(self.options[r][c], [self.getRow(r, self.options), self.getCol(c, self.options), self.getSqr(r, c, self.options)])
                    self.options[r][c] = '.'
                    print('naked single', (r, c))
                    return True
        return False

    def hiddenSingle(self, board):
        for r in range(9):
            for c in range(9):
                if self.options[r][c] != '.':
                    rowOptions = self.getRow(r, self.options)
                    colOptions = self.getCol(c, self.options)
                    sqrOptions = self.getSqr(r, c, self.options)
                    flatRowOptions = [item for sublist in rowOptions for item in sublist]
                    flatColOptions = [item for sublist in colOptions for item in sublist]
                    flatSqrOptions = [item for sublist in sqrOptions for item in sublist]
                    for option in self.options[r][c]:
                        if option != '.' and (flatRowOptions.count(option) == 1 or flatColOptions.count(option) == 1 or flatSqrOptions.count(option) == 1):
                            board[r][c] = option
                            self.toSolve -= 1
                            self.removeOptions([option], [rowOptions, colOptions, sqrOptions])
                            self.options[r][c] = '.'
                            print('hidden single', (r, c))
                            return True
        return False

    def pointingPair(self, board):
        removed = 0
        for i in range(9):
            rowOptions = self.getRow(i, self.options)
            colOptions = self.getCol(i, self.options)
            valid, index1, index2, value, sqr = self.checkForPointingBar(i, -1, rowOptions)
            if valid:
                for index in range(9):
                    if int(index / 3) != i % 3:
                        if sqr[index].count(value) > 0:
                            sqr[index].remove(value)
                            removed += 1
                if removed > 0:
                    print('pointing pair row')
                    return True
            valid, index1, index2, value, sqr = self.checkForPointingBar(-1, i, colOptions)
            if valid:
                for index in range(9):
                    if index % 3 != i % 3:
                        if sqr[index].count(value) > 0:
                            sqr[index].remove(value)
                            removed += 1
                if removed > 0:
                    print('pointing pair col')
                    return True
        return False
    
    def checkForPointingBar(self, row, col, optionList):
        if col == -1:
            sqr1, sqr2, sqr3 = self.getSqr(row, 0, self.options), self.getSqr(row, 3, self.options), self.getSqr(row, 6, self.options)
            flatSqr1, flatSqr2, flatSqr3 = [item for sublist in sqr1 for item in sublist], [item for sublist in sqr2 for item in sublist], [item for sublist in sqr3 for item in sublist]
            flatRowInSqr1, flatRowInSqr2, flatRowInSqr3 = [item for sublist in optionList[0:3] for item in sublist], [item for sublist in optionList[3:6] for item in sublist], [item for sublist in optionList[6:9] for item in sublist]
            for option in self.allOptions:
                if flatSqr1.count(option) == 2 and flatRowInSqr1.count(option) == 2:
                    index = -1
                    for i in range(0, 3):
                        if optionList[i].count(option) > 0:
                            if index == -1:
                                index = i
                            else:
                                return True, index, i, option, sqr1
                if flatSqr2.count(option) == 2 and flatRowInSqr2.count(option) == 2:
                    index = -1
                    for i in range(3, 6):
                        if optionList[i].count(option) > 0:
                            if index == -1:
                                index = i
                            else:
                                return True, index, i, option, sqr2
                if flatSqr3.count(option) == 2 and flatRowInSqr3.count(option) == 2:
                    index = -1
                    for i in range(6, 9):
                        if optionList[i].count(option) > 0:
                            if index == -1:
                                index = i
                            else:
                                return True, index, i, option, sqr3
        if row == -1:
            sqr1, sqr2, sqr3 = self.getSqr(0, col, self.options), self.getSqr(3, col, self.options), self.getSqr(6, col, self.options)
            flatSqr1, flatSqr2, flatSqr3 = [item for sublist in sqr1 for item in sublist], [item for sublist in sqr2 for item in sublist], [item for sublist in sqr3 for item in sublist]
            flatColInSqr1, flatColInSqr2, flatColInSqr3 = [item for sublist in optionList[0:3] for item in sublist], [item for sublist in optionList[3:6] for item in sublist], [item for sublist in optionList[6:9] for item in sublist]
            for option in self.allOptions:
                if flatSqr1.count(option) == 2 and flatColInSqr1.count(option) == 2:
                    index = -1
                    for i in range(0, 3):
                        if optionList[i].count(option) > 0:
                            if index == -1:
                                index = i
                            else:
                                return True, index, i, option, sqr1
                if flatSqr2.count(option) == 2 and flatColInSqr2.count(option) == 2:
                    index = -1
                    for i in range(3, 6):
                        if optionList[i].count(option) > 0:
                            if index == -1:
                                index = i
                            else:
                                return True, index, i, option, sqr2
                if flatSqr3.count(option) == 2 and flatColInSqr3.count(option) == 2:
                    index = -1
                    for i in range(6, 9):
                        if optionList[i].count(option) > 0:
                            if index == -1:
                                index = i
                            else:
                                return True, index, i, option, sqr3
        # TODO SQUARE CHECK
        return False, -1, -1, '.', ''

    def nakedPair(self, board):
        found = False
        for i in range(9):
            rowOptions = self.getRow(i, self.options)
            colOptions = self.getCol(i, self.options)
            for index in range(9):
                if rowOptions[index] != '.' and rowOptions.count(rowOptions[index] == 2):
                    index2 = rowOptions.index(rowOptions[index], 1)
                    sqrOptions1 = self.getSqr(i, index, self.options)
                    sqrOptionsExcludingRow1 = [o for i,o in enumerate(sqrOptions1) if i not in [index, (index + 3) % 9, (index + 6) % 9]]
                    sqrOptionsExcludingRow2 = []
                    if int(index / 3) != int(index2 / 3):
                        sqrOptions2 = self.getSqr(i, index2, self.options)
                        sqrOptionsExcludingRow2 = [o for i,o in enumerate(sqrOptions2) if i not in [index2, (index2 + 3) % 9, (index2 + 6) % 9]]
                    self.removeOptions(rowOptions[index], [sqrOptionsExcludingRow1, sqrOptionsExcludingRow2])
                    found = True
                if colOptions[index] != '.' and colOptions.count(colOptions[index] == 2):
                    index2 = colOptions.index(colOptions[index], 1)
                    sqrOptions1 = self.getSqr(index, i, self.options)
                    sqrOptionsExcludingCol1 = [o for i,o in enumerate(sqrOptions1) if i not in [index, (index + 3) % 9, (index + 6) % 9]]
                    sqrOptionsExcludingCol2 = []
                    if int(index / 3) != int(index2 / 3):
                        sqrOptions2 = self.getSqr(index2, i, self.options)
                        sqrOptionsExcludingCol2 = [o for i,o in enumerate(sqrOptions2) if i not in [index2, (index2 + 3) % 9, (index2 + 6) % 9]]
                    self.removeOptions(colOptions[index], [sqrOptionsExcludingCol1, sqrOptionsExcludingCol2])
                    found = True
        return found

    def hiddenPair(self, board):
        for i in range(9):
            rowOptions = self.getRow(i, self.options)
            colOptions = self.getCol(i, self.options)
            foundPairInRow, pairIndex1, pairIndex2, value1, value2 = self.checkForHiddenPair(rowOptions)
            if foundPairInRow:
                while len(rowOptions[pairIndex1]) > 0:
                    rowOptions[pairIndex1].pop()
                while len(rowOptions[pairIndex2]) > 0:
                    rowOptions[pairIndex2].pop()
                rowOptions[pairIndex1].append(value1)
                rowOptions[pairIndex1].append(value2)
                rowOptions[pairIndex2].append(value1)
                rowOptions[pairIndex2].append(value2)
                print('hidden row pair')
                return True 
            foundPairInCol, pairIndex1, pairIndex2, value1, value2 = self.checkForHiddenPair(colOptions)
            if foundPairInCol:
                while len(colOptions[pairIndex1]) > 0:
                    colOptions[pairIndex1].pop()
                while len(colOptions[pairIndex2]) > 0:
                    colOptions[pairIndex2].pop()
                colOptions[pairIndex1].append(value1)
                colOptions[pairIndex1].append(value2)
                colOptions[pairIndex2].append(value1)
                colOptions[pairIndex2].append(value2)
                print('hidden col pair')
                return True  
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                sqrOptions = self.getSqr(r, c, self.options)
                foundPairInSquare, pairIndex1, pairIndex2, value1, value2 = self.checkForHiddenPair(sqrOptions)
                if foundPairInSquare:
                    while len(sqrOptions[pairIndex1]) > 0:
                        sqrOptions[pairIndex1].pop()
                    while len(sqrOptions[pairIndex2]) > 0:
                        sqrOptions[pairIndex2].pop()
                    sqrOptions[pairIndex1].append(value1)
                    sqrOptions[pairIndex1].append(value2)
                    sqrOptions[pairIndex2].append(value1)
                    sqrOptions[pairIndex2].append(value2)
                    print('hidden sqr pair')
                    return True   
        return False
    
    def checkForHiddenPair(self, optionList):
        flatOptions = [item for sublist in optionList for item in sublist]
        allOptionsOccurrence = []
        for option in self.allOptions:
            allOptionsOccurrence.append(flatOptions.count(option))
        for index1 in range(9):
            if allOptionsOccurrence[index1] == 2:
                option1 = self.allOptions[index1]
                for index2 in range(index1 + 1, 9):
                    if allOptionsOccurrence[index2] == 2:
                        option2 = self.allOptions[index2]
                        index1InList, index2InList = -1, -1
                        for i in range(9):
                            if optionList[i].count(option1) > 0 and optionList[i].count(option2) > 0:
                                if index1InList == -1:
                                    index1InList = i
                                elif len(optionList[i]) > 2 or len(optionList[index1InList]) > 2:
                                    index2InList = i
                        if index1InList != -1 and index2InList != -1:
                            return True, index1InList, index2InList, option1, option2
        return False, -1, -1, -1, -1

    def swordFish(self, board):
        for r1 in range(9):
            rowOptions1 = self.getRow(r1, self.options)
            flatRow1 = [item for sublist in rowOptions1 for item in sublist]
            for option in self.allOptions:
                if flatRow1.count(option) == 3:
                    index1 = self.getSwordFishIndex(option, rowOptions1)
                    for r2 in range(9):
                        if r2 != r1:
                            rowOptions2 = self.getRow(r2, self.options)
                            flatRow2 = [item for sublist in rowOptions2 for item in sublist]
                            if flatRow2.count(option) >= 2 and flatRow2.count(option) <= 3: # not sure if its 2-3 or 1-3 for valid swordfish
                                index2 = self.getSwordFishIndex(option, rowOptions2, index1)
                                if index1 == index2:
                                    for r3 in range(9):
                                        if r3 != r1 and r3 != r2:
                                            rowOptions3 = self.getRow(r3, self.options)
                                            flatRow3 = [item for sublist in rowOptions3 for item in sublist]
                                            if flatRow3.count(option) >= 2 and flatRow3.count(option) <= 3: # not sure if its 2-3 or 1-3 for valid swordfish
                                                index3 = self.getSwordFishIndex(option, rowOptions3, index2)
                                                if index1 == index3:
                                                    col1, col2, col3 = self.getCol(index1[0], self.options), self.getCol(index1[1], self.options), self.getCol(index1[2], self.options)
                                                    removed = 0
                                                    for row in range(9):
                                                        if row not in [r1, r2, r3]:
                                                            if col1[row].count(option) > 0:
                                                                col1[row].remove(option)
                                                                removed += 1
                                                            if col2[row].count(option) > 0:
                                                                col2[row].remove(option)
                                                                removed += 1
                                                            if col3[row].count(option) > 0:
                                                                col3[row].remove(option)
                                                                removed +=1
                                                    if removed > 0:
                                                        print('sword fish')
                                                        return True
        return False

    def getSwordFishIndex(self, option, optionList, priorIndex=[]):
        indexList = []
        for index in range(9):
            if optionList[index].count(option) > 0 or (index in priorIndex and optionList[index] == '.'):
                indexList.append(index)
        return indexList                   

    def easyCheck(self, board):
        return self.nakedSingle(board) or self.hiddenSingle(board)

    def intermediateCheck(self, board):
        return self.nakedPair(board) or self.hiddenPair(board) or self.swordFish(board) or self.pointingPair(board) # self.pointingTriple(board)

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
test = 3

if test == 1:
    solution.solveSudoku(input1)
    print('RESULTS 1 -----------------------------------', input1==output1)
    for r in input1:
        print(r)
    print()
    for r in solution.options:
        print(r)

if test == 2:
    solution.solveSudoku(input2)
    print('RESULTS 2 -----------------------------------', input2==output2)
    for r in input2:
        print(r)
    print()
    for r in solution.options:
        print(r)

if test == 3:
    solution.solveSudoku(input3)
    print('RESULTS 3 -----------------------------------', input3==output3)
    for r in input3:
        print(r)
    print()
    for r in solution.options:
        print(r)