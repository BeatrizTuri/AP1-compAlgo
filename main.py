from listaAdj import ListaAdjacencia


if __name__ == "__main__":
    
    # Criar uma instância da classe ListaAdjacencia
    g1 = ListaAdjacencia()
    g2 = ListaAdjacencia()

    # Exemplo de inserção de pares usando insere_um_par
    g1.insere_um_par(1, 2)
    g1.insere_um_par(1, 5)
    g1.insere_um_par(2, 5)
    g1.insere_um_par(2, 3)
    g1.insere_um_par(2, 4)
    g1.insere_um_par(5, 4)
    g1.insere_um_par(4, 3)

    # Outra maneira de inserir múltiplos pares usando insere_multiplos_pares
    g2.insere_multiplos_pares([("A", "B"), ("A", "E"), ("B", "C"), ("B", "E"), ("C", "F"), ('E', "F"), ("F", "I"), ("D", "H"), ("D", "G"), ("G", "H")])

    # Chamar a função imprimir_lista para verificar a lista de adjacência
    g1.imprimir_lista()
    g2.imprimir_lista()
    g1.busca_em_largura(1)
    g2.busca_em_largura("A")
    
    arvore_dfs= g1.busca_em_profundidade(1)
    g1.imprimir_arvore(arvore_dfs, 1)
    
    arvore_dfs2 = g2.busca_em_profundidade("A")
    g2.imprimir_arvore(arvore_dfs2, "A")
