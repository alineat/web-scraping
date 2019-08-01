import xlrd

workbook = xlrd.open_workbook('9.nome_do_arquivo_que_quero_criar.xlsx')
worksheet = workbook.sheet_by_index(0)
linhas = worksheet.nrows

for linha in range(linhas):
    primeira_col, segunda_col = worksheet.row_values(linha)
    print(primeira_col, '    ', segunda_col)
