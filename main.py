
# Importações utilizadas
from math import *
from collections import defaultdict

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
                    dadosTeste.append(atributos)

        return dadosTreino, dadosTeste


# Função responsável por fazer o treinamento do Naive Bayes, ou seja
def treinaNaiveBayes(dadosTreino):
    pPrior = {}
    for instancia in dadosTreino:
        classe = instancia[-1]

        if classe not in pPrior:
            pPrior[classe] = 0

        pPrior[classe] += 1

    for classe in pPrior:
        pPrior[classe] /= len(dadosTreino)

    pCondicional = {}
    for atributo in range(6):
        pCondicional[atributo] = {}

        valores = set(instancia[atributo] for instancia in dadosTreino)

        for valor in valores:
            pCondicional[atributo][valor] = {}

            for classe in pPrior:
                total = 0
                ocorrencias = 0

                for instancia in dadosTreino:
                    if instancia[-1] == classe:
                        total += 1

                        if instancia[atributo] == valor:
                            ocorrencias += 1

                pCondicional[atributo][valor][classe] = (ocorrencias / total)

    return pPrior, pCondicional


# Função principal
def main():
    dadosTreino, dadosTeste = lerDados() 
    print(treinaNaiveBayes(dadosTreino))


# Chama função principal para funcionamento do projeto
main()
    
