# Problema 1047 - Tempo de Jogo com Minutos
# Fonte: https://judge.beecrowd.com/

# A ideia é converter tudo para minutos,
# calcular a diferença e depois converter de volta para horas e minutos.

# Solução 1
# -----------------------------------------------------

# Leitura dos dados
hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

# Convertemos os horários para minutos totais
inicio = hora_inicial * 60 + minuto_inicial
fim = hora_final * 60 + minuto_final

# Calculamos a duração em minutos
duracao = fim - inicio

# Se a duração for menor ou igual a zero, significa que virou o dia
# ou que o horário inicial e final são iguais (24 horas de duração)
if duracao <= 0:
    duracao += 24 * 60

# Convertendo a duração para horas e minutos
horas = duracao // 60
minutos = duracao % 60

# Exibindo o resultado
print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")


# Solução 2
# -----------------------------------------------------

hora_inicial, minuto_inicial, hora_final, minutos_final = map(int, input().split())


# Cálculo de horas caso o jogo termine no dia seguinte
if hora_inicial >= hora_final and minutos_final < minuto_inicial:
    duracao_hora = (24 - hora_inicial) + hora_final

# Cálculo de horas caso o jogo termine no mesmo dia
else:
    duracao_hora = hora_final - hora_inicial


if minutos_final >= minuto_inicial:
    duracao__minutos = abs(minutos_final - minuto_inicial)
else:
    duracao__minutos = 60 - abs(minutos_final - minuto_inicial)
    duracao_hora -= 1

# Caso o jogo  inicie a 00:00 de um dia e termine a 00:00 do seguinte
if hora_inicial == minuto_inicial == hora_final == minutos_final == 0:
    duracao_hora = 24
    duracao__minutos = 0

print(f"O JOGO DUROU {duracao_hora} HORA(S) E {duracao__minutos} MINUTO(S)")
