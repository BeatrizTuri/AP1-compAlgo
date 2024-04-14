from collections import deque



class ListaAdjacenciaDirecionada:
    
    #Método construtor 
    def __init__(self):
        self.listaAdjacenciaDirecionada = {}
        self.pre_visita = {}
        self.pos_visita = {}
        self.resultado_dfs = {}
        self.contador = 1

    #Método para inserir uma lista de pares
    def insere_listaAdjacenciaDirecionada(self, lista_de_pares):
        #Para cada par de vértices na lista de pares
        for v1, v2 in lista_de_pares:
            #Se o vértice v1 não está na lista de adjacência, cria uma lista vazia
            if v1 not in self.listaAdjacenciaDirecionada:
                #Adiciona o vértice v2 à lista de adjacência do vértice v1
                self.listaAdjacenciaDirecionada[v1] = [v2]
            #Se o vértice v1 já está na lista de adjacência
            else:
                #Adiciona o vértice v2 à lista de adjacência do vértice v1
                self.listaAdjacenciaDirecionada[v1].append(v2)
                #Ordena a lista de adjacência do vértice v1
                self.listaAdjacenciaDirecionada[v1].sort()
        
        #Ordena a lista de adjacência
        self.listaAdjacenciaDirecionada = {k: sorted(v) for k, v in sorted(self.listaAdjacenciaDirecionada.items())}
    
    #Método para identificar a quantidade de subgrafos a serem inseridos e armazena-los
    def insere_subgrafo_direcionado(self, qtd, lista_de_subgrafo):
        for _ in qtd:
            self.insere_listaAdjacenciaDirecionada(lista_de_subgrafo)

    #Imprime as listas armazenadas
    def imprimir_lista_direcionada(self):
        #Para cada vértice e seus adjacentes na lista de adjacência
        for vertice, adjacentes in self.listaAdjacenciaDirecionada.items():
            print(f"{vertice}: {adjacentes}")

    #Realiza a busca em largura (BFS)
    def busca_em_largura_direcionada(self):
        #Cria um conjunto para armazenar os vértices visitados
        visitados = set()
        #Escolhe o primeiro vértice como inicial
        vertice_inicial = next(iter(self.listaAdjacenciaDirecionada))
        #Cria uma fila para armazenar os vértices a serem visitados
        fila = deque([vertice_inicial])
        #Cria uma lista para armazenar os resultados
        resultados = []

        #Enquanto a fila não estiver vazia
        while fila:
            #Remove o primeiro vértice da fila
            vertice = fila.popleft()

            #Se o vértice não está no conjunto de visitados
            if vertice not in visitados:
                #Adiciona o vértice à lista de resultados e ao conjunto de visitados
                resultados.append(vertice)
                #Marca o vértice como visitado
                visitados.add(vertice)

                #Para cada vértice vizinho do vértice atual
                vizinhos_ordenados = sorted(self.listaAdjacenciaDirecionada.get(vertice, []))
                #Adiciona os vizinhos à fila
                fila.extend(vizinhos_ordenados)

        #Retorna os resultados
        return resultados

    #Realiza a busca em profundidade (DFS)
    def dfs_visit(self, vertice, visitados):
        #Adiciona o vértice ao conjunto de visitados
        visitados.add(vertice)
        
        #Marca o contador de pré-visita
        self.pre_visita[vertice] = self.contador
        self.contador += 1

        #Para cada vértice vizinho do vértice atual
        if vertice in self.listaAdjacenciaDirecionada:
            #Se o vizinho não foi visitado, chama a função recursivamente
            for vizinho in self.listaAdjacenciaDirecionada[vertice]:
                #Se o vizinho não foi visitado
                if vizinho not in visitados:
                    #Chama a função recursivamente
                    self.dfs_visit(vizinho, visitados)
        
        #Marca o contador de pós-visita
        self.pos_visita[vertice] = self.contador
        self.contador += 1

    #Método que inicia o DFS a partir dos vértices não visitados no grafo
    def busca_em_profundidade_direcionada(self):
        #Cria um conjunto para armazenar os vértices visitados
        visitados = set()
        #Inicializa o contador
        self.contador = 1
        
        #Para cada vértice na lista de adjacência
        for vertice in self.listaAdjacenciaDirecionada.keys():
            #Se o vértice não foi visitado
            if vertice not in visitados:
                #Chama a função de visita
                self.dfs_visit(vertice, visitados)
        
        #Cria um dicionário para armazenar os resultados
        for vertice in self.listaAdjacenciaDirecionada.keys():
            #Adiciona o vértice e suas pré e pós-visitas ao dicionário
            self.resultado_dfs[vertice] = [self.pre_visita[vertice], self.pos_visita[vertice]]
        
        #Retorna o dicionário com os resultados
        return self.resultado_dfs
    
    