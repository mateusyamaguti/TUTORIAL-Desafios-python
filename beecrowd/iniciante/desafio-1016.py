# Problema 1016 - Distância
# Fonte: https://judge.beecrowd.com/

# O problema pede o tempo necessário para que o carro mais rápido (90 km/h)
# abra uma distância X em relação ao carro mais lento (60 km/h).
#
# Como a diferença de velocidade é 30 km/h, o carro B abre 1 km a cada 2 minutos.
# Portanto, o tempo necessário é: tempo = X * 2

# -----------------------------------------------------

# Lemos a distância X em Km (inteiro)
X = int(input())

# Calculamos o tempo em minutos
tempo = X * 2

# Exibimos o resultado com a unidade "minutos"
print(f"{tempo} minutos")
