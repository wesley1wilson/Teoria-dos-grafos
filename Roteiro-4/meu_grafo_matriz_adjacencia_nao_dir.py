from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        vna = set()
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if j != i and len(self.M[i][j]) == 0:
                    vna.add(f'{self.N[i]}-{self.N[j]}')
                    vna.add(f'{self.N[j]}-{self.N[i]}')
        return vna

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.N)):
            if (len(self.M[i][i]) > 0):
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        contGrau = 0
        if V not in self.N:
            raise VerticeInvalidoException
        else:
            for a in range(len(self.N)):
                for b in range(len(self.N)):
                    if (self.N[a] == V or self.N[b] == V) and b >= a:
                        if b == a:
                            contGrau += 2 * len(self.M[a][b])
                        else:
                            if len(self.M[a][b]) > 0:
                                contGrau += len(self.M[a][b])
            return contGrau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if (len(self.M[i][j])) > 1:
                    return True
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
            for a in range(len(self.M)):
                for b in range(len(self.M)):
                    if len(self.M[a][b]) > 0:
                        for c in self.M[a][b]:
                            if self.N[a] == V and c != '-':
                                lista.add(c)
                            if self.N[b] == V and c != '-':
                                lista.add(c)
        return lista

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco():
            return False
        for a in range(len(self.M)):
            for b in range(len(self.M)):
                if a < b and len(self.M[a][b]) == 0:
                    return False
        return True
