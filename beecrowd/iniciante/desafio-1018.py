# Problema 1018 - Cédulas
# Fonte: https://judge.beecrowd.com/

# O problema pede para decompor um valor inteiro em cédulas de dinheiro
# (notas) nos valores: 100, 50, 20, 10, 5, 2 e 1.
# A saída deve mostrar primeiro o valor lido e depois quantas notas de cada
# valor são necessárias para compor esse número.

# Exemplo de entrada:
# 576
#
# Saída esperada:
# 576
# 5 nota(s) de R$ 100,00
# 1 nota(s) de R$ 50,00
# 1 nota(s) de R$ 20,00
# 0 nota(s) de R$ 10,00
# 1 nota(s) de R$ 5,00
# 0 nota(s) de R$ 2,00
# 1 nota(s) de R$ 1,00

# -----------------------------------------------------

# Lemos o valor inteiro informado pelo usuário
n = int(input())

# Lista com os valores das cédulas disponíveis
cedulas = [100, 50, 20, 10, 5, 2, 1]

# O primeiro valor impresso deve ser o número original
print(n)

# Para cada cédula, calculamos quantas cabem no valor atual de n
for c in cedulas:
    # Usamos divisão inteira (//) para saber quantas notas cabem
    quantidade = n // c

    # Exibimos a quantidade no formato exigido pelo problema
    print(f"{quantidade} nota(s) de R$ {c},00")

    # Atualizamos n para o resto da divisão, ou seja,
    # o valor que ainda falta decompor
    n = n % c
