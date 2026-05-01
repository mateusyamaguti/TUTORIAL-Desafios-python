# Problema 1051 - Imposto de Renda
# Fonte: https://judge.beecrowd.com/

# O problema pede para calcular o imposto de renda com base em faixas salariais.
# Cada faixa possui uma alíquota diferente, e o cálculo é feito de forma progressiva.

# A ideia é:
# 1. Ler o salário
# 2. Verificar em qual(is) faixa(s) ele se encaixa
# 3. Calcular o imposto proporcional em cada faixa
# 4. Exibir o valor do imposto ou "Isento"

# Solução 1
# ------------------------------------------------------------------

# Leitura dos dados
# renda = float(input())

# # Lógica de processamento e saída
# if renda < 2000:
#     print("Isento")
# elif renda < 3000:
#     imposto_de_renda = (renda - 2000) * 0.08
#     print(f"R$ {imposto_de_renda:.2f}")
# elif renda < 4500:
#     imposto_de_renda = (1000 * 0.08) + ((renda - 3000) * 0.18)
#     print(f"R$ {imposto_de_renda:.2f}")
# else:
#     imposto_de_renda = (1000 * 0.08) + (1500 * 0.18) + ((renda - 4500) * 0.28)
#     print(f"R$ {imposto_de_renda:.2f}")
    
# Solução 2 (Utilização de lista de tuplas com os limites)
# ------------------------------------------------------------------
# Problema 1051 - Imposto de Renda

def calcular_imposto(salario):
    faixas = [
        (2000, 0.0),
        (3000, 0.08),
        (4500, 0.18),
        (float('inf'), 0.28) # float("inf") representa infinito positivo.
    ]
    
    imposto = 0.0
    anterior = 0.0

    for limite, aliquota in faixas:
        if salario > limite:
            imposto += (limite - anterior) * aliquota
            anterior = limite
        else:
            imposto += (salario - anterior) * aliquota
            break

    return imposto

# Leitura
salario = float(input())

# Processamento
imposto = calcular_imposto(salario)

# Saída
if imposto == 0:
    print("Isento")
else:
    print(f"R$ {imposto:.2f}")
