# Problema 1021 - Notas e Moedas
# Fonte: https://judge.beecrowd.com/

# Lemos o valor e transformamos em centavos (inteiro)
valor = float(input())
centavos = int(round(valor * 100))

# Listas de notas e moedas em centavos
notas = [10000, 5000, 2000, 1000, 500, 200]   # notas em centavos
moedas = [100, 50, 25, 10, 5, 1]              # moedas em centavos

print("NOTAS:")
for nota in notas:
    qtd = centavos // nota
    print(f"{qtd} nota(s) de R$ {nota/100:.2f}")
    centavos %= nota

print("MOEDAS:")
for moeda in moedas:
    qtd = centavos // moeda
    print(f"{qtd} moeda(s) de R$ {moeda/100:.2f}")
    centavos %= moeda