codigo,quantidade = list(map(int,input().split()))

if codigo == 1:
    preço = (float) (4.00 * quantidade)

elif codigo == 2:
    preço = (float) (4.50 * quantidade)

elif  codigo == 3:
    preço = (float) (5.00 * quantidade)

elif codigo == 4:
    preço = (float) (2.00 * quantidade)

elif codigo == 5:
    preço = (float) (1.50 * quantidade)

print(f'Total: R$ {preço:.2f}')



