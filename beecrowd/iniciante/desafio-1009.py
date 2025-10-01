# Problema 1009 - Salário com Bônus
# Fonte: https://judge.beecrowd.com/

# O problema pede para calcular o salário final de um vendedor,
# sabendo que ele recebe um salário fixo e mais 15% de comissão
# sobre as vendas realizadas no mês.

# -----------------------------------------------------

# Lemos o nome do vendedor (string)
nome = input()

# Lemos o salário fixo (float)
salario_fixo = float(input())

# Lemos o total de vendas efetuadas no mês (float)
total_vendas = float(input())

# Calculamos o salário final com comissão de 15%
salario_total = salario_fixo + (total_vendas * 0.15)

# Exibimos o resultado com 2 casas decimais
print(f"TOTAL = R$ {salario_total:.2f}")
