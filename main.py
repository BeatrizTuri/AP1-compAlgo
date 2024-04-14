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

@app.route('/')
def home():
    return flask.render_template('home.html')
    
@app.route('/Direcionada')
def listaDirecionada():
    return flask.render_template('listaDirecionada.html')

@app.route('/NaoDirecionada')
def listaNaoDirecionada():
    return flask.render_template('listaNaoDirecionada.html')

@app.route('/insereListaDirecionada', methods=['POST'])
def insereListaDirecionada():
    lista_pares = flask.request.form.get("grafoInput")
    lista_formatada = []
    for i in range (len(lista_pares)):
        if lista_pares[i] == "(":
            lista_formatada.append((lista_pares[i+2], lista_pares[i+7]))
            
    lad.insere_listaAdjacenciaDirecionada(lista_formatada)

    return "Lista de adjacência direcionada inserida com sucesso!"

@app.route('/insereSubgrafoDirecionado', methods=['POST'])
def insereSubgrafoDirecionado():
    dados = flask.request.form
    qtd = dados.get("qtdInput")
    lista_pares = dados.get("subgrafoInput")
    lista_formatada = []
    for i in range (len(lista_pares)):
        if lista_pares[i] == "(":
            lista_formatada.append((lista_pares[i+2], lista_pares[i+7]))
    
    sd.insere_subgrafo_direcionado(qtd, lista_formatada)
    
    return "Subgrafo direcionado inserido com sucesso!"

@app.route('/exibeListaDirecionada', methods=['GET'])
def exibeListaDirecionada():
    grafo = lad.listaAdjacenciaDirecionada
    subgrafo = sd.listaAdjacenciaDirecionada

    print(grafo)
    print(subgrafo) 

    return flask.render_template('listaDirecionada.html', grafo=grafo, subgrafo=subgrafo)

@app.route('/insereListaNaoDirecionada', methods=['POST'])
def insereListaNaoDirecionada():
    lista_pares = flask.request.form.get("grafoInput")
    lista_formatada = []
    for i in range (len(lista_pares)):
        if lista_pares[i] == "(":
            lista_formatada.append((lista_pares[i+2], lista_pares[i+7]))
            
    la.insere_listaAdjacencia(lista_formatada)

    return "Lista de adjacência não direcionada inserida com sucesso!"

@app.route('/insereSubgrafoNaoDirecionado', methods=['POST'])   
def insereSubgrafoNaoDirecionado(): 
    dados = flask.request.form
    qtd = dados.get("qtdInput")
    lista_pares = dados.get("subgrafoInput")
    lista_formatada = []
    for i in range (len(lista_pares)):
        if lista_pares[i] == "(":
            lista_formatada.append((lista_pares[i+2], lista_pares[i+7]))
    
    s.insere_subgrafo(qtd, lista_formatada)
    
    return "Subgrafo não direcionado inserido com sucesso!"

@app.route('/exibeListaNaoDirecionada', methods=['GET'])
def exibeListaNaoDirecionada():
    grafo = la.listaAdjacencia
    subgrafo = s.listaAdjacencia

    print(grafo)
    print(subgrafo) 

    return flask.render_template('listaNaoDirecionada.html', grafo=grafo, subgrafo=subgrafo)

@app.route('/BuscaEmLarguraDirecionada', methods=['GET'])
def buscaEmLarguraDirecionada():
    grafo = lad.busca_em_largura_direcionada()
    subgrafo = sd.busca_em_largura_direcionada()
    
    return flask.render_template('algoritimoDirecionada.html', grafo=grafo, subgrafo=subgrafo)

@app.route('/BuscaEmProfundidadeDirecionada', methods=['GET'])
def buscaEmProfundidadeDirecionada():
    grafo = lad.busca_em_profundidade_direcionada()
    subgrafo = sd.busca_em_profundidade_direcionada()
    
    return flask.render_template('algoritimoDirecionada.html', grafo=grafo, subgrafo=subgrafo)

@app.route('/BuscaEmLargura', methods=['GET'])
def buscaEmLargura():   
    grafo = la.busca_em_largura()
    subgrafo = s.busca_em_largura()
    
    return flask.render_template('algoritimoNaoDirecionada.html', grafo=grafo, subgrafo=subgrafo)

@app.route('/BuscaEmProfundidade', methods=['GET'])
def buscaEmProfundidade():
    grafos = la.busca_em_profundidade()
    subgrafo = s.busca_em_profundidade()
    
    return flask.render_template('algoritimoNaoDirecionada.html', grafo=grafos, subgrafo=subgrafo)

if __name__ == "__main__":
    
    #Iniciando o servidor
    if not os.environ.get("WERKZEUG_RUN_MAIN"): #Executa apenas uma vez
        webbrowser.open("http://127.0.0.1:5000")

    app.run(debug=True)
    
    # # Criar uma instância da classe ListaAdjacencia
    # g1 = ListaAdjacencia()
    # g2 = ListaAdjacencia()
    # g3 = ListaAdjacencia()


    # # Outra maneira de inserir múltiplos pares usando insere_multiplos_pares
    # g2.insere_listaAdjacencia([("A", "B"), ("A", "E"), ("B", "C"), ("B", "E"), ("C", "F"), ("E", "F"), ("F", "I")])
    # g3.insere_subgrafo(1, [[("D", "H"), ("D", "G"), ("G", "H")]])
    # # Chamar a função imprimir_lista para verificar a lista de adjacência
    # # g1.imprimir_lista()
    
    # # g2.imprimir_lista()
    # # g3.imprimir_lista()
    
    # g2.busca_em_largura()
    # g3.busca_em_largura()
    
    # #g2.busca_em_profundidade()
    # # g3.busca_em_profundidade()
    # # g3.imprimir_dfs()
    
    # # g1.busca_em_largura(1)
    # # g2.busca_em_largura("A")
    
    # # arvore_dfs= g1.busca_em_profundidade(1)
    # # g1.imprimir_arvore(arvore_dfs, 1)
    
    # # arvore_dfs2 = g2.busca_em_profundidade("A")
    # # g2.imprimir_arvore(arvore_dfs2, "A")

    # # g3 = ListaAdjacenciaDirecionada()
    # g4 = ListaAdjacenciaDirecionada()
    # # g5 = ListaAdjacencia()
    
    # # g3.insere_um_par(1, 2)
    # # g3.insere_um_par(1, 5)
    # # g3.insere_um_par(2, 5)
    # # g3.insere_um_par(2, 3)
    # # g3.insere_um_par(2, 4)
    # # g3.insere_um_par(5, 4)
    # # g3.insere_um_par(4, 3)


    # #g4.insere_listaAdjacenciaDirecionada([("A", "B"), ("A", "F"), ("B", "C"), ("B", "E"), ("C", "D"), ("E", "D"), ("E", "G"), ("D", "H"), ("D", "B"), ("G", "F"), ("H", "G"), ("F", "G"), ("F", "E")])
    # # g3.imprimir_lista()
    # #g4.imprimir_lista_direcionada()

    # # print("Busca de profundidade")
    
    # g4.busca_em_profundidade_direcionada()


''' 
chat gpt falou para colocar essas funções, mas nao tenho certeza pq ta usando jsonify
'''

#     from flask import request, jsonify

# @app.route('/insere_lista_direcionada', methods=['POST'])
# def insere_lista_direcionada():
#     dados = request.json
#     lista_pares = dados['listaPares']
#     g4.insere_listaAdjacenciaDirecionada(lista_pares)
#     return "Lista de adjacência direcionada inserida com sucesso!"

# @app.route('/insere_subgrafo_direcionado', methods=['POST'])
# def insere_subgrafo_direcionado():
#     dados = request.json
#     lista_pares = dados['listaPares']
#     g4.insere_subgrafo_direcionado(1, lista_pares)
#     return "Subgrafo direcionado inserido com sucesso!"