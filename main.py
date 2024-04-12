from listaAdj import ListaAdjacencia
from listaAdjDirecionada import ListaAdjacenciaDirecionada
import flask

if __name__ == "__main__":
    
    # Criar uma instância da classe ListaAdjacencia
    g1 = ListaAdjacencia()
    g2 = ListaAdjacencia()
    g3 = ListaAdjacencia()


    # Outra maneira de inserir múltiplos pares usando insere_multiplos_pares
    g2.insere_listaAdjacencia([("A", "B"), ("A", "E"), ("B", "C"), ("B", "E"), ("C", "F"), ("E", "F"), ("F", "I")])
    g3.insere_subgrafo(1, [[("D", "H"), ("D", "G"), ("G", "H")]])
    # Chamar a função imprimir_lista para verificar a lista de adjacência
    # g1.imprimir_lista()
    
    g2.imprimir_lista()
    g3.imprimir_lista()
    
    g2.busca_em_largura()
    g3.busca_em_largura()
    
    g2.busca_em_profundidade()
    g3.busca_em_profundidade()  
    
    # g1.busca_em_largura(1)
    # g2.busca_em_largura("A")
    
    # arvore_dfs= g1.busca_em_profundidade(1)
    # g1.imprimir_arvore(arvore_dfs, 1)
    
    # arvore_dfs2 = g2.busca_em_profundidade("A")
    # g2.imprimir_arvore(arvore_dfs2, "A")

    # g3 = ListaAdjacenciaDirecionada()
    # g4 = ListaAdjacenciaDirecionada()
    # g5 = ListaAdjacencia()
    
    # g3.insere_um_par(1, 2)
    # g3.insere_um_par(1, 5)
    # g3.insere_um_par(2, 5)
    # g3.insere_um_par(2, 3)
    # g3.insere_um_par(2, 4)
    # g3.insere_um_par(5, 4)
    # g3.insere_um_par(4, 3)


    # g4.insere_multiplos_pares([("A", "B"), ("A", "F"), ("B", "C"), ("B", "E"), ("C", "D"), ("E", "D"), ("E", "G"), ("D", "H"), ("D", "B"), ("G", "F"), ("H", "G"), ("F", "G"), ("F", "E")])
    # g3.imprimir_lista()
    # g4.imprimir_lista()

    # print("Busca de profundidade")
    
    # g4.busca_em_profundidade_direcionada("A")