from meu_grafo_matriz_adjacencia_nao_dir import MeuGrafo

grafo_paraiba = MeuGrafo()
grafo_paraiba.adicionaVertice("J")
grafo_paraiba.adicionaVertice("C")
grafo_paraiba.adicionaVertice("E")
grafo_paraiba.adicionaVertice("P")
grafo_paraiba.adicionaVertice("M")
grafo_paraiba.adicionaVertice("T")
grafo_paraiba.adicionaVertice("Z")
grafo_paraiba.adicionaAresta('a1', 'J', 'C')
grafo_paraiba.adicionaAresta('a2', 'C', 'E')
grafo_paraiba.adicionaAresta('a3', 'C', 'E')
grafo_paraiba.adicionaAresta('a4', 'P', 'C')
grafo_paraiba.adicionaAresta('a5', 'P', 'C')
grafo_paraiba.adicionaAresta('a6', 'T', 'C')
grafo_paraiba.adicionaAresta('a7', 'M', 'C')
grafo_paraiba.adicionaAresta('a8', 'M', 'T')
grafo_paraiba.adicionaAresta('a9', 'T', 'Z')
print(grafo_paraiba)