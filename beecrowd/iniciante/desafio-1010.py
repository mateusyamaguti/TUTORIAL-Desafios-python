# Problema 1010 - Cálculo Simples
# Fonte: https://judge.beecrowd.com/

# O problema pede para calcular o valor total a pagar por duas peças,
# a partir do código da peça, quantidade e valor unitário.

# -----------------------------------------------------

# Lemos a primeira linha e dividimos em 3 valores
codigo1, qtd1, valor1 = input().split()

# Convertendo os valores: código e quantidade para int, valor para float
codigo1 = int(codigo1)
qtd1 = int(qtd1)
valor1 = float(valor1)

# Lemos a segunda linha
codigo2, qtd2, valor2 = input().split()
codigo2 = int(codigo2)
qtd2 = int(qtd2)
valor2 = float(valor2)

# Calculamos o valor total (quantidade * valor unitário)
total = qtd1 * valor1 + qtd2 * valor2

# Exibimos o resultado formatado com 2 casas decimais
print(f"VALOR A PAGAR: R$ {total:.2f}")
