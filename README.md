# Car Evaluation Dataset

O dataset utilizado pode ser encontrado em:

https://archive.ics.uci.edu/dataset/19/car+evaluation

## Classes utilizadas

Dentre as classes descritas no dataset original, foram descartadas as classes **`good`** e **`v-good`**.

Foram escolhidas para exclusão pois representam apenas **7,755% dos dados**.

Após a remoção das instâncias pertencentes às classes descartadas, temos:

**1728 - 134 = 1594 instâncias**

## Probabilidade a priori das classes

As probabilidades a priori das classes restantes são:

| Classe                    |     Cálculo |         Probabilidade |
| ------------------------- | ----------: | --------------------: |
| **Inaceitável (`unacc`)** | 1210 / 1594 | **≈ 0,7591 (75,91%)** |
| **Aceitável (`acc`)**     |  384 / 1594 | **≈ 0,2409 (24,09%)** |
