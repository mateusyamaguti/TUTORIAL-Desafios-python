# Problema 1041 - Coordenadas de um Ponto
# Fonte: https://judge.beecrowd.com/

# O problema pede para identificar em qual região do plano cartesiano
# o ponto (X, Y) se encontra: um dos quatro quadrantes, eixo X, eixo Y, ou origem.

# Solução 1
# -----------------------------------------------------

# Lemos os valores reais das coordenadas
x, y = map(float, input().split())

# Verificamos as condições na ordem adequada
if x == 0 and y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")


# Solução 2
# -----------------------------------------------------

# Input / Leitura das variáveis iniciais
x, y = map(float, input().split())

# Condição inicial de origem
if x == 0 and y == 0:
    print("Origem")

# Condições para identificação de eixo
elif x == 0 and y != 0:
    print("Eixo Y")
elif x != 0 and y == 0:
    print("Eixo X")

# Condições para identificação de quadrantes
elif x > 0:
    if y > 0:
        print("Q1")
    else:
        print("Q4")
elif x < 0:
    if y > 0:
        print("Q2")
    else:
        print("Q3")
