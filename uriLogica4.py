

def multi(qtdIten, valorinten):
    
    return qtdIten*valorinten

valores = input().split(' ')
valores2 = input().split(' ')
# vai efetuar a multiplicação dos valores e vai retorna o resultado
print(multi(int(valores[1]),float(valores[2])))
cal = multi(int(valores2[1]),float(valores2[2]))
# vai soamr o resultado da multiplicação anterior
soma = cal + multi(int(valores[1]),float(valores[2]))
print(f'VALOR A PAGAR: R$ {soma:.2f}')