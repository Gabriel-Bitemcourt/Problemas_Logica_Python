
dias = int(input())

anos = int(dias/365)
dias %= 365

mes = int(dias/30)
dias %= 30

print(f'{anos} ano(s)')
print(f'{mes} mes(es)')
print(f'{dias} dia(s)')

