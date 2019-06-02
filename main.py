# Listas com processos:
#0- IP
#1- Ciclo de chegada
#2- Ciclos para executar / ciclo em que foi executado
#3- Tamanho
#4- Tempo de espera (até entrar na memória)
#5- Qntd Miss
#6- Posição na memória

# Espaços:
#0- Posição
#1- Tamanho

from MemConfig import TAM_BLOCO, TAM_MEM
from graficos import*

def inicializacao():
    global lista_programas, lista_principal, memoria, executados, executando, espacos, ciclo
    lista_principal = []
    executados = []
    processador = []
    memoria = []
    executando = []
    espacos = []
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
            lista_principal[-1].append(0)


def checa_inicio_fila():
    # checa se há programas na lista principal
    if len(lista_principal) != 0:
        return (True)
    else:
        return(False)


def mapeia_memoria():   # mapeia memória e registra posições e quantidades de espaços vazios (espacos 0 e 1)
    # esvazia lista de espaços
    while len(espacos) > 0:
        espacos.pop(0)

    # busca séries de espaços e aloca na lista espaços
    aux = [0,0]
    for cont in range (0, len(memoria)):
        if memoria[cont] == 0:
            if aux[1] != 0:
                aux[1] += 1
            else:
                aux[0] = cont
                aux[1] = 1
        else:
            if aux[1] != 0:
                espacos.append(aux)
                aux = [0,0]

    if aux[1]:
        espacos.append(aux)


def ff():
    # percorre lista principal
    for pos_programa in range (0, len(lista_principal)):
        # verifica se programa pode ser alocado no espaço
        for cont in range (0, len(espacos)):
            if espacos[cont][1] >= lista_principal[pos_programa][3]:
                if espacos[cont][1] >= lista_principal[pos_programa][3]:
                    aloca(pos_programa, espacos[cont][0])
                    return

        if memoria.count(0) > lista_principal[pos_programa][3]:
            lista_principal[pos_programa][5] += 1


def bf():
    # percorre lista principal e busca processo para alocar
    for pos_programa in range (0, len(lista_principal)):
        bf_check = False
        bf = -1
        # verifica se programa pode ser alocado no espaço
        for cont in range (0, len(espacos)):
            if espacos[cont][1] >= lista_principal[pos_programa][3]:
                if bf != -1:
                    if (espacos[cont][1] - lista_principal[pos_programa][3]) < espacos[bf][1]:
                        bf = cont
                else:
                    bf = cont
                    bf_check = True

        if bf_check:
            aloca(pos_programa, espacos[bf][0])
            bf_check = False
            bf = -1
            return

        if memoria.count(0) > lista_principal[pos_programa][3]:
            lista_principal[pos_programa][5] += 1


def wf():
    # percorre lista principal e busca processo para alocar
    for pos_programa in range (0, len(lista_principal)):
        wf_check = False
        wf = -1
        # verifica se programa pode ser alocado no espaço
        for cont in range (0, len(espacos)):
            if espacos[cont][1] >= lista_principal[pos_programa][3]:
                if wf != -1:
                    if (espacos[cont][1] - lista_principal[pos_programa][3]) > espacos[wf][1]:
                        wf = cont
                else:
                    wf = cont
                    wf_check = True

        if wf_check:
            aloca(pos_programa, espacos[wf][0])
            wf_check = False
            wf = -1
            return

        if memoria.count(0) > lista_principal[pos_programa][3]:
            lista_principal[pos_programa][5] += 1


def aloca(pos_programa, pos_memo):
    lista_principal[pos_programa][6] = pos_memo
    executando.append(lista_principal[pos_programa])
    lista_principal.pop(pos_programa)
    for i in range (0, executando[-1][3]):
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

    global ciclo
    ciclo += 1
    for programa in lista_principal:
        programa[4] += 1
    if len(executados) == len(lista_programas):
        # exporta parâmetros
        politica_graficos()
        return False
    return True


def abre_arquivo(tipo, politica): # abre ou fecha arquivos de saída
    global saida_ff, saida_bf, saida_wf

    # abre arquivos de saída
    if tipo:
        if politica == "Frist Fit":
            saida_ff = open("saida_ff.txt", "w+")
        elif politica == "Best Fit":
            saida_bf = open("saida_bf.txt", "w+")
        elif politica == "Worst Fit":
            saida_wf = open("saida_wf.txt", "w+")

    # fecha arquivos de saída
    else:
        if politica == "Frist Fit":
            saida_ff.close()
        elif politica == "Best Fit":
            saida_bf.close()
        elif politica == "Worst Fit":
            saida_wf.close()


def imprime(politica):
    global lista_principal, lista_principal, executados, executados, ciclo

    if politica == "Frist Fit":
        arquivo = saida_ff
    elif politica == "Best Fit":
        arquivo = saida_bf
    elif politica == "Worst Fit":
        arquivo = saida_wf

    uso_memo = int((memoria.count(1)/TAM_MEM)*100) # Uso Memo

    saida_log(ciclo, arquivo)
    saida_log(lista_principal, arquivo)
    saida_log(executando, arquivo)
    saida_log(executados, arquivo)
    saida_log(uso_memo, arquivo)


def saida_log(lista, arquivo):
    if isinstance(lista, list):
        for processo in lista:
            for dado in processo:
                arquivo.write(str(dado))
                arquivo.write(" ")
        arquivo.write("\n")
    else:
        if isinstance(lista, int):
            arquivo.write("{}\n".format(lista))
        else:
            arquivo.write("\n")


#================================= MAIN =================================#


# lista de políticas aplicadas
lista = ["Frist Fit", "Best Fit", "Worst Fit"]

global_graficos()

for politica in lista:

    inicio_graficos()
    abre_arquivo(True, politica)

    run = True
    inicializacao()

    while(run):
        checa_lista()
        mapeia_memoria()
        if checa_inicio_fila():
            if politica == "Frist Fit":
                ff()
            elif politica == "Best Fit":
                bf()
            elif politica == "Worst Fit":
                wf()
        executa()
        mapeia_memoria()

        parametros_graficos(lista_principal, memoria, espacos, executados, ciclo)
        imprime(politica)

        run = prox_ciclo()

    abre_arquivo(False, politica)

# plota gráficos
plota()
