from collections import deque


class ListaAdjacencia:

    #Método construtor 
    def __init__(self):
        self.listaAdjacencia = {}
    
    #Insere apenas um par de arestas ao ser chamada
    def insere_um_par(self, v1, v2):
        if v1 not in self.listaAdjacencia:
            self.listaAdjacencia[v1] = [v2]
        else:
            self.listaAdjacencia[v1].append(v2)

        if v2 not in self.listaAdjacencia:
            self.listaAdjacencia[v2] = [v1]
        else:
            self.listaAdjacencia[v2].append(v1)
    
    #Insere uma lista contendo vários pares de aresta
    def insere_multiplos_pares(self, lista_de_pares):
        for v1, v2 in lista_de_pares:
            self.insere_um_par(v1, v2)
    
    listaAdjacencia().sort

    #Imprime a lista que foi armazenada
    def imprimir_lista(self):
        for vertice, adjacentes in self.listaAdjacencia.items():
            print(f'{vertice}: {adjacentes}')
    
    #Realiza o BFS      
    def busca_em_largura(self, vertice_inicial):
        visitados = set()
        fila = deque([vertice_inicial])

        while fila:
            vertice = fila.popleft()
            if vertice not in visitados:
                print(vertice, end=' ')
                visitados.add(vertice)
                for vizinho in self.listaAdjacencia.get(vertice, []):
                    if vizinho not in visitados:
                        fila.append(vizinho)


#o que esta retornando no terminal 
# 1: [2, 5]
# 2: [1, 5, 3, 4]
# 5: [1, 2, 4]
# 3: [2, 4]
# 4: [2, 5, 3]