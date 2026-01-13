# Problema 1044 - Múltiplos
# O programa verifica se os dois números são múltiplos entre si.

# Solução 1
# ----------------------------------------------------------------------
# Lendo dois valores inteiros
a, b = map(int, input().split())

# Dois números são múltiplos quando a divisão entre eles tem resto zero.
# Ex: 6 e 3 → 6 % 3 == 0 → múltiplos
# Ex: 3 e 6 → 6 % 3 == 0 → múltiplos

if (a % b == 0) or (b % a == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

# Solução 2
# ----------------------------------------------------------------------

# Input de números inteiros
num1, num2 = map(int, input().split())
maior = 0

# Verificar número maior para divisão posterior
if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

# Verificação condição de multiplicidade
if (maior % menor) == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
