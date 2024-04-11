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
            
    #Ordena os valores adjacentes dos vértices
    def ordena_lista_adjacencia(self):
        for lista in self.listaAdjacencia.values():
            lista.sort()
    
    #Imprime as listas armazenadas      
    def imprimir_lista(self):
        for vertice, adjacentes in self.listaAdjacencia.items():
            print(f'{vertice}: {adjacentes}')
    
    #Realiza o BFS      
    def busca_em_largura(self, vertice_inicial):
        
        #Cria o conjunto dos nos visitados 
        visitados = set()
        
        #Cria a fila para armazenar os vertices que ainda vão ser visitados 
        fila = deque([vertice_inicial])

        #Executa enquanto tiver vertices na fila 
        while fila:
            #Armazena o primeiro vertice da fila e exclui ele da fila 
            vertice = fila.popleft()
            
            #Verifica se o vertice foi visitado 
            if vertice not in visitados:
                #Imprime se o vertice não foi visitado 
                print(vertice, end=' ')
                #Adiciona ao conjunto de visitados
                visitados.add(vertice)
                
                #Explora os vertices vizinhos do vertice inicial 
                for vizinho in self.listaAdjacencia.get(vertice, []):
                    if vizinho not in visitados:
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

    #Realiza O DFS              
    def busca_em_profundidade(self, vertice_inicial):
        #Cria o conjunto dos nos visitados 
        visitados = set()
        
        #Cria um dicionario para armazenar a árvore gerada 
        arvore_dfs = {}
        
        #Chama a função auxiliar dfs_visit para iniciar a busca em profundidade
        self.dfs_visit(vertice_inicial, visitados, arvore_dfs)
        
        #Verifica se ainda existem vértices não visitados
        for vertice in self.listaAdjacencia.keys():
            if vertice not in visitados:
                self.dfs_visit(vertice, visitados, arvore_dfs)

        #Retorna a árvore DFS
        return arvore_dfs

    #Método para imprimir a árvore DFS
    def imprimir_arvore(self, arvore_dfs, vertice, nivel=0):
        if vertice not in arvore_dfs:
            return

        #Imprime o vértice atual
        print("  " * nivel + str(vertice))

        for filho in arvore_dfs[vertice]:
            #Chama recursivamente o método para imprimir o filho
            self.imprimir_arvore(arvore_dfs, filho, nivel = nivel+1)