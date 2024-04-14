from collections import deque



class ListaAdjacenciaDirecionada:
    
    #Método construtor 
    def __init__(self):
        self.listaAdjacenciaDirecionada = {}
        self.pre_visita = {}
        self.pos_visita = {}
        self.resultado_dfs = {}
        self.contador = 1

    def insere_listaAdjacenciaDirecionada(self, lista_de_pares):
        for v1, v2 in lista_de_pares:
            if v1 not in self.listaAdjacenciaDirecionada:
                self.listaAdjacenciaDirecionada[v1] = [v2]
            else:
                self.listaAdjacenciaDirecionada[v1].append(v2)
                self.listaAdjacenciaDirecionada[v1].sort()
        
        self.listaAdjacenciaDirecionada = {k: sorted(v) for k, v in sorted(self.listaAdjacenciaDirecionada.items())}
    
    def insere_subgrafo_direcionado(self, qtd, lista_de_subgrafo):
        for _ in qtd:
            self.insere_listaAdjacenciaDirecionada(lista_de_subgrafo)

    def imprimir_lista_direcionada(self):
        for vertice, adjacentes in self.listaAdjacenciaDirecionada.items():
            print(f"{vertice}: {adjacentes}")

    #Realiza a busca em largura (BFS)
    def busca_em_largura_direcionada(self):
        visitados = set()
        print("lista adjacencia: " + str(self.listaAdjacenciaDirecionada))
        vertice_inicial = next(iter(self.listaAdjacenciaDirecionada))
        print("vertice inical: " + str(vertice_inicial))
        fila = deque([vertice_inicial])
        resultados = []

        while fila:
            vertice = fila.popleft()

            if vertice not in visitados:
                resultados.append(vertice)
                visitados.add(vertice)

                vizinhos_ordenados = sorted(self.listaAdjacenciaDirecionada.get(vertice, []))
                fila.extend(vizinhos_ordenados)

        return resultados

    #Realiza a busca em profundidade (DFS)
    def dfs_visit(self, vertice, visitados):
        visitados.add(vertice)
        
        self.pre_visita[vertice] = self.contador
        # print(f"Pré-Visita de {vertice}: {self.pre_visita[vertice]}")  # Comentei essa linha
        
        self.contador += 1

        if vertice in self.listaAdjacenciaDirecionada:
            for vizinho in self.listaAdjacenciaDirecionada[vertice]:
                if vizinho not in visitados:
                    self.dfs_visit(vizinho, visitados)
        
        self.pos_visita[vertice] = self.contador
        # print(f"Pós-Visita de {vertice}: {self.pos_visita[vertice]}")  # Comentei essa linha
        
        self.contador += 1

    # Método que inicia o DFS a partir dos vértices não visitados no grafo
    def busca_em_profundidade_direcionada(self):
        visitados = set()
        self.contador = 1
        
        for vertice in self.listaAdjacenciaDirecionada.keys():
            if vertice not in visitados:
                self.dfs_visit(vertice, visitados)
        
        # armazena o contador de pré-visita e pós-visita no formato desejado
        for vertice in self.listaAdjacenciaDirecionada.keys():
            self.resultado_dfs[vertice] = [self.pre_visita[vertice], self.pos_visita[vertice]]
        
        return self.resultado_dfs
    
    