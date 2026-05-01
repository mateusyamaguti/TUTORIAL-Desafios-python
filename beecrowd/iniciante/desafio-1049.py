# Problema 1049 - Animal
# Fonte: https://judge.beecrowd.com/

# O problema pede para identificar um animal com base em três características:
# 1. Tipo (vertebrado ou invertebrado)
# 2. Classe (ave, mamifero, inseto, anelideo)
# 3. Alimentação (carnivoro, herbivoro, onivoro, hematofago)

# A ideia é:
# 1. Ler as três entradas
# 2. Usar estruturas condicionais para mapear corretamente
# 3. Imprimir o nome do animal correspondente

# Solução 1

# Leitura das variáveis reais de entrada
vertebral_structure = str(input())
animal_kingdom = str(input())
animal_feed = str(input())


# Grupos dos vertebrados
if vertebral_structure == "vertebrado":
    # Grupos das aves
    if animal_kingdom == "ave":
        if animal_feed == "carnivoro":
            print("aguia")
        else:
            print("pomba")
            
    # Grupos dos mamíferos 
    else:
        if animal_feed == "onivoro":
            print("homem")
        else:
            print("vaca")
        
        
# Grupo dos invertebrados        
else:
    if animal_kingdom == "inseto":
        if animal_feed == "herbivoro":
            print("lagarta")
        else:
            print("pulga")
    else:
        if animal_feed == "onivoro":
            print("minhoca")
        else:
            print("sanguessuga")
            
            
            
            

# Solução 2 (mais compacta - Utilização de dicionário)
# --------------------------------------------------------------

# Leitura dos dados
chave = (input(), input(), input())

# Processamento
animais = {
    ("vertebrado", "ave", "carnivoro"): "aguia",
    ("vertebrado", "ave", "onivoro"): "pomba",
    ("vertebrado", "mamifero", "onivoro"): "homem",
    ("vertebrado", "mamifero", "herbivoro"): "vaca",
    ("invertebrado", "inseto", "hematofago"): "pulga",
    ("invertebrado", "inseto", "herbivoro"): "lagarta",
    ("invertebrado", "anelideo", "hematofago"): "sanguessuga",
    ("invertebrado", "anelideo", "onivoro"): "minhoca",
}

# Saída
print(animais[chave])