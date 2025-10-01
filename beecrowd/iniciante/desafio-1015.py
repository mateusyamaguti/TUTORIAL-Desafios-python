# Problema 1015 - Distância Entre Dois Pontos
# Fonte: https://judge.beecrowd.com/

# O problema pede para calcular a distância entre dois pontos (x1, y1) e (x2, y2)
# usando a fórmula da distância euclidiana:
# distancia = sqrt((x2 - x1)^2 + (y2 - y1)^2)

# -----------------------------------------------------

# Lemos os dois pontos
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# Calculamos a distância (podemos usar o operador de potência **0.5 ou math.sqrt)
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Exibimos o resultado com 4 casas decimais
print(f"{distancia:.4f}")
