# Problema 1045 - Tipos de Triângulos

# Solução 1
# -------------------------------------------------------
# Lendo os três valores
a, b, c = map(float, input().split())

# Primeiro passo: ordenar em ordem decrescente para que A seja o maior
A, B, C = sorted([a, b, c], reverse=True)

# Agora A é o maior entre os três

# 1) Verificação se forma um triângulo
# Uma condição básica: o maior valor tem que ser menor que a soma dos outros dois
if A >= B + C:
    print("NAO FORMA TRIANGULO")

else:
    # 2) Classificação pelo ângulo (usando relação dos quadrados)

    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")

    if A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")

    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")

    # 3) Classificação pelos lados

    # Todos iguais
    if A == B == C:
        print("TRIANGULO EQUILATERO")

    # Dois iguais (e já sabemos que não é equilátero)
    elif A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")


# Solução 2
# -------------------------------------------------------

# Ler dados que serão os lados dos triângulos
a, b, c = map(float, input().split())

# Criar lista de dados ordenados crescente
lista_lados = [a, b, c]
lista_lados.sort(reverse=True)
a, b, c = lista_lados[0], lista_lados[1], lista_lados[2]

# Condição de existência de um triângulo
if a < (b + c):
    # Condições para cada tipo de triângulo
    if (a**2) == (b**2 + c**2):
        print("TRIANGULO RETANGULO")
    if (a**2) > (b**2 + c**2):
        print("TRIANGULO OBTUSANGULO")
    if (a**2) < (b**2 + c**2):
        print("TRIANGULO ACUTANGULO")
    if a == b or b == c or a == c:
        if a == b == c:
            print("TRIANGULO EQUILATERO")
        else:
            print("TRIANGULO ISOSCELES")
else:
    print("NAO FORMA TRIANGULO")
