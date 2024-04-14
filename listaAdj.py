from collections import deque

class ListaAdjacencia:

    #Método construtor
    def __init__(self):
        self.listaAdjacencia = {}
        self.pre_visita = {}
        self.pos_visita = {}
        self.resultado_dfs = {}


    #Método para inserir uma lista de pares
    def insere_listaAdjacencia(self, lista_de_pares):
        
        for v1, v2 in lista_de_pares:
            #Se o vértice v1 não está na lista de adjacência, cria uma lista vazia
            if v1 not in self.listaAdjacencia:
                self.listaAdjacencia[v1] = [v2]
            else:
                #Adiciona o vértice v2 à lista de adjacência do vértice v1
                self.listaAdjacencia[v1].append(v2)
                #Ordena a lista de adjacência do vértice v1
                self.listaAdjacencia[v1].sort()

            #Se o vértice v2 não está na lista de adjacência, cria uma lista vazia
            if v2 not in self.listaAdjacencia:
                self.listaAdjacencia[v2] = [v1]
            else:
                #Adiciona o vértice v1 à lista de adjacência do vértice v2
                self.listaAdjacencia[v2].append(v1)
                #Ordena a lista de adjacência do vértice v2
                self.listaAdjacencia[v2].sort()
                
        #Ordena a lista de adjacência
        self.listaAdjacencia = {k: sorted(v) for k, v in sorted(self.listaAdjacencia.items())}

    #Método para identificar a quantidade de subgrafos a serem inseridos e armazena-los
    def insere_subgrafo(self, qtd, lista_de_subgrafos):
        for _ in qtd:
            self.insere_listaAdjacencia(lista_de_subgrafos)
    
    #Imprime as listas armazenadas      
    def imprimir_lista(self):
        for vertice, adjacentes in self.listaAdjacencia.items():
            print(f'{vertice}: {adjacentes}')
            
    #Realiza a busca em largura (BFS)        
    def busca_em_largura(self):
        
        #Escolhe o primeiro vértice como inicial
        vertice_inicial = next(iter(self.listaAdjacencia))  
        #Cria um conjunto para armazenar os vértices visitados
        visitados = set()
        #Cria uma fila para armazenar os vértices a serem visitados
        fila = deque([vertice_inicial])

        resultados = []

        #Enquanto a fila não estiver vazia
        while fila:
            #Remove o primeiro vértice da fila
            vertice = fila.popleft()
            #Se o vértice não foi visitado
            if vertice not in visitados:
                resultados.append(vertice)
                #Adiciona o vértice aos visitados
                visitados.add(vertice)
                
                #Ordena os vizinhos alfabeticamente e numericamente
                vizinhos_ordenados = sorted(self.listaAdjacencia.get(vertice, []))             
                #Adiciona os vértices vizinhos do vértice atual à fila
                for vizinho in vizinhos_ordenados:
                    #Se o vizinho não foi visitado, adiciona à fila
                    if vizinho not in visitados:
                        #Adiciona o vizinho à fila
                        fila.append(vizinho)
        return resultados

    #Algoritmo que realiza a busca em profundidade (DFS)
    def dfs_visit(self, vertice, visitados, arvore_dfs, contador):

        #Adiciona o vértice inicial ao conjunto de vértices visitados
        visitados.add(vertice)

        #Inicializa o atributo de pre-visita ao vértice atual
        self.pre_visita[vertice] = contador['contador']
        contador['contador'] += 1

        #Inicializa uma lista vazia no dicionário para armazenar os filhos do vértice atual
        arvore_dfs[vertice] = []

        #Itera sobre os vizinhos vértice atual
        for vizinho in self.listaAdjacencia.get(vertice, []):
            #Verifica se o vizinho não foi visitado
            if vizinho not in visitados:

                #Adiciona vizinho na lista de filhos do vértice atual
                arvore_dfs[vertice].append(vizinho)
                #Chamada RECURSIVA da função
                self.dfs_visit(vizinho, visitados, arvore_dfs, contador)
        #Inicializa o atributo pos-visit a partir do valor do contador atual
        self.pos_visita[vertice] = contador['contador']
        contador['contador'] += 1

    #Método que inicia o DFS a partir dos vértices não visitados no grafo
    def busca_em_profundidade(self):
        #Conjunto que mantém o regsitro dos vértices já vistados
        visitados = set()
        #Dicionário de chave única para atribuir o tempo de visita
        contador = {'contador': 1}
        #Dicionário para árvore resultante
        arvore_dfs = {}

        #Itera pelos vértices presentes na lista de adjacência armazenada
        for vertice in self.listaAdjacencia.keys():
            #verifica se o vértice não foi visitado
            if vertice not in visitados:
                #Chama o DFS
                self.dfs_visit(vertice, visitados, arvore_dfs, contador)

        #Armazena o contador de pré-visita e pós-visita no formato desejado
        for vertice in self.listaAdjacencia.keys():
            self.resultado_dfs[vertice] = [self.pre_visita[vertice], self.pos_visita[vertice]]
        
        #Retorna o resultado do DFS
        return self.resultado_dfs
                
    #Retorna o pre-visit e pos-visit para cada vértice
    def imprimir_dfs(self):
        print("\nTempos de Pré-Visita e Pós-Visita:")
        #Itera sobre todos os vértices do grafo
        for vertice in self.listaAdjacencia.keys():
            #Imprime o tempo de pré e pós visita para cada vértice
            return(f"{vertice}: ({self.pre_visita[vertice]}, {self.pos_visita[vertice]})")
