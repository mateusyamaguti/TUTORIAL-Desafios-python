# Problema 1011 - Esfera
# Fonte: https://judge.beecrowd.com/

# O problema pede para calcular o volume de uma esfera de raio R,
# usando a fórmula: V = (4/3) * pi * R^3
# Onde pi = 3.14159

# -----------------------------------------------------

# Lemos o valor do raio (inteiro)
R = int(input())

# Definimos o valor de pi conforme especificado no enunciado
pi = 3.14159

# Calculamos o volume da esfera
VOLUME = (4.0/3) * pi * (R ** 3)

# Exibimos o resultado formatado com 3 casas decimais
print(f"VOLUME = {VOLUME:.3f}")
