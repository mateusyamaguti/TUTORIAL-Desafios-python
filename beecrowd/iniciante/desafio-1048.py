# Problema 1048 - Aumento de Salário
# Fonte: https://judge.beecrowd.com/

# O problema pede para calcular o novo salário de um funcionário
# com base em faixas salariais, aplicando um percentual de reajuste.
# Também deve mostrar o valor do reajuste e o percentual aplicado.

# A ideia é:
# 1. Identificar a faixa salarial
# 2. Definir o percentual correspondente
# 3. Calcular o reajuste e o novo salário
# 4. Exibir os valores formatados com duas casas decimais

# Solução 1
# -------------------------------------------------------------------

# Leitura dos dados
salario = float(input())

# Processamento
if salario <= 400:
    perc = 15
elif salario <= 800:
    perc = 12
elif salario <= 1200:
    perc = 10
elif salario <= 2000:
    perc = 7
else:
    perc = 4

reajuste = salario * perc / 100
novo_salario = salario + reajuste

# Saída
print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {perc} %")

# Solução 2
# -------------------------------------------------------------------

salario_atual = round(float(input()), 2)

def reajuste_salarial(salario_atual, ajuste):
    novo_salario = round((salario_atual * (1+ ajuste/100)),2)
    valor_do_ajuste = salario_atual * (ajuste / 100)
    lista_reajuste = [novo_salario, valor_do_ajuste, ajuste]
    return lista_reajuste

if salario_atual <= 400:
    ajuste = 15
    print(f"Novo salario: {reajuste_salarial(salario_atual, ajuste)[0]:.2f}")
    print(f"Reajuste ganho: {reajuste_salarial(salario_atual, ajuste)[1]:.2f}")
    print(f"Em percentual: {reajuste_salarial(salario_atual, ajuste)[2]} %")
    
elif  salario_atual <= 800:
    ajuste = 12
    print(f"Novo salario: {reajuste_salarial(salario_atual, ajuste)[0]:.2f}")
    print(f"Reajuste ganho: {reajuste_salarial(salario_atual, ajuste)[1]:.2f}")
    print(f"Em percentual: {reajuste_salarial(salario_atual, ajuste)[2]} %")
    
elif  salario_atual <= 1200:
    ajuste = 10
    print(f"Novo salario: {reajuste_salarial(salario_atual, ajuste)[0]:.2f}")
    print(f"Reajuste ganho: {reajuste_salarial(salario_atual, ajuste)[1]:.2f}")
    print(f"Em percentual: {reajuste_salarial(salario_atual, ajuste)[2]} %")
    
    
elif  salario_atual <= 2000:
    ajuste = 7
    print(f"Novo salario: {reajuste_salarial(salario_atual, ajuste)[0]:.2f}")
    print(f"Reajuste ganho: {reajuste_salarial(salario_atual, ajuste)[1]:.2f}")
    print(f"Em percentual: {reajuste_salarial(salario_atual, ajuste)[2]} %")
    
    
elif  salario_atual > 2000:
    ajuste = 4
    print(f"Novo salario: {reajuste_salarial(salario_atual, ajuste)[0]:.2f}")
    print(f"Reajuste ganho: {reajuste_salarial(salario_atual, ajuste)[1]:.2f}")
    print(f"Em percentual: {reajuste_salarial(salario_atual, ajuste)[2]} %")