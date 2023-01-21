
entrada = int(input())
horas = entrada // 3600
entrada = entrada - horas * 3600

minutos = entrada // 60
entrada = entrada - minutos*60
segundos = entrada % 60

print(f'{horas}:{minutos}:{segundos}')




