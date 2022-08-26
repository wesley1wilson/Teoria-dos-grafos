from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from copy import deepcopy
from sys import maxsize
from math import inf


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

    def vertice_oposto(self, a, r):
        if self.A[a].getV1() == r:
            v = self.A[a].getV2()
        else:
            v = self.A[a].getV1()
        return v

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

    def dijkstra_drone(self, vi, vf):
        if vi not in self.N or vf not in self.N:
            raise VerticeInvalidoException

        beta = {vertice: maxsize if vertice != vi else 0 for vertice in self.N}
        fi = {vertice: 0 for vertice in self.N}
        pi = {vertice: '' for vertice in self.N}

        self.busca_dijkstra(vi, vf, beta, fi, pi)
        return self.caminho_dijkstra(vf, pi)

    def menor_beta(self, beta, fi):
        menor = maxsize
        for vertice in beta:
            if fi[vertice] == 0:
                if beta[vertice] < menor:
                    menor = beta[vertice]
                    vi = vertice
        return vi

    def caminho_dijkstra(self, vf, pi):
        caminho = []
        while True:
            if pi[vf] == '':
                break
            caminho.append(vf + "-" + pi[vf])
            vf = pi[vf]
        return caminho

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

            dfs = MeuGrafo(deepcopy(self.N))
            visitado = []
            self.vertices = []
            self.primeiro = True

            for b in self.A:
                self.vertices.append([self.A[b].getV1(), self.A[b].getV2(), b])

            dfs_rec(V, visitado)
            return dfs

    def busca_dijkstra(self, vi, vf, beta, fi, pi):
        while vi != vf:
            fi[vi] = 1
            for aresta in self.arestas_sobre_vertice(vi):
                oposto = self.vertice_oposto(aresta, vi)
                peso = self.getAresta(aresta).getPeso()
                if beta[oposto] > (beta[vi] + peso):
                    beta[oposto] = beta[vi] + peso
                    pi[oposto] = vi
            vi = self.menor_beta(beta, fi)

    def bfs(self, V=''):
        '''
        Provê um grafo bfs
        :param V: vértice utilizado como referência
        :return: um grafo bfs gerado
        '''
        if V not in self.N:
            raise VerticeInvalidoException

        bfs = MeuGrafo(deepcopy(self.N))
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

    def ha_ciclo(self):
        lista = []
        lista2 = []
        self.ha_ciclo_rec(self.N[0], lista)
        for a in range(len(lista)):
            for b in range(a + 1, len(lista)):
                if lista[a] == lista[b]:
                    lista2 = lista[a:b + 1:]
                    if lista2:
                        return lista2
        return False

    def ha_ciclo_rec(self, v, lista):
        if v not in lista:
            lista.append(v)
        else:
            lista.append(v)
            return

        for i in self.arestas_sobre_vertice(v):
            if i not in lista:
                v1 = self.A[i].getV1()
                v2 = self.A[i].getV2()
                if v1 != v:
                    lista.append(i)
                    self.ha_ciclo_rec(v1, lista)
                if v2 != v:
                    lista.append(i)
                    self.ha_ciclo_rec(v2, lista)

    def caminho(self, tamanho):
        lista = []
        lista = self.caminho_rec(self.N[0], tamanho, lista)
        if lista is None:
            return False
        return lista

    def caminho_rec(self, v, tam, lis):
        keys = list(self.A.keys())
        x = 0
        if v not in lis:
            if len(lis) > 0:
                lis.append(self.caminho_dois_vertices(lis[(len(lis) - 1)], v))
            lis.append(v)
            for b in self.A:
                v1 = self.A[b].getV1()
                v2 = self.A[b].getV2()
                paralela = self.ha_paralelas()
                if paralela:
                    v1 = self.A[keys[x + 1]].getV1()
                    v2 = self.A[keys[x + 1]].getV2()
                    if x == len(keys):
                        x = 0
                    if tam == self.vertices_lista(lis):
                        return lis
                    if v1 != v:
                        self.caminho_rec(v1, tam, lis)
                    elif v2 != v:
                        self.caminho_rec(v2, tam, lis)
                else:
                    if x == len(keys):
                        x = 0
                    if tam == self.vertices_lista(lis):
                        return lis
                    if v1 != v:
                        self.caminho_rec(v1, tam, lis)
                    elif v2 != v:
                        self.caminho_rec(v2, tam, lis)

    def caminho_dois_vertices(self, x, y):
        for a in self.A:
            if (self.A[a].getV1() == x) and (self.A[a].getV2() == y):
                return a

    def vertices_lista(self, lis):
        lista_v = self.N
        cont = 0
        for a in lis:
            if a in lista_v:
                cont += 1
        return cont

    def conexo(self):
        arestas = list()
        adjacentes = []
        for b in self.A:
            arestas.append(self.A[b].getV1() + "-" + self.A[b].getV2())
        for vertice in self.N:
            if len(adjacentes) < 1:
                adjacentes.append(vertice)
            if vertice in adjacentes:
                for a in arestas:
                    if vertice in a:
                        if vertice == a[0] and a[2] not in adjacentes:
                            adjacentes.append(a[2])
                        elif vertice == a[2] and a[0] not in adjacentes:
                            adjacentes.append(a[0])
        if len(adjacentes) == len(self.N):
            return True
        else:
            return False

    sets = {}

    def floresta(self, v):
        self.sets[v] = [v]

    def procura(self, v):
        for i, x in self.sets.items():
            if v in x:
                return i
        return None

    def uniao(self, v1, v2):
        vertice1 = self.procura(v1)
        vertice2 = self.procura(v2)
        self.sets[vertice1] = self.sets[vertice1] + self.sets[vertice2]
        del self.sets[vertice2]

    def vertices_adjacentes(self, v):
        N = self.N
        lista = []
        for a in self.A:
            if self.A[a].getV1() == v:
                lista.append(self.A[a].getV2())
            if self.A[a].getV2() == v:
                lista.append(self.A[a].getV1())
        return lista

    def KruskallModificado(self):

        arvore_minima = MeuGrafo()
        nome_aresta = 1

        for i in self.N:
            self.floresta(i)

        self.lista_final_kruskall = []

        dicionarioArestasComPesos = self.dicionario_peso_aresta()
        arestas_menor_peso = self.dicionario_peso_aresta()
        arestas_menor_peso = dict(sorted(arestas_menor_peso.items(), key=lambda x: x[1], reverse=False))
        arestas_menor_peso = arestas_menor_peso.values()

        if self.conexo():
            for a in arestas_menor_peso:
                for i in dicionarioArestasComPesos:
                    if dicionarioArestasComPesos[i] == a:
                        if self.procura(i[0]) != self.procura(i[2]):
                            v1 = i[0]
                            v2 = i[2]
                            self.lista_final_kruskall.append(i)
                            existe_vertice1 = arvore_minima.existeVertice(v1)
                            existe_vertice2 = arvore_minima.existeVertice(v2)
                            if not existe_vertice1:
                                arvore_minima.adicionaVertice(v1)
                            if not existe_vertice2:
                                arvore_minima.adicionaVertice(v2)
                            if not (existe_vertice1 and existe_vertice2) or (existe_vertice1 and existe_vertice2):
                                v1, v2 = i.split(self.SEPARADOR_ARESTA)
                                arvore_minima.adicionaAresta(str(nome_aresta), v1, v2, a)
                                nome_aresta = nome_aresta + 1
                            self.uniao(v1, v2)
            return arvore_minima

    def procurar_na_arvore(self, vertice, lista=[]):
        if vertice not in lista:
            return True
        else:
            return False

    def dicionario_peso_aresta(self):
        dic = {}
        for a in self.A:
            aresta = '{}{}{}'.format(self.A[a].getV1(), self.SEPARADOR_ARESTA, self.A[a].getV2())
            dic[aresta] = self.A[a].getPeso()
        return dic

    def criar_aresta(self, v1, v2):
        aresta = "{}{}{}".format(v1, self.SEPARADOR_ARESTA, v2)
        return aresta

    def lista_kruskall(self):
        """
        Fornece uma representação do tipo lista para o grafo de Kruskall modificado
        :return: As arestas do grafo
        """
        self.KruskallModificado()
        return self.lista_final_kruskall

    def PrimModificado(self):
        vertices = deepcopy(self.N)
        arestas = []
        nome_aresta = 1

        for a in self.A:
            aresta1 = '{}{}{}'.format(self.A[a].getV1(), self.SEPARADOR_ARESTA, self.A[a].getV2())
            arestas.append(aresta1)

        dic_peso = self.dicionario_peso_aresta()
        Jet = {}
        P = {}
        self.lista_final_prim = []
        guarda_peso = inf
        arvore = MeuGrafo()

        for vertice in vertices:
            Jet[vertice] = inf
            P[vertice] = None

        for aresta in arestas:
            listap = dic_peso[aresta]
            peso = listap
            if peso < guarda_peso:
                guarda_peso = peso
                v1, v2 = aresta.split(self.SEPARADOR_ARESTA)

        Jet[v1] = 0
        lista_prioridade = deepcopy(self.N)

        while (len(lista_prioridade) != 0):
            menor_peso = inf
            vertice_menor_peso = ''
            for v in lista_prioridade:
                if isinstance(Jet[v], list) == True:
                    jet = Jet[v][0]
                    if jet < menor_peso:
                        pesolista = Jet[v]
                        menor_peso = pesolista[0]
                        vertice_menor_peso = v
                else:
                    if Jet[v] < menor_peso:
                        menor_peso = Jet[v]
                        vertice_menor_peso = v
            x = vertice_menor_peso

            lista_prioridade.pop(lista_prioridade.index(vertice_menor_peso))
            lista_vertices_adjacente = self.vertices_adjacentes(x)

            for vertice_adjacente in lista_vertices_adjacente:
                aresta_y = x + "-" + vertice_adjacente
                if aresta_y not in arestas:
                    aresta_y = vertice_adjacente + '-' + x
                pesoy = dic_peso[aresta_y]
                jety = Jet[vertice_adjacente]

                if isinstance(jety, list):
                    if vertice_adjacente in lista_prioridade and pesoy < jety[0]:
                        P[vertice_adjacente] = x
                        Jet[vertice_adjacente] = dic_peso[aresta_y]
                else:
                    if vertice_adjacente in lista_prioridade and pesoy < jety:
                        P[vertice_adjacente] = x
                        Jet[vertice_adjacente] = dic_peso[aresta_y]

        for v in vertices:
            arvore.adicionaVertice(v)

        self.lista_final = []
        for a, i in P.items():
            if i:
                self.lista_final.append(self.criar_aresta(i, a))

        dic_menor_peso = self.dicionario_peso_aresta()
        for i in self.lista_final:
            v2, v1 = i.split(self.SEPARADOR_ARESTA)
            inverso = self.criar_aresta(v1, v2)
            if i in dic_menor_peso:
                self.lista_final_prim.append(i)
                v1, v2 = i.split(self.SEPARADOR_ARESTA)
                arvore.adicionaAresta(str(nome_aresta), v1, v2, dic_menor_peso[i])
                nome_aresta = nome_aresta + 1
            if inverso in dic_menor_peso:
                self.lista_final_prim.append(inverso)
                v1, v2 = inverso.split(self.SEPARADOR_ARESTA)
                arvore.adicionaAresta(str(nome_aresta), v1, v2, dic_menor_peso[inverso])
                nome_aresta = nome_aresta + 1
        return arvore

    def lista_prim(self):
        """
        Fornece uma representação do tipo lista para o grafo de Prim modificado
        :return: As arestas do grafo
        """
        self.PrimModificado()
        return self.lista_final_prim