# sudoku-solver-algorithm

sudoku_algorithm contains an algorithm that simulates regular deduction to solve a sudoku. It can solve easy to intermediate sudoku puzzles.

sudoku_algorithm_2 implements an algorithm that combines guessing and using the basic rules of sudoku to reach one solution. This algorithm
can solve puzzles of all difficulties.

Both algorithms create a sudokuMatrix variable at the beginning of the program that contains the initial sudoku in the form of a list of lists
where every internal list represents a row of the sudoku puzzle. Each element within each row is a string. Empty squares are represented
with a ".". Each program prints the filled sudoku matrix after running.
