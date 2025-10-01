# Problema 1012 - Área
# Fonte: https://judge.beecrowd.com/

# O problema pede para calcular diferentes áreas geométricas a partir de 3 valores:
# A, B e C. Fórmulas:
# TRIANGULO = (A * C) / 2
# CIRCULO = pi * C^2
# TRAPEZIO = ((A + B) * C) / 2
# QUADRADO = B^2
# RETANGULO = A * B

# -----------------------------------------------------

# Lemos os três valores A, B, C em ponto flutuante
A, B, C = map(float, input().split())

# Definimos o valor de pi conforme o enunciado
pi = 3.14159

# Calculamos cada área
triangulo = (A * C) / 2
circulo = pi * (C ** 2)
trapezio = ((A + B) * C) / 2
quadrado = B ** 2
retangulo = A * B

# Exibimos os resultados com 3 casas decimais
print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")
