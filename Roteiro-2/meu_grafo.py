from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from copy import copy


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        vna = set()
        for v1 in self.N:
            for v2 in self.N:
                achei = False
                for a in self.A:
                    if v1 != v2:
                        if (v1 == self.A[a].getV1() and v2 == self.A[a].getV2()) or (
                                (v2 == self.A[a].getV1()) and v1 == self.A[a].getV2()):
                            achei = True
                if not achei and v1 != v2:
                    vna.add("{}-{}".format(v1, v2))
        return set(vna)

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in self.A:
            if self.A[i].getV1() == self.A[i].getV2():
                return True

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        contGrau = 0
        for a in self.A:
            if self.A[a].getV1() == V:
                contGrau += 1
            if self.A[a].getV2() == V:
                contGrau += 1
        if V not in self.N:
            raise VerticeInvalidoException
        return contGrau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        paralelas = 0
        for a in self.A:
            for b in self.A:
                if self.A[a] == self.A[b]:
                    continue
                else:
                    if (self.A[a].getV1() == self.A[b].getV1() or self.A[a].getV1() == self.A[b].getV2()) and (
                            self.A[a].getV2() == self.A[b].getV1() or self.A[a].getV2() == self.A[b].getV2()):
                        paralelas += 1
                    else:
                        continue
        if paralelas > 0:
            return True
        else:
            return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        lista = set()
        if V not in self.N:
            raise VerticeInvalidoException
        else:
            for a in self.A:
                if self.A[a].getV1() == V or self.A[a].getV2() == V:
                    lista.add(self.A[a].getRotulo())
        return lista

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco():
            return False
        elif self.ha_paralelas():
            return False
        else:
            for a in self.N:
                if self.grau(a) < len(self.N) - 1:
                    return False
                else:
                    return True

    def dijkstra_drone(self, vi, vf, carga: int, carga_max: int, pontos_recarga: list()):
        pass

    def dfs(self, V=''):
        '''
        Cria um grafo que contém as arestas do dfs
        :param V: O vértice raiz que inicia a busca
        :return: Um grafo DFS.
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException
        elif self.ha_laco():
            return False
        else:
            def dfs_rec(V, visitado):

                visitado.append(V)
                if not self.primeiro:
                    dfs.adicionaAresta(self.aresta[2], self.aresta[0], self.aresta[1])
                self.primeiro = False

                for a in range(len(self.vertices)):
                    if V in self.vertices[a]:
                        self.aresta = self.vertices[a]
                        aresta2 = [self.aresta[0], self.aresta[1]]
                        for vizinho in aresta2:
                            if vizinho not in visitado:
                                dfs_rec(vizinho, visitado)

            dfs = MeuGrafo(copy(self.N))
            visitado = []
            self.vertices = []
            self.primeiro = True

            for b in self.A:
                self.vertices.append([self.A[b].getV1(), self.A[b].getV2(), b])

            dfs_rec(V, visitado)
            return dfs

    def bfs(self, V=''):
        '''
        Provê um grafo bfs
        :param V: vértice utilizado como referência
        :return: um grafo bfs gerado
        '''
        if V not in self.N:
            raise VerticeInvalidoException

        bfs = MeuGrafo(copy(self.N))
        visitado = [V]

        self.vertices = []
        for i in self.A:
            self.vertices.append([self.A[i].getV1(), self.A[i].getV2(), i])

        fila = []
        rotulos = []
        fila.append(V)

        for a in self.A:
            rotulos.append(self.A[a].getRotulo())

        while fila:
            s = fila.pop(0)

            for a in range(len(self.vertices)):
                if s in self.vertices[a]:
                    aresta = self.vertices[a]
                    aresta2 = [aresta[0], aresta[1]]

                    for i in aresta2:
                        if i not in visitado:
                            bfs.adicionaAresta(aresta[2], aresta[0], aresta[1])
                            fila.append(i)
                            fila = list(dict.fromkeys(fila))
                            visitado.append(i)
        return bfs
