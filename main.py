
# Importações utilizadas
from math import *

# Função responsável por ler os dados do arquivo de entrada. Ela ignora as intâncias 
# de classes indesejadas e retorna 2 vetores, um contendo dados para treinamento 
# (com 80% das intâncias) e um contendo dados para testes (com 20% das instâncias)
def lerDados():
    qtdInstTreino = floor(1594 * 0.8)

    with open("dados/car.data", "r") as arquivo:
        dadosTreino = []
        dadosTeste = []

        for linha in arquivo:
            linha = linha.strip()

            if linha:
                atributos = linha.split(",")
                if atributos[6] == "good" or atributos[6] == "vgood":
                    continue

                if qtdInstTreino > 0:
                    dadosTreino.append(atributos)
                    qtdInstTreino -= 1
                else:
                    dadosTeste.append(atributos[:-1])

        return dadosTreino, dadosTeste

dadosTreino, dadosTeste = lerDados()
    
