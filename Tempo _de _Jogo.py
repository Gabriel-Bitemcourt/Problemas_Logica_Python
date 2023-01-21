a,b = list(map(int, input().split()))


if a<b:
    tempo = b -a
else:
    tempo = b + 24 - a
print(f"O JOGO DUROU {tempo} HORA(S)")