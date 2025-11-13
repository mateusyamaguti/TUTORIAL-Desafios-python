# Crie uma função lambda em python que organize uma lista de tupla

# Lista de tupla para exemplo
lista_de_tupla = [
    ("English", 88),
    ("Science", 90),
    ("Maths", 97),
    ("Social sciences", 82),
]

# Método sort é usado para ordenar uma lista, o parâmetro key é utilizado para determinar a chave de ordenação
# Neste caso o número inteiro da tupla
lista_de_tupla.sort(key=lambda x: x[1])

# Impressão da lista ordenada
print(lista_de_tupla)
