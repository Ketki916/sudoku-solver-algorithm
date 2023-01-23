
# Don't forget to subtract one when using row/column/grid numbers/items as index
# Don't forget to decrease count every item becomes single digit

sudokuMatrix = [[".","2",".","6",".","8",".",".","."],
["5","8",".",".",".","9","7",".","."],[".",".",".",".","4",".",".",".","."],
["3","7",".",".",".",".","5",".","."],["6",".",".",".",".",".",".",".","4"],
[".",".","8",".",".",".",".","1","3"],[".",".",".",".","2",".",".",".","."],
[".",".","9","8",".",".",".","3","6"],[".",".",".","3",".","6",".","9","."]]

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


# number = 6
while count > 0 : # number > 0   number = number - 1

    for row in sudokuMatrix:
        removeNumbers = ""
        for rowItem in row:
            if len(rowItem) == 1:
                removeNumbers = removeNumbers + rowItem
        for rowItem in row:
            itemIndex = row.index(rowItem)
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
    
    

    for column in columnMatrix:
        removeNumbers = ""
        for columnItem in column:
            if len(columnItem) == 1:
                removeNumbers = removeNumbers + columnItem
        for columnItem in column:
            itemIndex = column.index(columnItem)
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

    
    for grid in gridMatrix:
        removeNumbers = ""
        for gridItem in grid:
            if len(gridItem) == 1:
                removeNumbers = removeNumbers + gridItem
        for gridItem in grid:
            itemIndex = grid.index(gridItem)
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
        
    for row in sudokuMatrix:
        referenceNumber = ""
        for rowItem in row:
            indexList = []
            if len(rowItem) > 1:
                referenceNumber = rowItem
                indexList.append(row.index(rowItem))
                referenceIndex = -1
                for nextRowItem in row:
                    if nextRowItem == referenceNumber:
                        if row.index(nextRowItem, referenceIndex + 1) != indexList[0]:
                            indexList.append(row.index(nextRowItem))
                        referenceIndex = row.index(nextRowItem, referenceIndex + 1)
                if len(indexList) == len(referenceNumber):
                    for thirdRowItem in row:
                        itemIndex = row.index(thirdRowItem)
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

    for column in columnMatrix:
        referenceNumber = ""
        for columnItem in column:
            indexList = []
            if len(columnItem) > 1:
                referenceNumber = columnItem
                indexList.append(column.index(columnItem))
                referenceIndex = -1
                for nextColumnItem in column:
                    if nextColumnItem == referenceNumber:
                        if column.index(nextColumnItem, referenceIndex + 1) != indexList[0]:
                            indexList.append(column.index(nextColumnItem))
                        referenceIndex = column.index(nextColumnItem, referenceIndex + 1)
                if len(indexList) == len(referenceNumber):
                    for thirdColumnItem in column:
                        itemIndex = column.index(thirdColumnItem)
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





    # number = number - 1

print(sudokuMatrix)
# print("hi")
# print(gridMatrix)
# print("hi")
# print(columnMatrix)
# print("hi")
print(count)


   
    

    
