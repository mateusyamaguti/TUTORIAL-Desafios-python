# Problema 1020 - Idade em Dias
# Fonte: https://judge.beecrowd.com/

# O problema pede para converter uma quantidade de dias em anos, meses e dias.
# Considera-se:
# 1 ano = 365 dias
# 1 mês = 30 dias

# -----------------------------------------------------

# Lemos o valor inteiro (idade em dias)
dias = int(input())

# Calculamos quantos anos cabem dentro desse número de dias
anos = dias // 365
dias = dias % 365  # sobra de dias depois de retirar os anos

# Calculamos quantos meses cabem no que restou
meses = dias // 30
dias = dias % 30   # sobra de dias depois de retirar os meses

# O que sobrar são os dias finais
# (já armazenado em 'dias')

# Exibimos no formato exigido
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
