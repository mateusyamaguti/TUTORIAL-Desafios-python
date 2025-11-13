# Problema 1042 - Sort Simples
# Fonte: https://judge.beecrowd.com/

# O problema pede para ler três valores inteiros,
# exibi-los em ordem crescente e depois na ordem original.
#
# Etapas:
# 1. Ler os valores
# 2. Criar uma cópia da lista original
# 3. Ordenar a cópia
# 4. Exibir as duas versões conforme o enunciado

# Solução 1
# -----------------------------------------------------

# Lemos os três números inteiros
a, b, c = map(int, input().split())

# Criamos uma lista com os valores originais
valores = [a, b, c]

# Criamos uma cópia da lista e ordenamos
ordenados = sorted(valores)

# Exibimos os valores ordenados (um por linha)
for v in ordenados:
    print(v)

# Linha em branco entre as duas partes
print()

# Exibimos os valores originais (um por linha)
for v in valores:
    print(v)
# Solução 2
# -----------------------------------------------------

# Ler valores
num1, num2, num3 = map(int, input().split())

# Criar lista orginal
num_list_original = [num1, num2, num3]

# Copia para de lista para manipulação
num_list_new = num_list_original[:]
num_list_new.sort()

# Imprimir lista ordenada
for c in range(len(num_list_new)):
    print(num_list_new[c])

print()

# Imprimir lista original
for c in range(len(num_list_original)):
    print(num_list_original[c])
