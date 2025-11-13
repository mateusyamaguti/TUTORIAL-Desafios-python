# Problema 1040 - Média 3
# Fonte: https://judge.beecrowd.com/

# O problema pede para calcular a média ponderada de quatro notas,
# decidir a situação do aluno (aprovado, exame ou reprovado),
# e, se necessário, ler a nota do exame e recalcular a média final.

# Solução
# -----------------------------------------------------

# Input dos valores da notas
n1, n2, n3, n4 = map(float, input().split())

# Cálculo da média
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10
print(f"Media: {media:.1f}")

# Condição para aprovação, reprova e exame
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
# Caso em que o aluno fica de exame
else:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    # Cálculo da média final
    media_final = (media + nota_exame) / 2
    # Condição de aprovação e reprovação
    if media_final >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado")
    print(f"Media final: {media_final:.1f}")
