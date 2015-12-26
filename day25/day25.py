
ROW = 2947
COLUMN = 3029

iteration = 1
row = 1
col = 1
code = 20151125

def calc_next(code):
    newcode = code * 252533
    newcode = newcode % 33554393
    return newcode 

while True:
    # + col, - row
    col += 1
    row -= 1
    if row == 0:
        iteration += 1
        col = 1
        row = iteration
    code = calc_next(code)
    if col == COLUMN and row == ROW:
        print code
        break
