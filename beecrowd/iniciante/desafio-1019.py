# Problema 1019 - Conversão de Tempo
# Fonte: https://judge.beecrowd.com/

# O problema pede para converter um valor em segundos para o formato:
# horas:minutos:segundos
#
# Exemplo:
# Entrada: 556
# Saída:   0:9:16

# -----------------------------------------------------
# Solução 1
# Lemos o valor em segundos (inteiro)
N = int(input())

# Primeiro, calculamos quantas horas cabem em N.
# Uma hora tem 3600 segundos.
horas = N // 3600  # divisão inteira
N = N % 3600       # resto dos segundos que sobraram

# Agora, calculamos quantos minutos cabem no que restou.
# Um minuto tem 60 segundos.
minutos = N // 60
N = N % 60         # resto dos segundos que sobraram

# O valor final que restar são os segundos.
segundos = N

# Exibimos no formato exigido: H:M:S
print(f"{horas}:{minutos}:{segundos}")

# -------------------------------------------------------
# Solução 2
# Problema 1019 - Conversão de Tempo
# Solução alternativa utilizando listas

# Lemos o valor em segundos
n = int(input())

# Lista com os períodos em segundos: 1 hora (3600), 1 minuto (60) e 1 segundo (1)
periodo = [3600, 60, 1]

# Inicializamos as variáveis de horas, minutos e segundos
horas, minutos, segundos = 0, 0, 0

# Criamos uma lista que irá armazenar o resultado final
lista_de_variaveis_temporais = [horas, minutos, segundos]

# Percorremos cada unidade de tempo (hora, minuto, segundo)
for i, temp in enumerate(periodo):
    # Calculamos quantas vezes o período atual "cabe" no valor restante de n
    temp = n // periodo[i]

    # Se houver pelo menos 1 unidade (ex: pelo menos 1 hora, ou 1 minuto, etc.)
    if temp > 0:
        # Atualizamos a lista de resultados na posição correta
        lista_de_variaveis_temporais[i] = temp

        # Subtraímos do total o equivalente em segundos
        n -= temp * periodo[i]

# Ao final, imprimimos os resultados no formato H:M:S
print(f"{lista_de_variaveis_temporais[0]}:{lista_de_variaveis_temporais[1]}:{lista_de_variaveis_temporais[2]}")
