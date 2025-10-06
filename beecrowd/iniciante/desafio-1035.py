# Problema 1035 - Teste de Seleção 1
# Fonte: https://judge.beecrowd.com/

# O problema pede para verificar várias condições com 4 valores inteiros (A, B, C, D):
# - B deve ser maior que C
# - D deve ser maior que A
# - A soma de C e D deve ser maior que a soma de A e B
# - C e D devem ser positivos
# - A deve ser par
#
# Se todas as condições forem verdadeiras -> "Valores aceitos"
# Caso contrário -> "Valores nao aceitos"


# Solução 1
# -----------------------------------------------------

# Lemos os quatro valores inteiros
A, B, C, D = map(int, input().split())

# Verificamos todas as condições
if (B > C) and (D > A) and ((C + D) > (A + B)) and (C > 0) and (D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")


# Solução 2
# -----------------------------------------------------
a, b, c, d = map(int, input().split())

# Veroficação de condições aninhadas
if (a % 2) == 0:
    if (c > 0) and (d > 0):
        if (c + d) > (a + b):
            if (b > c) and (d > a):
                print("Valores aceitos")
            else:
                print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")
