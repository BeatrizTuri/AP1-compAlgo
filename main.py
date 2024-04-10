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
    g2.insere_multiplos_pares([(1, 2), (1, 5), (2, 5), (2, 3), (2, 4), (5, 4), (4, 3)])

    # Chamar a função imprimir_lista para verificar a lista de adjacência
    g1.imprimir_lista()
    g2.imprimir_lista()


# 1: [2, 5]
# 2: [1, 5, 3, 4]
# 5: [1, 2, 4]
# 3: [2, 4]
# 4: [2, 5, 3]

# 1: [2, 5]
# 2: [1, 5, 3, 4]
# 5: [1, 2, 4]
# 3: [2, 4]
# 4: [2, 5, 3]