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
    #Retorna a página inicial
    return flask.render_template('home.html')

#Rotas para as páginas de inserção de listas   
@app.route('/Direcionada')
def listaDirecionada():
    #Retorna a página de inserção de listas
    return flask.render_template('listaDirecionada.html')

#Rotas para as páginas de inserção de subgrafos
@app.route('/NaoDirecionada')
def listaNaoDirecionada():
    #Retorna a página de inserção de subgrafos
    return flask.render_template('listaNaoDirecionada.html')

#Rotas para as páginas de exibição de listas
@app.route('/insereListaDirecionada', methods=['POST'])
def insereListaDirecionada():
    #Recebe a lista de pares
    lista_pares = flask.request.form.get("grafoInput")
    #Formata a lista de pares
    lista_formatada = []
    #Para cada par de vértices na lista de pares
    for i in range (len(lista_pares)):
        #Se o caractere na posição i for igual a "("
        if lista_pares[i] == "(":
            #Adiciona o par de vértices à lista formatada
            lista_formatada.append((lista_pares[i+2], lista_pares[i+7]))
    
    #Insere a lista formatada na lista de adjacência direcionada     
    lad.insere_listaAdjacenciaDirecionada(lista_formatada)

    #Se a lista formatada não estiver vazia
    if lista_formatada != []:
        #Retorna a mensagem de sucesso
        return flask.render_template('mensagem.html', mensagem="Grafo inserido com sucesso!")
    #Se a lista formatada estiver vazia
    else:
        #Retorna a mensagem de erro
        return flask.render_template('mensagem.html', mensagem="Erro ao inserir o Grafo!")
    
#Rotas para as páginas de exibição de subgrafos
@app.route('/insereSubgrafoDirecionado', methods=['POST'])
def insereSubgrafoDirecionado():
    #Recebe os dados do formulário
    dados = flask.request.form
    #Recebe a quantidade de subgrafos a serem inseridos
    qtd = dados.get("qtdInput")
    #Recebe a lista de pares
    lista_pares = dados.get("subgrafoInput")
    #Formata a lista de pares
    lista_formatada = []
    #Para cada par de vértices na lista de pares
    for i in range (len(lista_pares)):
        #Se o caractere na posição i for igual a "("
        if lista_pares[i] == "(":
            #Adiciona o par de vértices à lista formatada
            lista_formatada.append((lista_pares[i+2], lista_pares[i+7]))
    
    #Insere a lista formatada na lista de adjacência direcionada
    lad.insere_subgrafo_direcionado(qtd, lista_formatada)
    #Insere a lista formatada na lista de adjacência
    sd.insere_subgrafo_direcionado(qtd, lista_formatada)
    
    #Se a lista formatada não estiver vazia
    if lista_formatada != []:
        #Retorna a mensagem de sucesso
        return flask.render_template('mensagem.html', mensagem="Grafo inserido com sucesso!")
    #Se a lista formatada estiver vazia
    else:
        #Retorna a mensagem de erro
        return flask.render_template('mensagem.html', mensagem="Erro ao inserir o Grafo!")

#Rotas para as páginas de exibição de listas
@app.route('/exibeListaDirecionada', methods=['GET'])
#Método para exibir a lista de adjacência direcionada
def exibeListaDirecionada():
    #Recebe a lista de adjacência direcionada
    grafo = lad.listaAdjacenciaDirecionada

    #Retorna a página de exibição da lista de adjacência direcionada
    return flask.render_template('listaDirecionada.html', grafo=grafo)

#Rotas para as páginas de exibição de listas
@app.route('/insereListaNaoDirecionada', methods=['POST'])
def insereListaNaoDirecionada():
    #Recebe a lista de pares
    lista_pares = flask.request.form.get("grafoInput")
    #Formata a lista de pares
    lista_formatada = []
    #Para cada par de vértices na lista de pares
    for i in range (len(lista_pares)):
        #Se o caractere na posição i for igual a "("
        if lista_pares[i] == "(":
            #Adiciona o par de vértices à lista formatada
            lista_formatada.append((lista_pares[i+2], lista_pares[i+7]))
    
    #Insere a lista formatada na lista de adjacência
    la.insere_listaAdjacencia(lista_formatada)

    #Se a lista formatada não estiver vazia
    if lista_formatada != []:
        #Retorna a mensagem de sucesso
        return flask.render_template('mensagem.html', mensagem="Grafo inserido com sucesso!")
    #Se a lista formatada estiver vazia
    else:
        #Retorna a mensagem de erro
        return flask.render_template('mensagem.html', mensagem="Erro ao inserir o Grafo!")

#Rotas para as páginas de exibição de subgrafos
@app.route('/insereSubgrafoNaoDirecionado', methods=['POST'])   
def insereSubgrafoNaoDirecionado(): 
    #Recebe os dados do formulário
    dados = flask.request.form
    #Recebe a quantidade de subgrafos a serem inseridos
    qtd = dados.get("qtdInput")
    #Recebe a lista de pares
    lista_pares = dados.get("subgrafoInput")
    #Formata a lista de pares
    lista_formatada = []
    #Para cada par de vértices na lista de pares
    for i in range (len(lista_pares)):
        #Se o caractere na posição i for igual a "("
        if lista_pares[i] == "(":
            #Adiciona o par de vértices à lista formatada
            lista_formatada.append((lista_pares[i+2], lista_pares[i+7]))
    
    #Insere a lista formatada na lista de adjacência
    la.insere_subgrafo(qtd, lista_formatada)
    #Insere a lista formatada na lista de adjacência
    s.insere_subgrafo(qtd, lista_formatada)
    
    #Se a lista formatada não estiver vazia
    if lista_formatada != []:
        #Retorna a mensagem de sucesso
        return flask.render_template('mensagem.html', mensagem="Grafo inserido com sucesso!")
    #Se a lista formatada estiver vazia
    else:
        #Retorna a mensagem de erro
        return flask.render_template('mensagem.html', mensagem="Erro ao inserir o Grafo!")

#Rotas para as páginas de exibição de listas
@app.route('/exibeListaNaoDirecionada', methods=['GET'])
def exibeListaNaoDirecionada():
    #Recebe a lista de adjacência
    grafo = la.listaAdjacencia

    #Retorna a página de exibição da lista de adjacência
    return flask.render_template('listaNaoDirecionada.html', grafo=grafo)

#Rotas para os algoritmos de busca BFS
@app.route('/BuscaEmLarguraDirecionada', methods=['GET'])
def buscaEmLarguraDirecionada():
    #Recebe a lista de adjacência direcionada
    grafo = {}
    #Recebe a lista de adjacência direcionada
    subgrafo = {}
    #Se a lista de adjacência direcionada não estiver vazia
    if lad.listaAdjacenciaDirecionada != {}:
        #Realiza a busca em largura direcionada
        grafo = lad.busca_em_largura_direcionada()
        #Retorna a lista de adjacência direcionada
    if sd.listaAdjacenciaDirecionada != {}:
        #Realiza a busca em largura direcionada
        subgrafo = sd.busca_em_largura_direcionada()
    
    #Retorna a página de exibição da busca em largura direcionada
    return flask.render_template('algoritmoDirecionadaBFS.html', grafoBFS=grafo, subgrafoBFS=subgrafo)

#Rotas para os algoritmos de busca DFS
@app.route('/BuscaEmProfundidadeDirecionada', methods=['GET'])
def buscaEmProfundidadeDirecionada():
    #Recebe a lista de adjacência direcionada
    grafo = {}
    #Realiza a busca em profundidade direcionada
    grafo = lad.busca_em_profundidade_direcionada()
    
    #Retorna a página de exibição da busca em profundidade direcionada
    return flask.render_template('algoritmoDirecionadaDFS.html', grafoDFS=grafo)

#Rotas para os algoritmos de busca BFS
@app.route('/BuscaEmLargura', methods=['GET'])
def buscaEmLargura(): 
    #Recebe a lista de adjacência 
    grafo = {} 
    #Recebe a lista de adjacência
    subgrafo = {}
    #Se a lista de adjacência não estiver vazia
    if la.listaAdjacencia != {}:
        #Realiza a busca em largura
        grafo = la.busca_em_largura()
    #Se a lista de adjacência não estiver vazia
    if s.listaAdjacencia != {}:
        #Realiza a busca em largura
        subgrafo = s.busca_em_largura()
    
    #Retorna a página de exibição da busca em largura
    return flask.render_template('algoritmoNaoDirecionadaBFS.html', grafoBFS=grafo, subgrafoBFS=subgrafo)

#Rotas para os algoritmos de busca DFS
@app.route('/BuscaEmProfundidade', methods=['GET'])
def buscaEmProfundidade():
    #Recebe a lista de adjacência
    grafo = {}
    #Realiza a busca em profundidade
    grafo = la.busca_em_profundidade()

    #Retorna a página de exibição da busca em profundidade
    return flask.render_template('algoritmoNaoDirecionadaDFS.html', grafoDFS=grafo)


if __name__ == "__main__":
    
    # #Iniciando o servidor
    if not os.environ.get("WERKZEUG_RUN_MAIN"): #Executa apenas uma vez
        webbrowser.open("http://127.0.0.1:5000")

    app.run(debug=True)
