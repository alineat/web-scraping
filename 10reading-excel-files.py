import xlrd     # import



# open workbook

workbook = xlrd.open_workbook('first-file.xlsx')



# get sheet - method - sheet_by_index(index parameter)

worksheet = workbook.sheet_by_index(0)


# find total no of rows - .nrows

rows = worksheet.nrows


# read rows - row_values(row number)

for row in range(rows):
    first_col,second_col = worksheet.row_values(row)
    print(first_col,'    ',second_col)
