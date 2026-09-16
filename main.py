
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
                    dadosTreino.append(ajustaClassificacao(atributos))
                    qtdInstTreino -= 1
                else:
                    dadosTeste.append(ajustaClassificacao(atributos[:-1]))

        return dadosTreino, dadosTeste


# Função responsável por ajustar a classificação dos atributos, transformando-os
# em números para facilitar a manipulação em python
def ajustaClassificacao(atributos):

    atributosAjustados = [0, 0, 0, 0, 0, 0, -1]

    # Compra (buying)
    match (atributos[0]):
        case "vhigh": 
            atributosAjustados[0] = 0
        case "high": 
            atributosAjustados[0] = 1
        case "med": 
            atributosAjustados[0] = 2
        case "low": 
            atributosAjustados[0] = 3

    # Manutenção (maint)
    match (atributos[1]):
        case "vhigh": 
            atributosAjustados[1] = 0
        case "high": 
            atributosAjustados[1] = 1 
        case "med": 
            atributosAjustados[1] = 2 
        case "low": 
            atributosAjustados[1] = 3 
    
    # Portas (doors)
    match (atributos[2]):
        case "2": 
            atributosAjustados[2] = 0 
        case "3": 
            atributosAjustados[2] = 1 
        case "4": 
            atributosAjustados[2] = 2 
        case "5-more":
            atributosAjustados[2] = 3 

    # Passageiros (persons)
    match (atributos[3]):
        case "2": 
            atributosAjustados[3] = 0
        case "4": 
            atributosAjustados[3] = 1
        case "more": 
            atributosAjustados[3] = 2
    
    # Porta malas (lug_boot)
    match (atributos[4]):
        case "small": 
            atributosAjustados[4] = 0
        case "med": 
            atributosAjustados[4] = 1
        case "big": 
            atributosAjustados[4] = 2

    # Segurança (safety)
    match (atributos[5]):
        case "low": 
            atributosAjustados[5] = 0
        case "med": 
            atributosAjustados[5] = 1
        case "high": 
            atributosAjustados[5] = 2

    # Classe
    if len(atributos) == 7:
        match (atributos[6]):
            case "unacc": 
                atributosAjustados[6] = 0
            case "acc": 
                atributosAjustados[6] = 1

    return atributosAjustados


# Função principal
def main():
    dadosTreino, dadosTeste = lerDados() 


# Chama função principal para funcionamento do projeto
main()
    
