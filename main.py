import MemConfig

def inicializacao():
    # abre arquivo de entrada
    arq = open("entrada.txt", "r")
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
    # cria lista de zeros para representar memoria
    return inteiros, ciclo


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

def ff (lista_principal, memoria):
    pos, qnt = 0
    # percorre lista principal
    for processo in lista_principal:
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

        return(False, 0)

# def checa_inicio_fila_principal (lista_principal, ciclo):

fila_principal = []

programas, ciclo = inicializacao()
fila_principal += checa_lista(programas, ciclo)

print(programas, ciclo)
print(tamanho)
