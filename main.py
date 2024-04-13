import os
import webbrowser
from listaAdj import ListaAdjacencia
from listaAdjDirecionada import ListaAdjacenciaDirecionada
import flask

app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template('home.html')
    
@app.route('/Direcionada')
def listaDirecionada():
    return flask.render_template('listaDirecionada.html')

@app.route('/NaoDirecionada')
def listaNaoDirecionada():
    return flask.render_template('listaNaoDirecionada.html')

@app.route('/BuscaEmLarguraDirecionada')
def buscaEmLarguraDirecionada():
    return flask.render_template('buscaEmLarguraDirecionada.html')

@app.route('/BuscaEmLargura')
def buscaEmLargura():
    return flask.render_template('buscaEmLargura.html')

@app.route('/BuscaEmProfundidadeDirecionada')
def buscaEmProfundidadeDirecionada():
    return flask.render_template('buscaEmProfundidadeDirecionada.html')

@app.route('/BuscaEmProfundidade')
def buscaEmProfundidade():
    return flask.render_template('buscaEmProfundidade.html')
    

if __name__ == "__main__":
    
    #Iniciando o servidor
    if not os.environ.get("WERKZEUG_RUN_MAIN"): #Executa apenas uma vez
        webbrowser.open("http://127.0.0.1:5000")

    app.run(debug=True)
    
    # Criar uma instância da classe ListaAdjacencia
    g1 = ListaAdjacencia()
    g2 = ListaAdjacencia()
    g3 = ListaAdjacencia()


    # Outra maneira de inserir múltiplos pares usando insere_multiplos_pares
    g2.insere_listaAdjacencia([("A", "B"), ("A", "E"), ("B", "C"), ("B", "E"), ("C", "F"), ("E", "F"), ("F", "I")])
    g3.insere_subgrafo(1, [[("D", "H"), ("D", "G"), ("G", "H")]])
    # Chamar a função imprimir_lista para verificar a lista de adjacência
    # g1.imprimir_lista()
    
    # g2.imprimir_lista()
    # g3.imprimir_lista()
    
    g2.busca_em_largura()
    g3.busca_em_largura()
    
    #g2.busca_em_profundidade()
    # g3.busca_em_profundidade()
    # g3.imprimir_dfs()
    
    # g1.busca_em_largura(1)
    # g2.busca_em_largura("A")
    
    # arvore_dfs= g1.busca_em_profundidade(1)
    # g1.imprimir_arvore(arvore_dfs, 1)
    
    # arvore_dfs2 = g2.busca_em_profundidade("A")
    # g2.imprimir_arvore(arvore_dfs2, "A")

    # g3 = ListaAdjacenciaDirecionada()
    g4 = ListaAdjacenciaDirecionada()
    # g5 = ListaAdjacencia()
    
    # g3.insere_um_par(1, 2)
    # g3.insere_um_par(1, 5)
    # g3.insere_um_par(2, 5)
    # g3.insere_um_par(2, 3)
    # g3.insere_um_par(2, 4)
    # g3.insere_um_par(5, 4)
    # g3.insere_um_par(4, 3)


    #g4.insere_listaAdjacenciaDirecionada([("A", "B"), ("A", "F"), ("B", "C"), ("B", "E"), ("C", "D"), ("E", "D"), ("E", "G"), ("D", "H"), ("D", "B"), ("G", "F"), ("H", "G"), ("F", "G"), ("F", "E")])
    # g3.imprimir_lista()
    #g4.imprimir_lista_direcionada()

    # print("Busca de profundidade")
    
    g4.busca_em_profundidade_direcionada()


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