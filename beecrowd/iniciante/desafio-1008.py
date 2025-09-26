# Problema 1008 - Salário
# Fonte: https://judge.beecrowd.com/

# O problema pede para calcular o salário de um funcionário
# sabendo o número do funcionário, o total de horas trabalhadas
# e o valor que recebe por hora.

# -----------------------------------------------------

# Lemos o número do funcionário (inteiro)
numero_funcionario = int(input())

# Lemos o número de horas trabalhadas (inteiro)
horas_trabalhadas = int(input())

# Lemos o valor recebido por hora (float, pois pode ter decimais)
valor_por_hora = float(input())

# Calculamos o salário multiplicando horas pelo valor da hora
salario = horas_trabalhadas * valor_por_hora

# Exibimos o número do funcionário
print(f"NUMBER = {numero_funcionario}")

# Exibimos o salário com 2 casas decimais
print(f"SALARY = U$ {salario:.2f}")
