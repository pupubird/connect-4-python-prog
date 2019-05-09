win = False
choice = [
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', 'O', 'O'],
    [' ', ' ', ' ', ' ', 'X', 'X'],
    [' ', ' ', ' ', ' ', 'X', 'O'],
    [' ', ' ', 'X', 'O', 'O', 'O'],
    [' ', ' ', ' ', 'X', 'O', 'X'],
    [' ', ' ', ' ', ' ', 'X', 'X'],
    [' ', ' ', 'X', 'X', 'X', 'X'],
    [' ', ' ', ' ', ' ', 'X', 'O']
]

# check for winning conditon of every column
# initialize last symbol and connect_amount
connect_col_amount = 1
previous_col_symbol = " "
for column in choice:
    # if last symbol = current row symbol, means they are the same, connect_amount +1
    for row_symbol in column:
        if row_symbol == previous_col_symbol:
            connect_col_amount += 1
        else:
            previous_col_symbol = row_symbol
            connect_col_amount = 1
    if connect_col_amount == 4 and previous_col_symbol != " ":
        win = True
    else:
        win = False
    print(win)
