
# Don't forget to subtract one when using row/column/grid numbers/items as index

sudokuMatrix = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

for row in sudokuMatrix:
    for rowItem in row:
        if rowItem == ".":
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
