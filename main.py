#0- IP
#1- Ciclo de chegada
#2- Ciclos para executar / ciclo em que foi executado
#3- Tamanho
#4- Tempo de espera
#5- Qntd Miss
#6- Posição na memória

from MemConfig import TAM_BLOCO, TAM_MEM

def inicializacao():
    global lista_programas, lista_principal, memoria, executados, executando, ciclo
    lista_principal = []
    executados = []
    processador = []
    memoria = []
    executando = []
    ciclo = 0

    # cria lista de zeros para representar memoria
    memoria = [0] * int(TAM_MEM / TAM_BLOCO)

    # abre arquivo de entrada
    arq = open("entrada", "r")
    # separa o arquivo por linhas
    conteudo = arq.read().split('\n')
    # separa as linhas em posicoes acessiveis ID, Tchegada, Tam, Texecucao
    entrada = []
    for linha in conteudo:
        entrada.append(linha.split(' '))
    # torna a lista de entrada uma lista de inteiros
    lista_programas = []
    for programa in entrada[:-1]:
        linha = []
        for dado in programa:
            linha.append(int(dado))
        lista_programas.append(linha)


def checa_lista():
    # percorre lista de programas e adiciona os que entram no ciclo a lista
    for i in range(0, len(lista_programas)):
        if lista_programas[i][1] == ciclo:
            lista_principal.append(lista_programas[i])
            lista_principal[-1].append(0)
            lista_principal[-1].append(0)


def checa_inicio_fila():
    # checa se há programas na lista principal
    if len(lista_principal) != 0:
        return (True)
    else:
        return(False)


def ff():
    # percorre lista principal
    for pos_programa in range (0, len(lista_principal)):
        pos_memo = 0
        qnt = 0
        # percorre memória buscando primeiro espaço para alocar processo
        for cont in range (0, len(memoria)):
            if memoria[cont] == 0:
                if qnt != 0:
                    qnt += 1
                else:
                    pos_memo = cont
                    qnt = 1
                # verifica se programa pode ser alocado no espaço
                if qnt == lista_principal[pos_programa][3]:
                    aloca(pos_programa, pos_memo)
                    return
            else:
                qnt = 0
        lista_principal[pos_programa][5] += 1


def aloca(pos_programa, pos_memo):
    lista_principal[pos_programa].append(pos_memo)
    executando.append(lista_principal[pos_programa])
    lista_principal.pop(pos_programa)
    print('tamanho: ',executando[-1][3])
    print('pos memo: ',executando[-1][6])
    for i in range (0, executando[-1][3]):
        print(pos_memo + i)
        memoria[pos_memo + i] = 1


def executa():
    try:
        for i in range (0, len(executando)):
            executando[i][2] -= 1
            if executando[i][2] == 0:
                executando[i][2] = ciclo
                for j in range (0, executando[i][3]):
                    memoria[executando[i][6]+j] = 0
                executados.append(executando[i])
                executando.pop(i)
    except:
        return


def prox_ciclo():

    for programa in lista_principal:
        programa[4] += 1
    if len(executados) == len(lista_programas):
        return False
    return True


#================================= MAIN =================================#

########### FF ###########

run = True
inicializacao()

while(run):
    checa_lista()
    if checa_inicio_fila():
        ff()
    executa()

    print("\nCiclo: ", ciclo)
    print("Memoria: ", memoria)
    print("Lista Principal: ", lista_principal)
    print("Executando: ", executando)
    print("Executados: ", executados)

    ciclo += 1
    run = prox_ciclo()

##########################
