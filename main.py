from MemConfig import TAM_BLOCO, TAM_MEM

def inicializacao():
    global executados, executandos, lista_principal, memoria, ciclo, inteiros
    
    # cria lista de zeros para representar memoria
    memoria = [0] * int(TAM_MEM / TAM_BLOCO)

    # abre arquivo de entrada
    arq = open("entrada", "r")
    # separa o arquivo por linhas
    conteudo = arq.read().split('\n')
    # separa as linhas em posicoes acessiveis ID, Tchegada, Tam, Texecucao
    programas = []
    for linha in conteudo:
        programas.append(linha.split(' '))
    ciclo = 0
    # torna a lista de entrada uma lista de inteiros
    inteiros = []
    for programa in programas[:-1]:
        linha = []
        for dado in programa:
            linha.append(int(dado))
        inteiros.append(linha)
        
        
def checa_lista():
    # percorre lista de programas e adiciona os que entram no ciclo a lista
    for i in range(0, len(lista_programas)):
        if lista_programas[1] == ciclo:
            fila_principal.append(lista_programas)
            fila_principal[-1].append(0)
            fila_principal[-1].append(0)


def checa_inicio_fila_principal ():
    # checa se há programas na lista principal
    if len(lista_principal) != 0:
        return (True)
    else:
        return(False)


def ff ():
    pos_memo, qnt = 0
    # percorre lista principal
    for pos_programa in range (0, len(lista_principal)):
        # percorre memória buscando primeiro espaço para alocar processo
        for cont in range (0, len(memoria)):
            if memoria[cont] == 0:
                if qnt != 0:
                    qnt += 1
                else:
                    pos_memo = cont
                    qnt = 1
                # verifica se programa pode ser alocado no espaço
                if qnt == lista_principal[pos_programa][prog[3]]:
                    aloca(pos_programa, pos_memo)
            else:
                qnt = 0
        lista_principal[pos_programa][5] += 1


def aloca (pos_programa, pos_memo):
    lista_principal[pos_programa].append(pos_memo)
    executando.append(lista_principal[pos_programa])
    lista_principal.pop(pos_programa)
    for i in range (0, executando[-1][3]):
        memoria[pos + i] = 1


def executa ():
    for i in range (0, len(executando)):
        executando[i][3] -= 1
        if executando[i][3] == 0:
            for j in range (0, lista_principal[pos_programa][3]):
                memoria[lista_principal[pos_programa][4]+j] = 0
            executado.append(executando[i])
            executando.pop(i)
    for i in range (0, len(lista_principal)):
        lista_principal[i][4] += 1

            
            
