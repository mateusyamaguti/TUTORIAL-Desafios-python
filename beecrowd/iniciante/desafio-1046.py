# Problema 1046 - Tempo de Jogo
# Fonte: https://judge.beecrowd.com/

# O problema pede para calcular a duração de um jogo em horas,
# considerando que o jogo pode atravessar a meia-noite.

# Solução 1
# -----------------------------------------------------

# Lemos a hora inicial e a hora final
hora_inicial, hora_final = map(int, input().split())

# Caso 1: o jogo termina no mesmo dia
if hora_final > hora_inicial:
    duracao = hora_final - hora_inicial

# Caso 2: o jogo atravessa a meia-noite
elif hora_final < hora_inicial:
    duracao = (24 - hora_inicial) + hora_final

# Caso 3: horas iguais -> jogo durou 24 horas
else:
    duracao = 24

# Exibimos o resultado no formato exigido
print(f"O JOGO DUROU {duracao} HORA(S)")


# Solução 2
# Entrada de dados
hora_inicio, hora_fim = map(int, input().split())

# Condição para cálculo da duração das horas
# Caso o jogo terminar no próximo dia ou iniciar e finalizar as 0 horas
if hora_inicio >= hora_fim:
    duracao = (24 - hora_inicio) + hora_fim
# Caso o jogo termine no mesmo dia
else:
    duracao = hora_fim - hora_inicio

print(f"O JOGO DUROU {duracao} HORA(S)")
