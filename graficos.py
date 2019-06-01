import matplotlib.pyplot as plt
import numpy as np
from MemConfig import TAM_BLOCO, TAM_MEM

def global_graficos():
    global y_espera, y_quantidade, y_tamanho, y_memoria, y_miss, x
    y_espera = []
    y_quantidade = []
    y_tamanho = []
    y_memoria = []
    y_miss = []
    x = []


def inicio_graficos():
    global tempo_medio_espera, qnt_buracos, tam_medio_buracos, uso_memo, lista_ciclo, erro_aloca
    tempo_medio_espera = []
    qnt_buracos = []
    tam_medio_buracos = []
    uso_memo = []
    lista_ciclo = []
    erro_aloca = []


def parametros_graficos(lista_principal, memoria, espacos, executados, ciclo):

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
        espera /= len(lista_principal)
    else:
        espera = 0

    # quantidade de miss na alocacao num ciclo de clock
    miss = 0
    if lista_principal:
        for i in lista_principal:
            miss += i[5]

    tempo_medio_espera.append(espera)
    qnt_buracos.append(len(espacos))
    tam_medio_buracos.append(media)
    uso_memo.append((memoria.count(1)/TAM_MEM)*100)
    lista_ciclo.append(ciclo)
    erro_aloca.append(miss)


def politica_graficos():

    y_espera.append(tempo_medio_espera)
    y_quantidade.append(qnt_buracos)
    y_tamanho.append(tam_medio_buracos)
    y_memoria.append(uso_memo)
    y_miss.append(erro_aloca)
    x.append(lista_ciclo)


def plota():
    global y_espera, y_quantidade, y_tamanho, y_memoria, y_miss, x

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
    for lista in y_miss:
        while len(x[maior]) > len(lista):
            lista.append(0)

    x = x[maior]

    # gráfico 1: uso da memória
    plt.subplot(3, 1, 1)
    plt.ylim([0,100])
    plt.plot(x, y_memoria[0], label="FF", color="blue")
    plt.title('Uso da memória\n')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.ylim([0,100])
    plt.plot(x, y_memoria[1], label="BF", color="green")
    plt.ylabel('%')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.ylim([0,100])
    plt.plot(x, y_memoria[2], label="WF", color="red")
    plt.xlabel('Ciclo')
    plt.grid(True)
    plt.legend()

    plt.savefig('1uso_memo.png')
    plt.show()

    # gráfico 2: quantidade de buracos
    plt.subplot(3, 1, 1)
    plt.ylim([0,5])
    plt.plot(x, y_quantidade[0], label="FF", color="blue")
    plt.title('Quantidade de buracos na memória\n')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.ylim([0,5])
    plt.plot(x, y_quantidade[1], label="BF", color="green")
    plt.ylabel('Nº de buracos')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.ylim([0,5])
    plt.plot(x, y_quantidade[2], label="WF", color="red")
    plt.xlabel('Ciclo')
    plt.grid(True)
    plt.legend()

    plt.savefig('2qnt_buracos.png')
    plt.show()

    # gráfico 3: tamanho dos buracos
    plt.subplot(3, 1, 1)
    plt.ylim([0,TAM_MEM])
    plt.plot(x, y_tamanho[0], label="FF", color="blue")
    plt.title('Tamanho dos buracos na memória\n')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.ylim([0,TAM_MEM])
    plt.plot(x, y_tamanho[1], label="BF", color="green")
    plt.ylabel('kB')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.ylim([0,TAM_MEM])
    plt.plot(x, y_tamanho[2], label="WF", color="red")
    plt.xlabel('Ciclo')
    plt.grid(True)
    plt.legend()

    plt.savefig('3tam_buracos.png')
    plt.show()

    # gráfico 4: tempo médio de espera
    plt.subplot(3, 1, 1)
    plt.ylim([0,30])
    plt.plot(x, y_espera[0], label="FF", color="blue")
    plt.title('Tempo médio de espera para entrar na memória\n')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.ylim([0,30])
    plt.plot(x, y_espera[1], label="BF", color="green")
    plt.ylabel('Tempo')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.ylim([0,30])
    plt.plot(x, y_espera[2], label="WF", color="red")
    plt.xlabel('Ciclo')
    plt.grid(True)
    plt.legend()

    plt.savefig('4media_espera.png')
    plt.show()

    # gráfico 5: quantidade de miss
    plt.subplot(3, 1, 1)
    plt.ylim([0,60])
    plt.plot(x, y_miss[0], label="FF", color="blue")
    plt.title('Quantidade de erros de alocação por ciclo\n')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.ylim([0,60])
    plt.plot(x, y_miss[1], label="BF", color="green")
    plt.ylabel('Erros')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.ylim([0,60])
    plt.plot(x, y_miss[2], label="WF", color="red")
    plt.xlabel('Ciclo')
    plt.grid(True)
    plt.legend()

    plt.savefig('5erros.png')
    plt.show()
