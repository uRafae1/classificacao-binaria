from random import Random

PERCENTUAL_TREINO = 0.7
SEED = 42
CLASSES = ("unacc", "acc")


def lerDados():
    dadosPorClasse = {classe: [] for classe in CLASSES}
    with open("dados/car.data", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            atributos = linha.strip().split(",")
            if atributos[-1] in CLASSES:
                dadosPorClasse[atributos[-1]].append(atributos)

    gerador = Random(SEED)
    dadosTreino = []
    dadosTeste = []

    #embaralha e divide cada classe separadamente para preservar sua proporção
    for classe in CLASSES:
        exemplos = dadosPorClasse[classe]
        gerador.shuffle(exemplos)
        qtdInstTreino = int(len(exemplos) * PERCENTUAL_TREINO)
        dadosTreino.extend(exemplos[:qtdInstTreino])
        dadosTeste.extend(exemplos[qtdInstTreino:])

    gerador.shuffle(dadosTreino)
    gerador.shuffle(dadosTeste)
    return dadosTreino, dadosTeste



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

                pCondicional[atributo][valor][classe] = ocorrencias / total

    return pPrior, pCondicional



def classificaNaiveBayes(pPrior, pCondicional, exemploNovo):
    melhorProbabilidade = 0
    classePredita = None

    for classe in pPrior:
        probClasse = pPrior[classe]

        for atributo, valor in enumerate(exemploNovo):
            probCondicional = pCondicional[atributo][valor][classe]
            probClasse *= probCondicional

        if probClasse > melhorProbabilidade:
            melhorProbabilidade = probClasse
            classePredita = classe

    return classePredita


def avaliarModelo(pPrior, pCondicional, dadosTeste):
    matriz = {"VP": 0, "FP": 0, "VN": 0, "FN": 0}

    # acc é a classe positiva; unacc é a classe negativa.
    for instancia in dadosTeste:
        classeReal = instancia[-1]
        classePredita = classificaNaiveBayes(pPrior, pCondicional, instancia[:-1])

        if classeReal == "acc":
            if classePredita == "acc":
                matriz["VP"] += 1
            else:
                matriz["FN"] += 1
        else:
            if classePredita == "acc":
                matriz["FP"] += 1
            else:
                matriz["VN"] += 1

    return matriz


def calcularMetricas(matriz):
    vp = matriz["VP"]
    fp = matriz["FP"]
    vn = matriz["VN"]
    fn = matriz["FN"]
    total = vp + fp + vn + fn

    # Se o denominador for zero, a métrica é indefinida; aqui convencionamos 0.
    return {
        "Acurácia": (vp + vn) / total if total else 0.0,
        "Sensibilidade": vp / (vp + fn) if vp + fn else 0.0,
        "Especificidade": vn / (vn + fp) if vn + fp else 0.0,
        "Precisão": vp / (vp + fp) if vp + fp else 0.0,
    }


def main():
    dadosTreino, dadosTeste = lerDados()
    pPrior, pCondicional = treinaNaiveBayes(dadosTreino)
    matriz = avaliarModelo(pPrior, pCondicional, dadosTeste)
    metricas = calcularMetricas(matriz)

    print(f"Total de instâncias: {len(dadosTreino) + len(dadosTeste)}")
    print(f"Treino: {len(dadosTreino)} ({PERCENTUAL_TREINO:.0%})")
    print(f"Teste: {len(dadosTeste)} ({1 - PERCENTUAL_TREINO:.0%})")

    for nome, dados in (("Treino", dadosTreino), ("Teste", dadosTeste)):
        print(f"\n{nome}:")
        for classe in ("acc", "unacc"):
            quantidade = sum(instancia[-1] == classe for instancia in dados)
            print(f"{classe} = {quantidade}")

    print("\nMatriz de confusão (positiva = acc; negativa = unacc):")
    for nome, quantidade in matriz.items():
        print(f"{nome} = {quantidade}")

    print("\nMétricas:")
    for nome, valor in metricas.items():
        print(f"{nome}: {valor:.2%}")


if __name__ == "__main__":
    main()
