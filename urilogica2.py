nomeFuncionario = str(input('')).upper()
salariofuncionario = float(input(''))
totalvendas = float(input(''))
totalcomissão = (totalvendas/100*15+salariofuncionario)
print(F'TOTAL = {totalcomissão:.2f}')