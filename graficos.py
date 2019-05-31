import matplotlib.pyplot as plt
import numpy as np
from MemConfig import TAM_BLOCO, TAM_MEM

def global_graficos():
    global y_espera, y_quantidade, y_tamanho, y_memoria, x
    y_espera = []
    y_quantidade = []
    y_tamanho = []
    y_memoria = []
    x = []


def inicio_graficos():
    global tempo_medio_espera, qnt_buracos, tam_medio_buracos, uso_memo, lista_ciclo
    tempo_medio_espera = []
    qnt_buracos = []
    tam_medio_buracos = []
    uso_memo = []
    lista_ciclo = []


def parametros_graficos(lista_principal, memoria, espacos, ciclo):

    # tamanho médio dos espaços
    media = 0
    if espacos:
        for i in espacos:
            media += i[1]
        media/=len(espacos)
    else:
        media = 0

    # tempo médio de espera
    espera = 0
    if lista_principal:
        for i in lista_principal:
            espera += i[4]
        espera/=len(lista_principal)
    else:
        espera = 0

    tempo_medio_espera.append(espera)
    qnt_buracos.append(len(espacos))
    tam_medio_buracos.append(media)
    uso_memo.append((memoria.count(1)/TAM_MEM)*100)
    lista_ciclo.append(ciclo)


def politica_graficos():

    y_espera.append(tempo_medio_espera)
    y_quantidade.append(qnt_buracos)
    y_tamanho.append(tam_medio_buracos)
    y_memoria.append(uso_memo)
    x.append(lista_ciclo)


def plota():
    global y_espera, y_quantidade, y_tamanho, y_memoria, x

    # definindo qual foi o maior tempo de execução para gerar os gráficos
    maior = 0
    for i in range (1, len(x)):
        if len(x[i]) > len(x[maior]):
            maior = i

    total = []

    # deixando componentes x e y com mesmos tamanhos
    for lista in y_espera:
        while len(x[maior]) > len(lista):
            lista.append(0)
    for lista in y_quantidade:
        while len(x[maior]) > len(lista):
            lista.append(0)
    for lista in y_tamanho:
        while len(x[maior]) > len(lista):
            lista.append(0)
    for lista in y_memoria:
        while len(x[maior]) > len(lista):
            lista.append(0)



    x = x[maior]
    plt.plot(x, y_memoria[0], label="FF")
    plt.plot(x, y_memoria[1], label="BF")
    plt.plot(x, y_memoria[2], label="WF")

    plt.xlabel("Ciclo")
    plt.ylabel("Tempo médio de espera")

    plt.title("Grafico 1\nTempo médio de espera x Ciclo")
    plt.legend()
    plt.show()
