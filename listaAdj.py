from collections import deque

class ListaAdjacencia:

    #Método construtor 
    def __init__(self):
        self.listaAdjacencia = {}
    
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
        for subgrafo in lista_de_subgrafos[:qtd]:
            self.insere_listaAdjacencia(subgrafo)
    
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

        #Enquanto a fila não estiver vazia
        while fila:
            #Remove o primeiro vértice da fila
            vertice = fila.popleft()
            #Se o vértice não foi visitado
            if vertice not in visitados:
                #Imprime o vértice
                print(vertice, end=' ')
                #Adiciona o vértice aos visitados
                visitados.add(vertice)
                
                # Ordena os vizinhos alfabeticamente e numericamente
                vizinhos_ordenados = sorted(self.listaAdjacencia.get(vertice, []))             
                #Adiciona os vértices vizinhos do vértice atual à fila
                for vizinho in vizinhos_ordenados:
                    #Se o vizinho não foi visitado, adiciona à fila
                    if vizinho not in visitados:
                        #Adiciona o vizinho à fila
                        fila.append(vizinho)
      
    #Auxilia o DFS
    def dfs_visit(self, vertice, visitados, arvore_dfs):
        #Adiciona o vértice atual aos visitados
        visitados.add(vertice)
        
        #Inicializa a lista de vértices filhos do vértice atual na árvore DFS
        arvore_dfs[vertice] = []
        
        #Explora os vértices vizinhos do vértice atual
        for vizinho in self.listaAdjacencia.get(vertice, []):
            
            if vizinho not in visitados:
                #Adiciona o vizinho como filho do vértice atual na árvore DFS e chama recursivamente dfs_visit
                arvore_dfs[vertice].append(vizinho)
                self.dfs_visit(vizinho, visitados, arvore_dfs)

    #Método para imprimir a árvore DFS
    def imprimir_arvore(self, arvore_dfs, vertice, nivel=0):
        if vertice not in arvore_dfs:
            return

        #Imprime o vértice atual
        print("  " * nivel + str(vertice))

        for filho in arvore_dfs[vertice]:
            #Chama recursivamente o método para imprimir o filho
            self.imprimir_arvore(arvore_dfs, filho, nivel = nivel+1)
            
    #Realiza O DFS              
    def busca_em_profundidade(self):
        
        #Cria o conjunto dos nos visitados 
        visitados = set()
        #Cria um dicionario para armazenar a árvore gerada 
        arvore_dfs = {}
        
        #Para cada vértice na lista de adjacência
        for vertice in self.listaAdjacencia.keys():
            #Se o vértice não foi visitado, chama o método dfs_visit
            if vertice not in visitados:
                self.dfs_visit(vertice, visitados, arvore_dfs)

        #Retorna a árvore DFS
        return self.imprimir_arvore(arvore_dfs, next(iter(self.listaAdjacencia)))
