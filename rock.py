import random

# Função que gera indrodução da história
def gerar_introducao():
    introducoes = ["Em uma manhar ensolarada", "Há milhares de anos atrás", "Em um planeta muito distante"]
    return random.choice(introducoes)

# Função que gera o desenvolvimento da história
def gerar_desenvolvimento():
    desenvolvimentos = ["Um humano espadachin", "Uma planta falante", "Um alienigena com roupas de humano","Uma Mulher gata espacial", "Um orfã em uma estrada"]
    return random.choice(desenvolvimentos)

# Função que gera o final da história
def gerar_final():
    Finais = ["enfrentou o seu arqui-inimigo.", "foi presa(o).", "Caiu de um penhasco.", "Ganhou na loteria.", "Encontrou o amor."]
    return random.choice(Finais)

#Função principal que gera toda a história
def gerar_historia():
    introducao = gerar_introducao
    desenvolvimento = gerar_desenvolvimento
    final = gerar_final

    historia = f"{introducao} {desenvolvimento} {final}"
    return historia

# Exibe a história gerada
if __name__ == "__main__":
    print(gerar_historia)
