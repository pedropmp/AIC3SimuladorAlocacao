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

    inteiros = []
    for programa in programas[:-1]:
        linha = []
        for dado in programa:
            linha.append(int(dado))
        inteiros.append(linha)
    return inteiros, ciclo


def checa_lista (lista_programas, ciclo):
	entra = []
	# percorre lista de programas e adiciona os que entram no ciclo a lista
	for i in range (0, len(lista_programas), 1):
    	if lista_programas[1] == ciclo:
        	entra.append(lista_programas)
	return(entra)

#def checa_inicio_fila_principal (lista_principal, ciclo):

fila_principal = []

programas, ciclo = inicializacao()
fila_principal += checa_lista(programas, ciclo)

print(programas, ciclo)
