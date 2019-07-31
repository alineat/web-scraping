from xlsxwriter import Workbook

workbook = Workbook('9nome_do_arquivo_que_quero_criar.xlsx')
worksheet = workbook.add_worksheet()

for linha in range(20):
    worksheet.write(linha, 0, 'Nº da linha')
    worksheet.write(linha, 1, linha)

workbook.close()
