# Problema 1002 - Área do Círculo
# Fonte: https://judge.beecrowd.com/

# O problema pede para calcular a área de um círculo dado o raio R.
# Fórmula: A = π * R^2
# O valor de π deve ser 3.14159 e o resultado precisa ter 4 casas decimais.

# -----------------------------------------------------

# Lemos o valor do raio (tipo float, pois pode ter casas decimais)
raio = float(input())

# Definimos o valor de π conforme especificado no enunciado
pi = 3.14159

# Calculamos a área usando a fórmula matemática
area = pi * (raio ** 2)

# Exibimos o resultado formatado com 4 casas decimais
# Usamos :.4f para forçar 4 dígitos depois do ponto decimal
print(f"A={area:.4f}")
