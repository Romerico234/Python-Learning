def row_correct(sudoku: list, row_no: int):
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in check:
        if sudoku[row_no].count(i) >= 2:    
            return False    
    return True

def column_correct(sudoku: list, column_no: int):
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    col = []
    for row in sudoku:
        col.append(row[column_no])

    for i in check:
        if col.count(i) >= 2:
            return False   
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    new_list = []
    for row in range(row_no, row_no+3):
        for element in range(column_no, column_no+3):
            number = sudoku[row][element]
            if number > 0 and number in new_list:
                return False
            new_list.append(number)
    return True

def sudoku_grid_correct(sudoku: list):
    for row in range(0,9):
        if not row_correct(sudoku, row):
            return False
 
    for column in range(0,9):
        if not column_correct(sudoku, column):
            return False
 
    for row in range(0,9,3):
        for column in range(0,9,3):
            if not block_correct(sudoku, row, column):
                return False
    return True

def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        for k in range(len(sudoku[i])):
            if (k + 1) % 3 == 0 and sudoku[i][k] == 0:
                print("_  ", end="")
            elif k == len(sudoku[i]) - 1 and k != 0: #causes the some underscores to not be printed
                continue
            elif sudoku[i][k] != 0:
                print(f"{sudoku[i][k]} ", end="")
                if (k+1)%3 == 0:
                    print(" ",end="")
            else:
                print("_ ", end="")
        if (i + 1) % 3 == 0:
            print("\n")
        else:
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    for i in range(len(sudoku)):
        if i == row_no:
            sudoku[row_no].insert(column_no, number)
    return sudoku

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_copy = []
    for i in range(len(sudoku)):
        row_copy = []
        for k in range(len(sudoku[i])):
            if i == row_no and k == column_no:
                row_copy.append(number)
            else: 
                row_copy.append(sudoku[i][k])
        sudoku_copy.append(row_copy)
    return sudoku_copy
        

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]

    print(sudoku_grid_correct(sudoku))
    print_sudoku(sudoku)
    add_number(sudoku, 0, 5, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print_sudoku(sudoku)
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)            

