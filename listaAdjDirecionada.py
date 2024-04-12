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
        return visitados

    #Realiza a busca em profundidade (DFS)
    def busca_em_profundidade_direcionada(self, vertice_inicial, visitado=None, pre_visita=None, pos_visita=None, contador=None):
        
        #lista de visitados começa zerada
        if visitado is None:
            #cria lista em estilo set e os dict de pre e pos visit
            visitado = set()
            pre_visita = {}
            pos_visita = {}
            contador = {'contador': 1}

            #se a lista estiver zerada, o vertice inicial vai ser adicionado dentro da lista vazia
        visitado.add(vertice_inicial)
        #atribui o contador ao vertice atual como pre visit
        pre_visita[vertice_inicial] = contador['contador']
        contador['contador'] += 1
        
        #vai printar o pre visit do vertice
        print(f"Pré-Visita de {vertice_inicial}: {pre_visita[vertice_inicial]}")

        if vertice_inicial in self.listaAdjacenciaDirecionada:
            #faz uma iteração sobre os adjacentes ao verice inicial
            for vizinho in self.listaAdjacenciaDirecionada[vertice_inicial]:
                #reinicia a função dfs utilizando vizinho como se fosse o vertice inicial
                if vizinho not in visitado:   
                    self.busca_em_profundidade_direcionada(vizinho, visitado, pre_visita, pos_visita, contador)
        
        #atribui o contador ao vertice atual como pos visit
        pos_visita[vertice_inicial] = contador['contador']
        contador['contador'] += 1

        #vai printar o pos visit do vertice
        print(f"Pós-Visita de {vertice_inicial}: {pos_visita[vertice_inicial]}")

        return visitado, pre_visita, pos_visita
    