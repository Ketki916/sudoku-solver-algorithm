import copy

''' sudokuMatrix = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]] '''

''' sudokuMatrix = [[".","2",".","6",".","8",".",".","."],
["5","8",".",".",".","9","7",".","."],[".",".",".",".","4",".",".",".","."],
["3","7",".",".",".",".","5",".","."],["6",".",".",".",".",".",".",".","4"],
[".",".","8",".",".",".",".","1","3"],[".",".",".",".","2",".",".",".","."],
[".",".","9","8",".",".",".","3","6"],[".",".",".","3",".","6",".","9","."]]'''

''' sudokuMatrix = [[".",".",".","6",".",".","4",".","."], 
["7",".",".",".",".","3","6",".","."], [".",".",".",".","9","1",".","8","."],
[".",".",".",".",".",".",".",".","."], [".","5",".","1","8",".",".",".","3"],
[".",".",".","3",".","6",".","4","5"], [".","4",".","2",".",".",".","6","."],
["9",".","3",".",".",".",".",".","."], [".","2",".",".",".",".","1",".","."]]'''

''' sudokuMatrix = [[".","2",".",".",".",".",".",".","."], 
[".",".",".","6",".",".",".",".","3"], [".","7","4",".","8",".",".",".","."],
[".",".",".",".",".","3",".",".","2"], [".","8",".",".","4",".",".","1","."],
["6",".",".","5",".",".",".",".","."], [".",".",".",".","1",".","7","8","."],
["5",".",".",".",".","9",".",".","."], [".",".",".",".",".",".",".","4","."]]'''

sudokuMatrix = [["8",".",".",".",".",".",".",".","."], 
[".",".","3","6",".",".",".",".","."], [".","7",".",".","9",".","2",".","."],
[".","5",".",".",".","7",".",".","."], [".",".",".",".","4","5","7",".","."],
[".",".",".","1",".",".",".","3","."], [".",".","1",".",".",".",".","6","8"],
[".",".","8","5",".",".",".","1","."], [".","9",".",".",".",".","4",".","."]]



count = 0

for row in sudokuMatrix:
    for rowItem in row:
        if rowItem == ".":
            count = count + 1
            sudokuMatrix[sudokuMatrix.index(row)][row.index(rowItem)] = "123456789"


columnMatrix = [[], [], [], [], [], [], [], [], []]

for row in sudokuMatrix:
    columnMatrix[0].append(row[0])
    columnMatrix[1].append(row[1])
    columnMatrix[2].append(row[2])
    columnMatrix[3].append(row[3])
    columnMatrix[4].append(row[4])
    columnMatrix[5].append(row[5])
    columnMatrix[6].append(row[6])
    columnMatrix[7].append(row[7])
    columnMatrix[8].append(row[8])

gridMatrix = [[], [], [], [], [], [], [], [], []]

for row in sudokuMatrix:
    if sudokuMatrix.index(row) < 3:
        gridMatrix[0] = gridMatrix[0] + [row[0], row[1], row[2]]
        gridMatrix[1] = gridMatrix[1] + [row[3], row[4], row[5]]
        gridMatrix[2] = gridMatrix[2] + [row[6], row[7], row[8]]
    if sudokuMatrix.index(row) < 6 and sudokuMatrix.index(row) >= 3:
        gridMatrix[3] = gridMatrix[3] + [row[0], row[1], row[2]]
        gridMatrix[4] = gridMatrix[4] + [row[3], row[4], row[5]]
        gridMatrix[5] = gridMatrix[5] + [row[6], row[7], row[8]]
    if sudokuMatrix.index(row) < 9 and sudokuMatrix.index(row) >= 6:
        gridMatrix[6] = gridMatrix[6] + [row[0], row[1], row[2]]
        gridMatrix[7] = gridMatrix[7] + [row[3], row[4], row[5]]
        gridMatrix[8] = gridMatrix[8] + [row[6], row[7], row[8]]

def rowToGrid(rowNumber, rowItem):
    if (rowNumber == 0 or rowNumber == 1 or rowNumber == 2):
        if (rowItem == 0 or rowItem == 1 or rowItem == 2):
            gridNumber = 0
        if (rowItem == 3 or rowItem == 4 or rowItem == 5):
            gridNumber = 1
        if (rowItem == 6 or rowItem == 7 or rowItem == 8):
            gridNumber = 2
    if (rowNumber == 3 or rowNumber == 4 or rowNumber == 5):
        if (rowItem == 0 or rowItem == 1 or rowItem == 2):
            gridNumber = 3
        if (rowItem == 3 or rowItem == 4 or rowItem == 5):
            gridNumber = 4
        if (rowItem == 6 or rowItem == 7 or rowItem == 8):
            gridNumber = 5
    if (rowNumber == 6 or rowNumber == 7 or rowNumber == 8):
        if (rowItem == 0 or rowItem == 1 or rowItem == 2):
            gridNumber = 6
        if (rowItem == 3 or rowItem == 4 or rowItem == 5):
            gridNumber = 7
        if (rowItem == 6 or rowItem == 7 or rowItem == 8):
            gridNumber = 8
    
    column = (rowItem + 1) % 3
    row = (rowNumber + 1) % 3
    if column == 0:
        column = 3
    if row == 0:
        row = 3
    
    gridItem = (row - 1)*3 + column - 1

    return [gridNumber, gridItem]


def gridToRow(gridNumber, gridItem):
    if (gridNumber == 0 or gridNumber == 1 or gridNumber == 2):
        if (gridItem == 0 or gridItem == 1 or gridItem == 2):
            rowNumber = 0
        if (gridItem == 3 or gridItem == 4 or gridItem == 5):
            rowNumber = 1
        if (gridItem == 6 or gridItem == 7 or gridItem == 8):
            rowNumber = 2
    if (gridNumber == 3 or gridNumber == 4 or gridNumber == 5):
        if (gridItem == 0 or gridItem == 1 or gridItem == 2):
            rowNumber = 3
        if (gridItem == 3 or gridItem == 4 or gridItem == 5):
            rowNumber = 4
        if (gridItem == 6 or gridItem == 7 or gridItem == 8):
            rowNumber = 5
    if (gridNumber == 6 or gridNumber == 7 or gridNumber == 8):
        if (gridItem == 0 or gridItem == 1 or gridItem == 2):
            rowNumber = 6
        if (gridItem == 3 or gridItem == 4 or gridItem == 5):
            rowNumber = 7
        if (gridItem == 6 or gridItem == 7 or gridItem == 8):
            rowNumber = 8
    
    column = (gridItem + 1) % 3
    row = (gridNumber + 1) % 3
    if column == 0:
        column = 3
    if row == 0:
        row = 3
    
    rowItem = (row - 1)*3 + column - 1

    return [rowNumber, rowItem]

def columnToGrid(columnNumber, columnItem):
    if (columnNumber == 0 or columnNumber == 1 or columnNumber == 2):
        if (columnItem == 0 or columnItem == 1 or columnItem == 2):
            gridNumber = 0
        if (columnItem == 3 or columnItem == 4 or columnItem == 5):
            gridNumber = 3
        if (columnItem == 6 or columnItem == 7 or columnItem == 8):
            gridNumber = 6
    if (columnNumber == 3 or columnNumber == 4 or columnNumber == 5):
        if (columnItem == 0 or columnItem == 1 or columnItem == 2):
            gridNumber = 1
        if (columnItem == 3 or columnItem == 4 or columnItem == 5):
            gridNumber = 4
        if (columnItem == 6 or columnItem == 7 or columnItem == 8):
            gridNumber = 7
    if (columnNumber == 6 or columnNumber == 7 or columnNumber == 8):
        if (columnItem == 0 or columnItem == 1 or columnItem == 2):
            gridNumber = 2
        if (columnItem == 3 or columnItem == 4 or columnItem == 5):
            gridNumber = 5
        if (columnItem == 6 or columnItem == 7 or columnItem == 8):
            gridNumber = 8
    
    column = (columnNumber + 1) % 3
    row = (columnItem + 1) % 3
    if column == 0:
        column = 3
    if row == 0:
        row = 3
    
    gridItem = (row - 1)*3 + column - 1

    return [gridNumber, gridItem]


def gridToColumn(gridNumber, gridItem):
    if (gridNumber == 0 or gridNumber == 3 or gridNumber == 6):
        if (gridItem == 0 or gridItem == 3 or gridItem == 6):
            columnNumber = 0
        if (gridItem == 1 or gridItem == 4 or gridItem == 7):
            columnNumber = 1
        if (gridItem == 2 or gridItem == 5 or gridItem == 8):
            columnNumber = 2
    if (gridNumber == 1 or gridNumber == 4 or gridNumber == 7):
        if (gridItem == 0 or gridItem == 3 or gridItem == 6):
            columnNumber = 3
        if (gridItem == 1 or gridItem == 4 or gridItem == 7):
            columnNumber = 4
        if (gridItem == 2 or gridItem == 5 or gridItem == 8):
            columnNumber = 5
    if (gridNumber == 2 or gridNumber == 5 or gridNumber == 8):
        if (gridItem == 0 or gridItem == 3 or gridItem == 6):
            columnNumber = 6
        if (gridItem == 1 or gridItem == 4 or gridItem == 7):
            columnNumber = 7
        if (gridItem == 2 or gridItem == 5 or gridItem == 8):
            columnNumber = 8
 

    if gridNumber == 0 or gridNumber == 1 or gridNumber == 2:
        row = 0
    elif gridNumber == 3 or gridNumber == 4 or gridNumber == 5:
        row = 1
    else:
        row = 2

    if gridItem == 0 or gridItem == 1 or gridItem == 2:
        column = 1
    elif gridItem == 3 or gridItem == 4 or gridItem == 5:
        column = 2
    else:
        column = 3
    
    columnItem = (row)*3 + column - 1

    return [columnNumber, columnItem]

stop = False
changes = 0

while stop == False:

    originalChanges = changes

    for row in sudokuMatrix:
        removeNumbers = ""
        for rowItem in row:
            if len(rowItem) == 1:
                removeNumbers = removeNumbers + rowItem
        itemIndex = 0
        if len(removeNumbers) > 0:
            for rowItem in row:
                rowIndex = sudokuMatrix.index(row)
                if len(rowItem) > 1:
                    for digit in removeNumbers:
                        if digit in rowItem:
                            changes = changes + 1
                            newNumber = sudokuMatrix[rowIndex][itemIndex].replace(digit, "")
                            sudokuMatrix[rowIndex][itemIndex] = newNumber
                            columnMatrix[itemIndex][rowIndex] = newNumber
                            gridIndex = rowToGrid(rowIndex, itemIndex)
                            gridMatrix[gridIndex[0]][gridIndex[1]] = newNumber
                            if len(newNumber) == 1:
                                count = count - 1
                itemIndex = itemIndex + 1
    

    for column in columnMatrix:
        removeNumbers = ""
        for columnItem in column:
            if len(columnItem) == 1:
                removeNumbers = removeNumbers + columnItem
        itemIndex = 0
        if len(removeNumbers) > 0:
            for columnItem in column:
                columnIndex = columnMatrix.index(column)
                if len(columnItem) > 1:
                    for digit in removeNumbers:
                        if digit in columnItem:
                            changes = changes + 1
                            newNumber = columnMatrix[columnIndex][itemIndex].replace(digit, "")
                            columnMatrix[columnIndex][itemIndex] = newNumber
                            sudokuMatrix[itemIndex][columnIndex] = newNumber
                            gridIndex = columnToGrid(columnIndex, itemIndex)
                            gridMatrix[gridIndex[0]][gridIndex[1]] = newNumber
                            if len(newNumber) == 1:
                                count = count - 1
                itemIndex = itemIndex + 1

    
    for grid in gridMatrix:
        removeNumbers = ""
        for gridItem in grid:
            if len(gridItem) == 1:
                removeNumbers = removeNumbers + gridItem
        itemIndex = 0
        if len(removeNumbers) > 0:
            for gridItem in grid:
                gridIndex = gridMatrix.index(grid)
                if len(gridItem) > 1:
                    for digit in removeNumbers:
                        if digit in gridItem:
                            changes = changes + 1
                            newNumber = gridMatrix[gridIndex][itemIndex].replace(digit, "")
                            gridMatrix[gridIndex][itemIndex] = newNumber
                            rowIndex = gridToRow(gridIndex, itemIndex)
                            sudokuMatrix[rowIndex[0]][rowIndex[1]] = newNumber
                            columnIndex = gridToColumn(gridIndex, itemIndex)
                            columnMatrix[columnIndex[0]][columnIndex[1]] = newNumber
                            if len(newNumber) == 1:
                                count = count - 1
                itemIndex = itemIndex + 1
    
    if changes == originalChanges:
        stop = True


error = False
restart = False
firstIteration = True
guessedValues = []
possibleValues = []
guessedValuesIndices = []
number = 0
number2 = 0


while count > 0:

    if error == True and restart == True:
        guessedValues = []
        possibleValues = []
        guessedValuesIndices = []

    sudokuReplica = copy.deepcopy(sudokuMatrix)
    columnReplica = copy.deepcopy(columnMatrix)
    gridReplica = copy.deepcopy(gridMatrix)

    if (firstIteration == True) or (stop == True) or (error == True and restart == True):
        shouldBreak = False
        rowIndex = 0
        for row in sudokuReplica:
            rowItemIndex = 0
            for rowItem in row:
                if len(rowItem) > 1 and ([rowIndex, rowItemIndex] not in guessedValuesIndices):
                    possibleValues.append(rowItem)
                    guessedValues.append(rowItem[0])
                    guessedValuesIndices.append([rowIndex, rowItemIndex])
                    shouldBreak = True
                    break
                rowItemIndex = rowItemIndex + 1
            if shouldBreak == True:
                break
            rowIndex = rowIndex + 1


    for index in range(0, len(guessedValues)):
        sudokuReplica[guessedValuesIndices[index][0]][guessedValuesIndices[index][1]] = guessedValues[index]
        columnReplica[guessedValuesIndices[index][1]][guessedValuesIndices[index][0]] = guessedValues[index]
        gridIndex = rowToGrid(guessedValuesIndices[index][0], guessedValuesIndices[index][1])
        gridReplica[gridIndex[0]][gridIndex[1]] = guessedValues[index]


    error = False
    restart = False
    stop = False
    changes = 0
    temporaryCount = count - len(guessedValues)

    while (error == False and stop == False and temporaryCount > 0):

        originalChanges = changes

        shouldBreak = False
        for row in sudokuReplica:
            removeNumbers = ""
            for rowItem in row:
                if len(rowItem) == 1:
                    if rowItem in removeNumbers:
                        shouldBreak = True
                        error = True
                        break
                    removeNumbers = removeNumbers + rowItem
            if shouldBreak == True:
                break
            itemIndex = 0
            if len(removeNumbers) > 0:
                newSingleDigits = ""
                for rowItem in row:
                    rowIndex = sudokuReplica.index(row)
                    if len(rowItem) > 1:               
                        for digit in removeNumbers:
                            if digit in rowItem:
                                newNumber = sudokuReplica[rowIndex][itemIndex].replace(digit, "")
                                if newNumber == "" or (len(newNumber) == 1 and newNumber in newSingleDigits):
                                    shouldBreak = True
                                    error = True
                                    break   
                                changes = changes + 1   
                                sudokuReplica[rowIndex][itemIndex] = newNumber
                                columnReplica[itemIndex][rowIndex] = newNumber
                                gridIndex = rowToGrid(rowIndex, itemIndex)
                                gridReplica[gridIndex[0]][gridIndex[1]] = newNumber
                                if len(newNumber) == 1:
                                    newSingleDigits = newSingleDigits + newNumber
                                    temporaryCount = temporaryCount - 1
                    if shouldBreak == True:
                        break
                    itemIndex = itemIndex + 1
        

        if shouldBreak == True:
            break
    
        shouldBreak = False
        for column in columnReplica:
            removeNumbers = ""
            for columnItem in column:
                if len(columnItem) == 1:
                    if columnItem in removeNumbers:
                        shouldBreak = True
                        error = True
                        break
                    removeNumbers = removeNumbers + columnItem
            if shouldBreak == True:
                break
            itemIndex = 0
            if len(removeNumbers) > 0:
                newSingleDigits = ""
                for columnItem in column:
                    columnIndex = columnReplica.index(column)
                    if len(columnItem) > 1:
                        for digit in removeNumbers:
                            if digit in columnItem:
                                newNumber = columnReplica[columnIndex][itemIndex].replace(digit, "")
                                if newNumber == "" or (len(newNumber) == 1 and newNumber in newSingleDigits):
                                    shouldBreak = True
                                    error = True
                                    break 
                                changes = changes + 1
                                columnReplica[columnIndex][itemIndex] = newNumber
                                sudokuReplica[itemIndex][columnIndex] = newNumber
                                gridIndex = columnToGrid(columnIndex, itemIndex)  
                                gridReplica[gridIndex[0]][gridIndex[1]] = newNumber
                                if len(newNumber) == 1:
                                    temporaryCount = temporaryCount - 1
                    if shouldBreak == True:
                        break
                    itemIndex = itemIndex + 1


        if shouldBreak == True:
            break

        shouldBreak = False
        for grid in gridReplica:
            removeNumbers = ""
            for gridItem in grid:
                if len(gridItem) == 1:
                    if gridItem in removeNumbers:
                        shouldBreak = True
                        error = True
                        break
                    removeNumbers = removeNumbers + gridItem
            if shouldBreak == True:
                break
            itemIndex = 0
            if len(removeNumbers) > 0:
                newSingleDigits = ""
                for gridItem in grid:
                    gridIndex = gridReplica.index(grid)
                    if len(gridItem) > 1:               
                        for digit in removeNumbers:
                            if digit in gridItem:
                                newNumber = gridReplica[gridIndex][itemIndex].replace(digit, "")
                                if newNumber == "" or (len(newNumber) == 1 and newNumber in newSingleDigits):
                                    shouldBreak = True
                                    error = True
                                    break 
                                changes = changes + 1
                                gridReplica[gridIndex][itemIndex] = newNumber
                                rowIndex = gridToRow(gridIndex, itemIndex)
                                sudokuReplica[rowIndex[0]][rowIndex[1]] = newNumber
                                columnIndex = gridToColumn(gridIndex, itemIndex)
                                columnReplica[columnIndex[0]][columnIndex[1]] = newNumber
                                if len(newNumber) == 1:
                                    temporaryCount = temporaryCount - 1
                    if shouldBreak == True:
                        break
                    itemIndex = itemIndex + 1

        if shouldBreak == True:
            break
    
        if changes == originalChanges:
            stop = True
    
    
    if temporaryCount == 0:
        count = temporaryCount
        sudokuMatrix = copy.deepcopy(sudokuReplica)

    if stop == True:
        sudokuReplica = copy.deepcopy(sudokuMatrix)
        columnReplica = copy.deepcopy(columnMatrix)
        gridReplica = copy.deepcopy(gridMatrix)

    firstIteration = False

    if error == True:
        for i in range(len(possibleValues) - 1, -1, -1):
            if len(possibleValues[i]) > 1 and i != 0:
                possibleValues[i] = possibleValues[i].replace(guessedValues[i], "")
                guessedValues[i] = possibleValues[i][0]
                possibleValues = possibleValues[ : i+1]
                guessedValues = guessedValues[ : i+1]
                guessedValuesIndices = guessedValuesIndices[ : i+1]
                break
            elif len(possibleValues[i]) > 2 and i == 0:
                possibleValues[i] = possibleValues[i].replace(guessedValues[i], "")
                guessedValues[i] = possibleValues[i][0]
                possibleValues = possibleValues[ : i+1]
                guessedValues = guessedValues[ : i+1]
                guessedValuesIndices = guessedValuesIndices[ : i+1]
                break
            elif len(possibleValues) == 2 and i == 0:
                possibleValues[i] = possibleValues[i].replace(guessedValues[i], "")
                sudokuMatrix[guessedValuesIndices[i][0]][guessedValuesIndices[i][1]] = possibleValues[i]
                columnMatrix[guessedValuesIndices[i][1]][guessedValuesIndices[i][0]] = possibleValues[i]
                gridIndex = rowToGrid(guessedValuesIndices[i][0], guessedValuesIndices[i][1])
                gridMatrix[gridIndex[0]][gridIndex[1]] = possibleValues[i]
                count = count - 1
                restart = True


print(sudokuMatrix)
