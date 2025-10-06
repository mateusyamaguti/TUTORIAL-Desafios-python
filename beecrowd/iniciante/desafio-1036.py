# Problema 1036 - Fórmula de Bhaskara
# Fonte: https://judge.beecrowd.com/

# O problema pede para calcular as raízes da equação do 2º grau:
# Ax^2 + Bx + C = 0
#
# Fórmula de Bhaskara:
# R1 = (-B + sqrt(delta)) / (2*A)
# R2 = (-B - sqrt(delta)) / (2*A)
#
# delta = B^2 - 4*A*C
#
# Casos especiais:
# - Se A == 0 (não é equação quadrática), não dá para dividir por 2A.
# - Se delta < 0, a raiz quadrada não é real.
# Nesse caso, devemos imprimir "Impossivel calcular".


# Solução 1
# -----------------------------------------------------

import math  # para usar sqrt (raiz quadrada)

# Lemos os três coeficientes
A, B, C = map(float, input().split())

# Calculamos o discriminante (delta)
delta = B**2 - 4*A*C

# Verificamos se é possível calcular as raízes
if A == 0 or delta < 0:
    print("Impossivel calcular")
else:
    R1 = (-B + math.sqrt(delta)) / (2*A)
    R2 = (-B - math.sqrt(delta)) / (2*A)
    
    # Exibimos os resultados com 5 casas decimais
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")



# Solução 2
# -----------------------------------------------------

# Ler os 3 coeficientes
a, b, c = map(float, input().split())

# Calcular delta
delta = (b**2) - (4*a) * c

# Verificar condição se é possível calcular as raízes
if (a == 0) or (delta < 0):
    print("Impossivel calcular")
else:
    r1 = (-b + (delta**0.5))/ (2 * a)
    r2 = (-b - (delta**0.5))/ (2 * a)

    # Exibir resultado
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")