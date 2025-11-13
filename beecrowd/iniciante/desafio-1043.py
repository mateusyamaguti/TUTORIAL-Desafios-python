# Problema 1043 - Triângulo
# Fonte: https://judge.beecrowd.com/

# O programa lê três valores reais e verifica se podem formar um triângulo.
# Caso possam, calcula o perímetro. Caso contrário, calcula a área de um trapézio.

# -----------------------------------------------------

# Leitura das variáveis reais de entrada
a, b, c = map(float, input().split())

# Condição de existência de um triângulo
# a + b > c, a + c > b, b + c > a.

if (a + b > c) and (a + c > b) and (b + c > a):
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((a + b) * c) / 2
    print(f"Area = {area}")
