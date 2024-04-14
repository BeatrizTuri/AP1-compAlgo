import os
import webbrowser
from listaAdj import ListaAdjacencia
from listaAdjDirecionada import ListaAdjacenciaDirecionada
import flask

app = flask.Flask(__name__)
lad = ListaAdjacenciaDirecionada()
la = ListaAdjacencia()
sd = ListaAdjacenciaDirecionada()
s = ListaAdjacencia()

#Rotas para as páginas
@app.route('/')
def home():
    return flask.render_template('home.html')

#Rotas para as páginas de inserção de listas   
@app.route('/Direcionada')
def listaDirecionada():
    return flask.render_template('listaDirecionada.html')

#Rotas para as páginas de inserção de subgrafos
@app.route('/NaoDirecionada')
def listaNaoDirecionada():
    return flask.render_template('listaNaoDirecionada.html')

#Rotas para as páginas de exibição de listas
@app.route('/insereListaDirecionada', methods=['POST'])
def insereListaDirecionada():
    lista_pares = flask.request.form.get("grafoInput")
    lista_formatada = []
    for i in range (len(lista_pares)):
        if lista_pares[i] == "(":
            lista_formatada.append((lista_pares[i+2], lista_pares[i+7]))
            
    lad.insere_listaAdjacenciaDirecionada(lista_formatada)

    return "Lista de adjacência direcionada inserida com sucesso!"

#Rotas para as páginas de exibição de subgrafos
@app.route('/insereSubgrafoDirecionado', methods=['POST'])
def insereSubgrafoDirecionado():
    dados = flask.request.form
    qtd = dados.get("qtdInput")
    lista_pares = dados.get("subgrafoInput")
    lista_formatada = []
    for i in range (len(lista_pares)):
        if lista_pares[i] == "(":
            lista_formatada.append((lista_pares[i+2], lista_pares[i+7]))
    
    lad.insere_subgrafo_direcionado(qtd, lista_formatada)
    sd.insere_subgrafo_direcionado(qtd, lista_formatada)
        
    return "Subgrafo direcionado inserido com sucesso!"

#Rotas para as páginas de exibição de listas
@app.route('/exibeListaDirecionada', methods=['GET'])
def exibeListaDirecionada():
    grafo = lad.listaAdjacenciaDirecionada

    return flask.render_template('listaDirecionada.html', grafo=grafo)

#Rotas para as páginas de exibição de listas
@app.route('/insereListaNaoDirecionada', methods=['POST'])
def insereListaNaoDirecionada():
    lista_pares = flask.request.form.get("grafoInput")
    lista_formatada = []
    for i in range (len(lista_pares)):
        if lista_pares[i] == "(":
            lista_formatada.append((lista_pares[i+2], lista_pares[i+7]))
            
    la.insere_listaAdjacencia(lista_formatada)

    return "Lista de adjacência não direcionada inserida com sucesso!"

#Rotas para as páginas de exibição de subgrafos
@app.route('/insereSubgrafoNaoDirecionado', methods=['POST'])   
def insereSubgrafoNaoDirecionado(): 
    dados = flask.request.form
    qtd = dados.get("qtdInput")
    lista_pares = dados.get("subgrafoInput")
    lista_formatada = []
    for i in range (len(lista_pares)):
        if lista_pares[i] == "(":
            lista_formatada.append((lista_pares[i+2], lista_pares[i+7]))
    
    la.insere_subgrafo(qtd, lista_formatada)
    s.insere_subgrafo(qtd, lista_formatada)
    
    return "Subgrafo não direcionado inserido com sucesso!"

#Rotas para as páginas de exibição de listas
@app.route('/exibeListaNaoDirecionada', methods=['GET'])
def exibeListaNaoDirecionada():
    grafo = la.listaAdjacencia

    return flask.render_template('listaNaoDirecionada.html', grafo=grafo)

#Rotas para os algoritmos de busca BFS
@app.route('/BuscaEmLarguraDirecionada', methods=['GET'])
def buscaEmLarguraDirecionada():
    grafo = {}
    subgrafo = {}
    if lad.listaAdjacenciaDirecionada != {}:
        grafo = lad.busca_em_largura_direcionada()
    if sd.listaAdjacenciaDirecionada != {}:
        subgrafo = sd.busca_em_largura_direcionada()
    
    return flask.render_template('algoritmoDirecionadaBFS.html', grafoBFS=grafo, subgrafoBFS=subgrafo)

#Rotas para os algoritmos de busca DFS
@app.route('/BuscaEmProfundidadeDirecionada', methods=['GET'])
def buscaEmProfundidadeDirecionada():
    grafo = {}
    grafo = lad.busca_em_profundidade_direcionada()
    
    return flask.render_template('algoritmoDirecionadaDFS.html', grafoDFS=grafo)

#Rotas para os algoritmos de busca BFS
@app.route('/BuscaEmLargura', methods=['GET'])
def buscaEmLargura():  
    grafo = {} 
    subgrafo = {}
    if la.listaAdjacencia != {}:
        grafo = la.busca_em_largura()
    if s.listaAdjacencia != {}:
        subgrafo = s.busca_em_largura()
    
    return flask.render_template('algoritmoNaoDirecionadaBFS.html', grafoBFS=grafo, subgrafoBFS=subgrafo)

#Rotas para os algoritmos de busca DFS
@app.route('/BuscaEmProfundidade', methods=['GET'])
def buscaEmProfundidade():
    grafo = {}
    grafo = la.busca_em_profundidade()

    return flask.render_template('algoritmoNaoDirecionadaDFS.html', grafoDFS=grafo)

if __name__ == "__main__":
    
    # #Iniciando o servidor
    if not os.environ.get("WERKZEUG_RUN_MAIN"): #Executa apenas uma vez
        webbrowser.open("http://127.0.0.1:5000")

    app.run(debug=True)
    
    # g1 = ListaAdjacenciaDirecionada()
    # g2 = ListaAdjacencia()
    # g3 = ListaAdjacencia()
    
    # # # g1.insere_listaAdjacenciaDirecionada([('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'C'), ('E', 'F'), ('F', 'C')])
    
    # # # g1.busca_em_largura_direcionada()

    # g2.insere_listaAdjacencia([("A", "B"), ("A", "E"), ("B", "C"), ("B", "E"), ("C", "F"), ("E", "F"), ("F", "I")])
    
    # g3.insere_subgrafo('1', [("D", "H"), ("D", "G"), ("G", "H")])
    
    # print(g2.busca_em_profundidade())
    
    # print(g2.busca_em_largura())