# Problema 1037 - Intervalo
# Fonte: https://judge.beecrowd.com/

# O problema pede para identificar em qual dos intervalos o número N se encontra:
# [0,25], (25,50], (50,75], (75,100]
# Caso o número não pertença a nenhum desses intervalos, imprimir "Fora de intervalo".


# Solução 1
# -----------------------------------------------------

# Lemos o valor real
N = float(input())

# Verificamos em qual intervalo o número se encontra
if 0 <= N <= 25:
    print("Intervalo [0,25]")
elif 25 < N <= 50:
    print("Intervalo (25,50]")
elif 50 < N <= 75:
    print("Intervalo (50,75]")
elif 75 < N <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")

# Solução 2
# -----------------------------------------------------

# Ler o valor real
num = float(input("Número: "))

# Condição extrema
if (num >= 0) and (num <= 100):

    # Demais condições
    if num <= 25:
        print("Intervalo [0,25]")
    elif num <= 50:
        print("Intervalo (25,50]")
    elif num <= 75:
        print("Intervalo (50,75]")
    else:
        print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
