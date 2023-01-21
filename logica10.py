litros_km = 12

tempo_horas = int(input())
velocidade = int(input())

distancia = tempo_horas*velocidade

litros_necessarios = distancia/litros_km

print(f'{litros_necessarios:.3f}')