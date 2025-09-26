# Problema 1007 - Diferença
# Fonte: https://judge.beecrowd.com/

# O problema pede para calcular a diferença entre o produto de A e B
# e o produto de C e D. Fórmula:
# DIFERENCA = (A * B) - (C * D)

# -----------------------------------------------------

# Lemos o valor inteiro A
A = int(input())

# Lemos o valor inteiro B
B = int(input())

# Lemos o valor inteiro C
C = int(input())

# Lemos o valor inteiro D
D = int(input())

# Calculamos a diferença conforme a fórmula
DIFERENCA = (A * B) - (C * D)

# Exibimos o resultado no formato pedido
print(f"DIFERENCA = {DIFERENCA}")
