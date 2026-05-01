# Problema 1050 - DDD
# Fonte: https://judge.beecrowd.com/

# O problema pede para identificar a cidade correspondente a um código DDD.
# Caso o DDD não exista na lista, deve-se imprimir "DDD nao cadastrado".

# A ideia é:
# 1. Ler o DDD
# 2. Mapear o DDD para a cidade usando um dicionário
# 3. Verificar se o DDD existe
# 4. Exibir a cidade ou mensagem de erro

# Solução 1
# -------------------------------------------------------------------------

# Leitura dos dados
ddd = int(input())

# Processamento
tabela_ddd = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

# Saída
print(tabela_ddd.get(ddd, "DDD nao cadastrado"))

# Solução 2
# -------------------------------------------------------------------------

ddd = int(input())

ddd_dict = {61: "Brasilia",
            71: "Salvador",
            11: "Sao Paulo",
            21: "Rio de Janeiro",
            32: "Juiz de Fora",
            19: "Campinas",
            27: "Vitoria",
            31: "Belo Horizonte"}

if ddd in list(ddd_dict):
    print(ddd_dict[ddd])
else:
    print("DDD nao cadastrado")