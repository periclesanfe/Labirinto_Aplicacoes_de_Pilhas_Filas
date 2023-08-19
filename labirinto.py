from collections import deque

from random import randint

livre = ' '
ocupado = '#'
parede  = '#'
andou = '@'

linhas = 7
colunas = 15

inicio = (1,0)
fim = (linhas-2,colunas-1)

def gera_lab(m,n):
	lab = [([parede]*n)]
	for i in range(1,m-1):
		linha = [livre] * n
		for j in range(n):
			if randint(0,7) in [0,1]:
				linha[j] = ocupado
			if j in [0,n-1]:
				linha[j] = parede
		lab.append(linha)
	lab.append([parede]*n)
	lab[inicio[0]][inicio[1]] = livre
	lab[fim[0]][fim[1]] = livre
	return lab

def eh_possivel_sair(lab):
    fila = deque([inicio])
    visitados = set()

    while fila:
        celula_atual = fila.popleft()
        if celula_atual == fim:
            return True

        visitados.add(celula_atual)

        linha, coluna = celula_atual
        vizinhos = [(linha-1, coluna), (linha+1, coluna), (linha, coluna-1), (linha, coluna+1)]

        for vizinho in vizinhos:
            linha_vizinho, coluna_vizinho = vizinho
            if 0 <= linha_vizinho < len(lab) and 0 <= coluna_vizinho < len(lab[0]) and lab[linha_vizinho][coluna_vizinho] == livre and vizinho not in visitados:
                fila.append(vizinho)

    return False


def print_lab(lab):
	for i in lab:
		print("".join(i))


if __name__ == '__main__':
    labirinto = gera_lab(linhas, colunas)
    print_lab(labirinto)
    
    if eh_possivel_sair(labirinto):
        print("É possível sair do labirinto.")
    else:
        print("Não é possível sair do labirinto.")
