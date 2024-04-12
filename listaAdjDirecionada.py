from collections import deque

contador = 0

class ListaAdjacenciaDirecionada:
    
    #Método construtor 
    def __init__(self):
        self.listaAdjacenciaDirecionada = {}

    def insere_listaAdjacenciaDirecionada(self, lista_de_pares):
        for v1, v2 in lista_de_pares:
            if v1 not in self.listaAdjacenciaDirecionada:
                self.listaAdjacenciaDirecionada[v1] = [v2]
            else:
                self.listaAdjacenciaDirecionada[v1].append(v2)
                self.listaAdjacenciaDirecionada[v1].sort()
        
        self.listaAdjacenciaDirecionada = {k: sorted(v) for k, v in sorted(self.listaAdjacenciaDirecionada.items())}
    
    def insere_subgrafo(self, qtd, lista_de_subgrafo):
        for subgrafo in lista_de_subgrafo[:qtd]:
            self.insere_listaAdjacenciaDirecionada(subgrafo)

    def imprimir_lista_direcionada(self):
        for vertice, adjacentes in self.listaAdjacenciaDirecionada.items():
            print(f"{vertice}: {adjacentes}")

    #Realiza a busca em largura (BFS)
    def busca_em_largura_direcionada(self):
        vertice_inicial = next(iter(self.listaAdjacenciaDirecionada))
        visitados = set()
        fila = deque([vertice_inicial])

        while fila:
            vertice = fila.popleft()

            if vertice not in visitados:
                print(vertice, end=' ')
                visitados.add(vertice)
                
                vizinhos_ordenados = sorted(self.listaAdjacenciaDirecionada.get(vertice, []))
                for vizinho in vizinhos_ordenados:
                    if vizinho not in visitados:
                        fila.append(vizinho)

    #Realiza a busca em profundidade (DFS)
    def busca_em_profundidade_direcionada(self, vertice_inicial, visitado=None):
        
        #lista de visitados começa zerada
        if visitado is None:
            #cria lista em estilo set
            visitado = set()
            #se a lista estiver zerada, o vertice inicial vai ser adicionado dentro da lista
        visitado.add(vertice_inicial)
        
        #vai printar o vertice inicial no momento
        print(vertice_inicial,contador)

        if vertice_inicial in self.listaAdjacenciaDirecionada:
            #faz uma iteração sobre os adjacentes ao verice inicial
            for vizinho in self.listaAdjacenciaDirecionada[vertice_inicial]:
                #reinicia a função dfs utilizando vizinho como se fosse o vertice inicial
                if vizinho not in visitado:   
                    self.dfs(vizinho, visitado)
                

        return visitado
    