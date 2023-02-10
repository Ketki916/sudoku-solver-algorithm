

'''sudokuMatrix = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'''

sudokuMatrix = [[".","2",".","6",".","8",".",".","."],
["5","8",".",".",".","9","7",".","."],[".",".",".",".","4",".",".",".","."],
["3","7",".",".",".",".","5",".","."],["6",".",".",".",".",".",".",".","4"],
[".",".","8",".",".",".",".","1","3"],[".",".",".",".","2",".",".",".","."],
[".",".","9","8",".",".",".","3","6"],[".",".",".","3",".","6",".","9","."]]

''' sudokuMatrix = [[".",".",".","6",".",".","4",".","."], 
["7",".",".",".",".","3","6",".","."], [".",".",".",".","9","1",".","8","."],
[".",".",".",".",".",".",".",".","."], [".","5",".","1","8",".",".",".","3"],
[".",".",".","3",".","6",".","4","5"], [".","4",".","2",".",".",".","6","."],
["9",".","3",".",".",".",".",".","."], [".","2",".",".",".",".","1",".","."]]'''

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


while count > 0 :

    for row in sudokuMatrix:
        removeNumbers = ""
        for rowItem in row:
            if len(rowItem) == 1:
                removeNumbers = removeNumbers + rowItem
        itemIndex = 0
        for rowItem in row:
            rowIndex = sudokuMatrix.index(row)
            if len(rowItem) > 1 and len(removeNumbers) > 0:
                for digit in removeNumbers:
                    if digit in rowItem:
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
        for columnItem in column:
            columnIndex = columnMatrix.index(column)
            if len(columnItem) > 1 and len(removeNumbers) > 0:
                for digit in removeNumbers:
                    if digit in columnItem:
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
        for gridItem in grid:
            gridIndex = gridMatrix.index(grid)
            if len(gridItem) > 1 and len(removeNumbers) > 0:
                for digit in removeNumbers:
                    if digit in gridItem:
                        newNumber = gridMatrix[gridIndex][itemIndex].replace(digit, "")
                        gridMatrix[gridIndex][itemIndex] = newNumber
                        rowIndex = gridToRow(gridIndex, itemIndex)
                        sudokuMatrix[rowIndex[0]][rowIndex[1]] = newNumber
                        columnIndex = gridToColumn(gridIndex, itemIndex)
                        columnMatrix[columnIndex[0]][columnIndex[1]] = newNumber
                        if len(newNumber) == 1:
                            count = count - 1
            itemIndex = itemIndex + 1

        
    for row in sudokuMatrix:
        referenceNumber = ""
        rowItemIndex = 0
        for rowItem in row:
            indexList = []
            if len(rowItem) > 1:
                referenceNumber = rowItem
                indexList.append(rowItemIndex)
                referenceIndex = -1
                for nextRowItem in row:
                    if nextRowItem == referenceNumber:
                        if row.index(nextRowItem, referenceIndex + 1) != indexList[0]:
                            indexList.append(row.index(nextRowItem, referenceIndex + 1))
                        referenceIndex = row.index(nextRowItem, referenceIndex + 1)
                if len(indexList) == len(referenceNumber):
                    itemIndex = 0
                    for thirdRowItem in row:
                        rowIndex = sudokuMatrix.index(row)
                        if row.index(thirdRowItem) not in indexList:
                            for digit in referenceNumber:
                                if digit in thirdRowItem:
                                    newNumber = sudokuMatrix[rowIndex][itemIndex].replace(digit, "")
                                    sudokuMatrix[rowIndex][itemIndex] = newNumber
                                    columnMatrix[itemIndex][rowIndex] = newNumber
                                    gridIndex = rowToGrid(rowIndex, itemIndex)
                                    gridMatrix[gridIndex[0]][gridIndex[1]] = newNumber
                                    if len(newNumber) == 1:
                                        count = count - 1
                        itemIndex = itemIndex + 1
            rowItemIndex = rowItemIndex + 1


    for column in columnMatrix:
        referenceNumber = ""
        columnItemIndex = 0
        for columnItem in column:
            indexList = []
            if len(columnItem) > 1:
                referenceNumber = columnItem
                indexList.append(columnItemIndex)
                referenceIndex = -1
                for nextColumnItem in column:
                    if nextColumnItem == referenceNumber:
                        if column.index(nextColumnItem, referenceIndex + 1) != indexList[0]:
                            indexList.append(column.index(nextColumnItem, referenceIndex + 1))
                        referenceIndex = column.index(nextColumnItem, referenceIndex + 1)
                if len(indexList) == len(referenceNumber):
                    itemIndex = 0
                    for thirdColumnItem in column:
                        columnIndex = columnMatrix.index(column)
                        if column.index(thirdColumnItem) not in indexList:
                            for digit in referenceNumber:
                                if digit in thirdColumnItem:
                                    newNumber = columnMatrix[columnIndex][itemIndex].replace(digit, "")
                                    columnMatrix[columnIndex][itemIndex] = newNumber
                                    sudokuMatrix[itemIndex][columnIndex] = newNumber
                                    gridIndex = columnToGrid(columnIndex, itemIndex)
                                    gridMatrix[gridIndex[0]][gridIndex[1]] = newNumber
                                    if len(newNumber) == 1:
                                        count = count - 1 
                        itemIndex = itemIndex + 1
            columnItemIndex = columnItemIndex + 1
        

    for grid in gridMatrix:
        referenceNumber = ""
        gridItemIndex = 0
        for gridItem in grid:
            indexList = []
            if len(gridItem) > 1:
                referenceNumber = gridItem
                indexList.append(gridItemIndex)
                referenceIndex = -1
                for nextGridItem in grid:
                    if nextGridItem == referenceNumber:
                        if grid.index(nextGridItem, referenceIndex + 1) != indexList[0]:
                            indexList.append(grid.index(nextGridItem, referenceIndex + 1))
                        referenceIndex = grid.index(nextGridItem, referenceIndex + 1)
                if len(indexList) == len(referenceNumber):
                    itemIndex = 0
                    for thirdGridItem in grid:
                        gridIndex = gridMatrix.index(grid)
                        if grid.index(thirdGridItem) not in indexList:
                            for digit in referenceNumber:
                                if digit in thirdGridItem:
                                    newNumber = gridMatrix[gridIndex][itemIndex].replace(digit, "")
                                    gridMatrix[gridIndex][itemIndex] = newNumber
                                    rowIndex = gridToRow(gridIndex, itemIndex)
                                    sudokuMatrix[rowIndex[0]][rowIndex[1]] = newNumber
                                    columnIndex = gridToColumn(gridIndex, itemIndex)
                                    columnMatrix[columnIndex[0]][columnIndex[1]] = newNumber
                                    if len(newNumber) == 1:
                                        count = count - 1
                        itemIndex = itemIndex + 1
            gridItemIndex = gridItemIndex + 1


    for grid in gridMatrix:
        for gridItemIndex in range(0, len(grid), 3):
            gridRow = "".join(grid[gridItemIndex: gridItemIndex + 3])
            restOfRow = ""
            [rowNumber, rowItem] = gridToRow(gridMatrix.index(grid), gridItemIndex)
            if rowItem == 0:
                restOfRow = "".join(sudokuMatrix[rowNumber][rowItem + 3:])
            elif rowItem == 6:
                restOfRow = "".join(sudokuMatrix[rowNumber][: rowItem])
            else:
                restOfRow =  "".join(sudokuMatrix[rowNumber][: rowItem]) + "".join(sudokuMatrix[rowNumber][rowItem + 3:])
            removeNumbers = ""
            for digit in range(0, 9):
                if (str(digit + 1) in gridRow) and (str(digit + 1) not in restOfRow):
                    removeNumbers = removeNumbers + str(digit + 1)
            itemIndex = 0
            for gridItem in grid:
                gridIndex = gridMatrix.index(grid)
                if len(gridItem) > 1 and len(removeNumbers) > 0:
                    for digit in removeNumbers:
                        if (digit in gridItem) and not (gridItemIndex <= itemIndex and itemIndex < gridItemIndex + 3):
                            newNumber = gridMatrix[gridIndex][itemIndex].replace(digit, "")
                            gridMatrix[gridIndex][itemIndex] = newNumber
                            rowIndex = gridToRow(gridIndex, itemIndex)
                            sudokuMatrix[rowIndex[0]][rowIndex[1]] = newNumber
                            columnIndex = gridToColumn(gridIndex, itemIndex)
                            columnMatrix[columnIndex[0]][columnIndex[1]] = newNumber
                            if len(newNumber) == 1:
                                count = count - 1
                itemIndex = itemIndex + 1
        

    for grid in gridMatrix:
        for gridItemIndex in range(0,3):
            gridColumn = grid[gridItemIndex] + grid[gridItemIndex + 3] + grid[gridItemIndex + 6]
            restOfColumn = ""
            [columnNumber, columnItem] = gridToColumn(gridMatrix.index(grid), gridItemIndex)
            if columnItem == 0:
                restOfColumn = "".join(columnMatrix[columnNumber][columnItem + 3:])
            elif columnItem == 6:
                restOfColumn = "".join(columnMatrix[columnNumber][: columnItem])
            else:
                restOfColumn =  "".join(columnMatrix[columnNumber][: columnItem]) + "".join(columnMatrix[columnNumber][columnItem + 3:])
            removeNumbers = ""
            for digit in range(0, 9):
                if (str(digit + 1) in gridColumn) and (str(digit + 1) not in restOfColumn):
                    removeNumbers = removeNumbers + str(digit + 1)
            itemIndex = 0
            for gridItem in grid:
                gridIndex = gridMatrix.index(grid)
                if len(gridItem) > 1 and len(removeNumbers) > 0:
                    for digit in removeNumbers:
                        if (digit in gridItem) and not (itemIndex == gridItemIndex or itemIndex == gridItemIndex + 3 or itemIndex == gridItemIndex + 6):
                            newNumber = gridMatrix[gridIndex][itemIndex].replace(digit, "")
                            gridMatrix[gridIndex][itemIndex] = newNumber
                            rowIndex = gridToRow(gridIndex, itemIndex)
                            sudokuMatrix[rowIndex[0]][rowIndex[1]] = newNumber
                            columnIndex = gridToColumn(gridIndex, itemIndex)
                            columnMatrix[columnIndex[0]][columnIndex[1]] = newNumber
                            if len(newNumber) == 1:
                                count = count - 1
                itemIndex = itemIndex + 1

    for grid in gridMatrix:
        referenceNumber = ""
        gridItemIndex = 0
        for gridItem in grid:
            indexList = []
            if len(gridItem) > 1:
                referenceNumber = gridItem
                counter = 1
                indexList.append(gridItemIndex)
                nextGridItemIndex = 0
                for nextGridItem in grid:
                    if len(nextGridItem) > 1 and gridItemIndex != nextGridItemIndex:
                        shouldInclude = True
                        for digit in nextGridItem:
                            if digit not in referenceNumber:
                                shouldInclude = False
                        if shouldInclude == True:
                            indexList.append(nextGridItemIndex)
                            counter = counter + 1
                    if counter == len(referenceNumber):
                        break
                    nextGridItemIndex = nextGridItemIndex + 1
                if counter == len(referenceNumber):
                    itemIndex = 0
                    for thirdGridItem in grid:
                        gridIndex = gridMatrix.index(grid)
                        if len(thirdGridItem) > 1:
                            for digit in referenceNumber:
                                if (digit in thirdGridItem) and (itemIndex not in indexList):
                                    newNumber = gridMatrix[gridIndex][itemIndex].replace(digit, "")
                                    gridMatrix[gridIndex][itemIndex] = newNumber
                                    rowIndex = gridToRow(gridIndex, itemIndex)
                                    sudokuMatrix[rowIndex[0]][rowIndex[1]] = newNumber
                                    columnIndex = gridToColumn(gridIndex, itemIndex)
                                    columnMatrix[columnIndex[0]][columnIndex[1]] = newNumber
                                    if len(newNumber) == 1:
                                        count = count - 1
                        itemIndex = itemIndex + 1
            gridItemIndex = gridItemIndex + 1

    
    for column in columnMatrix:
        referenceNumber = ""
        columnItemIndex = 0
        for columnItem in column:
            indexList = []
            if len(columnItem) > 1:
                referenceNumber = columnItem
                counter = 1
                indexList.append(columnItemIndex)
                nextColumnItemIndex = 0
                for nextColumnItem in column:
                    if len(nextColumnItem) > 1 and columnItemIndex != nextColumnItemIndex:
                        shouldInclude = True
                        for digit in nextColumnItem:
                            if digit not in referenceNumber:
                                shouldInclude = False
                        if shouldInclude == True:
                            indexList.append(nextColumnItemIndex)
                            counter = counter + 1
                    if counter == len(referenceNumber):
                        break
                    nextColumnItemIndex = nextColumnItemIndex + 1
                if counter == len(referenceNumber):
                    itemIndex = 0
                    for thirdColumnItem in column:
                        columnIndex = columnMatrix.index(column)
                        if len(thirdColumnItem) > 1:
                            for digit in referenceNumber:
                                if (digit in thirdColumnItem) and (itemIndex not in indexList):
                                    newNumber = columnMatrix[columnIndex][itemIndex].replace(digit, "")
                                    columnMatrix[columnIndex][itemIndex] = newNumber
                                    sudokuMatrix[itemIndex][columnIndex] = newNumber
                                    gridIndex = columnToGrid(columnIndex, itemIndex)
                                    gridMatrix[gridIndex[0]][gridIndex[1]] = newNumber
                                    if len(newNumber) == 1:
                                        count = count - 1
                        itemIndex = itemIndex + 1
            columnItemIndex = columnItemIndex + 1


    for row in sudokuMatrix:
        referenceNumber = ""
        rowItemIndex = 0
        for rowItem in row:
            indexList = []
            if len(rowItem) > 1:
                referenceNumber = rowItem
                counter = 1
                indexList.append(rowItemIndex)
                nextRowItemIndex = 0
                for nextRowItem in row:
                    if len(nextRowItem) > 1 and rowItemIndex != nextRowItemIndex:
                        shouldInclude = True
                        for digit in nextRowItem:
                            if digit not in referenceNumber:
                                shouldInclude = False
                        if shouldInclude == True:
                            indexList.append(nextRowItemIndex)
                            counter = counter + 1
                    if counter == len(referenceNumber):
                        break
                    nextRowItemIndex = nextRowItemIndex + 1
                if counter == len(referenceNumber):
                    itemIndex = 0
                    for thirdRowItem in row:
                        rowIndex = sudokuMatrix.index(row)
                        if len(thirdRowItem) > 1:
                            for digit in referenceNumber:
                                if (digit in thirdRowItem) and (itemIndex not in indexList):
                                    newNumber = sudokuMatrix[rowIndex][itemIndex].replace(digit, "")
                                    sudokuMatrix[rowIndex][itemIndex] = newNumber
                                    columnMatrix[itemIndex][rowIndex] = newNumber
                                    gridIndex = rowToGrid(rowIndex, itemIndex)
                                    gridMatrix[gridIndex[0]][gridIndex[1]] = newNumber
                                    if len(newNumber) == 1:
                                        count = count - 1
                        itemIndex = itemIndex + 1
            rowItemIndex = rowItemIndex + 1


    for row in sudokuMatrix:
        for digit in range(1,10):
            indexList = []
            rowItemIndex = 0
            for rowItem in row:
                if str(digit) in rowItem:
                    indexList.append(rowItemIndex)
                rowItemIndex = rowItemIndex + 1
            if len(indexList) == 1:
                if len(sudokuMatrix[sudokuMatrix.index(row)][indexList[0]]) > 1:
                    count = count - 1
                sudokuMatrix[sudokuMatrix.index(row)][indexList[0]] = str(digit)
                columnMatrix[indexList[0]][sudokuMatrix.index(row)] = str(digit)
                gridIndex = rowToGrid(sudokuMatrix.index(row), indexList[0])
                gridMatrix[gridIndex[0]][gridIndex[1]] = str(digit)
            else:
                rowItemIndex = 0
                mainRow = ""
                restOfRow = ""
                for rowItem in row:
                    if rowItemIndex in indexList:
                        mainRow = mainRow + rowItem
                    else:
                        restOfRow = restOfRow + rowItem
                    rowItemIndex = rowItemIndex + 1
                counter = 0
                matchedDigits = ""
                for nextDigit in range(1,10):
                    if (str(nextDigit) in mainRow) and (str(nextDigit) not in restOfRow):
                        matchedDigits = matchedDigits + str(nextDigit)
                        counter = counter + 1
                if counter == len(indexList):
                    for rowItemIndex in indexList:
                        rowIndex = sudokuMatrix.index(row)
                        for thirdDigit in range(0,10):
                            check = 0
                            if str(thirdDigit) not in matchedDigits:
                                if len(sudokuMatrix[rowIndex][rowItemIndex]) > 1:
                                    check = 1
                                newNumber = sudokuMatrix[rowIndex][rowItemIndex].replace(str(thirdDigit), "")
                                sudokuMatrix[rowIndex][rowItemIndex] = newNumber
                                columnMatrix[rowItemIndex][rowIndex] = newNumber
                                gridIndex = rowToGrid(rowIndex, rowItemIndex)
                                gridMatrix[gridIndex[0]][gridIndex[1]] = newNumber
                                if len(newNumber) == 1 and check == 1:
                                    count = count - 1

    for column in columnMatrix:
        for digit in range(1,10):
            indexList = []
            columnItemIndex = 0
            for columnItem in column:
                if str(digit) in columnItem:
                    indexList.append(columnItemIndex)
                columnItemIndex = columnItemIndex + 1
            if len(indexList) == 1:
                if len(columnMatrix[columnMatrix.index(column)][indexList[0]]) > 1:
                    count = count - 1
                columnMatrix[columnMatrix.index(column)][indexList[0]] = str(digit)
                sudokuMatrix[indexList[0]][columnMatrix.index(column)] = str(digit)
                gridIndex = columnToGrid(columnMatrix.index(column), indexList[0])
                gridMatrix[gridIndex[0]][gridIndex[1]] = str(digit)
            else:
                columnItemIndex = 0
                mainColumn = ""
                restOfColumn = ""
                for columnItem in column:
                    if columnItemIndex in indexList:
                        mainColumn = mainColumn + columnItem
                    else:
                        restOfColumn = restOfColumn + columnItem
                    columnItemIndex = columnItemIndex + 1
                counter = 0
                matchedDigits = ""
                for nextDigit in range(1,10):
                    if (str(nextDigit) in mainColumn) and (str(nextDigit) not in restOfColumn):
                        matchedDigits = matchedDigits + str(nextDigit)
                        counter = counter + 1
                if counter == len(indexList):
                    for columnItemIndex in indexList:
                        columnIndex = columnMatrix.index(column)
                        for thirdDigit in range(0,10):
                            check = 0
                            if str(thirdDigit) not in matchedDigits:
                                if len(columnMatrix[columnIndex][columnItemIndex]) > 1:
                                    check = 1
                                newNumber = columnMatrix[columnIndex][columnItemIndex].replace(str(thirdDigit), "")
                                columnMatrix[columnIndex][columnItemIndex] = newNumber
                                sudokuMatrix[columnItemIndex][columnIndex] = newNumber
                                gridIndex = columnToGrid(columnIndex, columnItemIndex)
                                gridMatrix[gridIndex[0]][gridIndex[1]] = newNumber
                                if len(newNumber) == 1 and check == 1:
                                    count = count - 1


    for grid in gridMatrix:
        for digit in range(1,10):
            indexList = []
            gridItemIndex = 0
            for gridItem in grid:
                if str(digit) in gridItem:
                    indexList.append(gridItemIndex)
                gridItemIndex = gridItemIndex + 1
            if len(indexList) == 1:
                if len(gridMatrix[gridMatrix.index(grid)][indexList[0]]) > 1:
                    count = count - 1
                gridMatrix[gridMatrix.index(grid)][indexList[0]] = str(digit)
                rowIndex = gridToRow(gridMatrix.index(grid), indexList[0])
                sudokuMatrix[rowIndex[0]][rowIndex[1]] = str(digit)
                columnIndex = gridToColumn(gridMatrix.index(grid), indexList[0])
                columnMatrix[columnIndex[0]][columnIndex[1]] = str(digit)
            else:
                gridItemIndex = 0
                mainGrid = ""
                restOfGrid = ""
                for gridItem in grid:
                    if gridItemIndex in indexList:
                        mainGrid = mainGrid + gridItem
                    else:
                        restOfGrid = restOfGrid + gridItem
                    gridItemIndex = gridItemIndex + 1
                counter = 0
                matchedDigits = ""
                for nextDigit in range(1,10):
                    if (str(nextDigit) in mainGrid) and (str(nextDigit) not in restOfGrid):
                        matchedDigits = matchedDigits + str(nextDigit)
                        counter = counter + 1
                if counter == len(indexList):
                    for gridItemIndex in indexList:
                        gridIndex = gridMatrix.index(grid)
                        for thirdDigit in range(0,10):
                            check = 0
                            if str(thirdDigit) not in matchedDigits:
                                if len(gridMatrix[gridIndex][gridItemIndex]) > 1:
                                    check = 1
                                newNumber = gridMatrix[gridIndex][gridItemIndex].replace(str(thirdDigit), "")
                                gridMatrix[gridIndex][gridItemIndex] = newNumber
                                rowIndex = gridToRow(gridIndex, gridItemIndex)
                                sudokuMatrix[rowIndex[0]][rowIndex[1]] = newNumber
                                columnIndex = gridToColumn(gridIndex, gridItemIndex)
                                columnMatrix[columnIndex[0]][columnIndex[1]] = newNumber
                                if len(newNumber) == 1 and check == 1:
                                    count = count - 1
                            

    


print(sudokuMatrix)


   
    

    
