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
        
        
def checa_lista(lista_programas, ciclo):
    entra = []
    # percorre lista de programas e adiciona os que entram no ciclo a lista
    for i in range(0, len(lista_programas), 1):
        if lista_programas[1] == ciclo:
            entra.append(lista_programas)
    return (entra)

def checa_inicio_fila_principal (lista_principal):
    if len(lista_principal) != 0:
        return (0)
    else:
        return(1)

'''def ff (lista_principal, memoria):
    pos, qnt = 0
    aux = [0,0]
    vazio = []
    # percorre lista principal

    for cont in range (0, len(memoria)):
        if memoria[cont] == 0:
            if aux[1] == 0:
                aux[0] = cont
                aux[1] = 1
            else:
                aux[1] += 1
        else:
            if aux[1] != 0:
                vazio.append(aux)

    for prog in range (0, len(lista_principal)):
        for espaco in

    for cont in range (0, len(memoria)):
        # verifica se espaço da memória x está vazio
        if memoria[cont] == 0:
            pos = cont
            qnt += 1
            # verifica se programa pode ser alocado
            if qnt == lista_principal:
                return(True, pos, qnt)

        else:
            pos = cont
            qnt = 0

    return(False, 0)'''

def aloca (lista_principal, executando, pos_programa, pos_memo, memoria):
    lista_principal[pos_programa].append(pos_memo)
    executando.append(lista_principal[pos_programa])
    lista_principal.pop(pos)
    for i in range (0, executando[-1][3]):
        memoria[pos + i] = 1

def executa (executando):
    for i in range (0, len(executando)):
        executando[i][3] -= 1
        if executando[i][3] == 0:
            for j in range (0, lista_principal[pos_programa][3]):
                memoria[lista_principal[pos_programa][4]+j] = 0
            executado.append(executando[i])
            executando.pop(i)
            
            
