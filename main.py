import random

# Solicita a quantidade de jogadores
n = int(input("✿ Quantidade de jogadores: "))

# Cria uma lista com os jogadores
jogadores = []
for i in range(n):
    jogador = input(f"\nNome do jogador {i+1}: ")
    jogadores.append(jogador)

# Distribui os jogadores aleatoriamente em dois times
random.shuffle(jogadores)
time1 = jogadores[:n//2]
time2 = jogadores[n//2:]

# Imprime os times
print("✿ Time 1:")
for jogador in time1:
    print(jogador)

print("\nTime 2:")
for jogador in time2:
    print(jogador)
