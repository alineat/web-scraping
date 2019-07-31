import xlrd

workbook = xlrd.open_workbook('9nome_do_arquivo_que_quero_criar.xlsx')
worksheet = workbook.sheet_by_index(0)
linhas = worksheet.nrows

for linha in range(linhas):
    first_col, second_col = worksheet.row_values(linha)
    print(first_col, '    ', second_col)
