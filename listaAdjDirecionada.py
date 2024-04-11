from collections import deque

contador = 0

class ListaAdjacenciaDirecionada:
    
    #Método construtor 
    def __init__(self):
        self.listaAdjacenciaDirecionada = {}
    
    def insere_um_par(self, v1, v2):
        if v1 not in self.listaAdjacenciaDirecionada:
            self.listaAdjacenciaDirecionada[v1] = []
        self.listaAdjacenciaDirecionada[v1].append(v2)
    
    def insere_multiplos_pares(self,lista_de_pares):
        for v1, v2 in lista_de_pares:
            self.insere_um_par(v1,v2)
    
    def imprimir_lista(self):
        for vertice, adjacentes in self.listaAdjacenciaDirecionada.items():
            print(f"{vertice}: {adjacentes}")

    #BFS
    def busca_em_largura(self, vertice_inicial):
        visitados = set()
        fila = deque([vertice_inicial])

        while fila:
            vertice = fila.popleft()

            if vertice not in visitados:
                print(vertice, end=' ')
                visitados.add(vertice)
                    
                for vizinho in self.listaAdjacenciaDirecionada.get(vertice, []):
                    if vizinho not in visitados:
                        fila.append(vizinho)

   
    def dfs(self, vertice_inicial, visitado=None):
        
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
    