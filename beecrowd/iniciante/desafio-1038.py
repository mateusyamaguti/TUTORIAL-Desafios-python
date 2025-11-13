# Problema 1038 - Lanche
# Fonte: https://judge.beecrowd.com/

# O problema pede para calcular o valor total a pagar de um pedido,
# a partir do código do item e da quantidade, segundo a tabela de preços.

# Solução 1
# -----------------------------------------------------

# Lemos o código do produto e a quantidade
codigo, quantidade = map(int, input().split())

# Definimos os preços de cada produto em um dicionário
precos = {
    1: 4.00,  # Cachorro-quente
    2: 4.50,  # X-Salada
    3: 5.00,  # X-Bacon
    4: 2.00,  # Torrada simples
    5: 1.50,  # Refrigerante
}

# Calculamos o total multiplicando o preço pelo número de unidades
total = precos[codigo] * quantidade

# Exibimos o resultado formatado com 2 casas decimais
print(f"Total: R$ {total:.2f}")


# Solução 2
# -----------------------------------------------------

# Criação de dicionário dos lanches sobre os códigos respectivos
dic_lanche = {
    1: ("Cachorro Quente", 4.00),
    2: ("X-Salada", 4.50),
    3: ("X-Bacon", 5.00),
    4: ("Torrada simples", 2.00),
    5: ("Refrigerante", 1.50),
}

# Input do código do lanche e quantidade
codigo, quantidade = map(int, input().split())

# Buscar o valor do código (key) do dicionários
propriedade_lache = dic_lanche[codigo]

# Buscar valor do lanche dentro da propriedade (tupla do lache)
valor_lanche = propriedade_lache[1]

# Calcular o valor do pedido total
valor_do_pedido = valor_lanche * quantidade

# Imprimir o valor do pedido
print(f"Total: R$ {valor_do_pedido:.2f}")


ano = "dois mill"
ano.capi
