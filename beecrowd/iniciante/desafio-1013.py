# Problema 1013 - O Maior
# Fonte: https://judge.beecrowd.com/

# O problema pede para descobrir qual é o maior de três valores inteiros.
# Podemos resolver usando uma fórmula matemática que retorna o maior de dois números:
#
# MaiorAB = (a + b + |a - b|) / 2
#
# Essa fórmula funciona porque:
# - Se a > b, então |a - b| = a - b → (a + b + (a - b)) / 2 = (2a) / 2 = a
# - Se b > a, então |a - b| = b - a → (a + b + (b - a)) / 2 = (2b) / 2 = b
#
# Assim, ela retorna o maior entre a e b.
# Depois, podemos aplicar novamente para comparar o resultado com c.

# -----------------------------------------------------

# Lemos três valores inteiros em uma única linha
a, b, c = map(int, input().split())

# Calculamos o maior entre a e b
maior_ab = (a + b + abs(a - b)) // 2

# Calculamos o maior entre (maior_ab) e c
maior = (maior_ab + c + abs(maior_ab - c)) // 2

# Exibimos o resultado no formato exigido
print(f"{maior} eh o maior")
