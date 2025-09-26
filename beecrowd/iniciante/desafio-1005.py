# Problema 1005 - Média 1
# Fonte: https://judge.beecrowd.com/

# O problema pede para calcular a média ponderada de dois números
# reais A e B, com os seguintes pesos:
# A -> 3.5
# B -> 7.5
# O resultado deve ser mostrado com 5 casas decimais.

# -----------------------------------------------------

# Lemos o primeiro valor (número real)
A = float(input())

# Lemos o segundo valor (número real)
B = float(input())

# Definimos os pesos
peso_A = 3.5
peso_B = 7.5

# Calculamos a média ponderada:
# (valor1*peso1 + valor2*peso2) / (peso1 + peso2)
MEDIA = (A * peso_A + B * peso_B) / (peso_A + peso_B)

# Exibimos o resultado com 5 casas decimais
# Usamos :.5f para forçar exatamente 5 dígitos após o ponto
print(f"MEDIA = {MEDIA:.5f}")
