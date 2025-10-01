# Problema 1014 - Consumo
# Fonte: https://judge.beecrowd.com/

# O problema pede para calcular o consumo médio de um carro,
# dado a distância percorrida (Km) e o combustível gasto (litros).

# Fórmula: consumo = X / Y

# -----------------------------------------------------

# Lemos a distância total percorrida (em Km, inteiro)
X = int(input())

# Lemos o total de combustível gasto (em litros, float)
Y = float(input())

# Calculamos o consumo médio
consumo = X / Y

# Exibimos o resultado formatado com 3 casas decimais
print(f"{consumo:.3f} km/l")
