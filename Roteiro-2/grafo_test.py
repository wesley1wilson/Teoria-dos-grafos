import unittest
from meu_grafo import *
from bibgrafo.grafo_exceptions import *


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p2.adicionaAresta('a1', 'J', 'C')
        self.g_p2.adicionaAresta('a2', 'C', 'E')
        self.g_p2.adicionaAresta('a3', 'C', 'E')
        self.g_p2.adicionaAresta('a4', 'P', 'C')
        self.g_p2.adicionaAresta('a5', 'P', 'C')
        self.g_p2.adicionaAresta('a6', 'T', 'C')
        self.g_p2.adicionaAresta('a7', 'M', 'C')
        self.g_p2.adicionaAresta('a8', 'M', 'T')
        self.g_p2.adicionaAresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p3.adicionaAresta('a', 'J', 'C')
        self.g_p3.adicionaAresta('a2', 'C', 'E')
        self.g_p3.adicionaAresta('a3', 'C', 'E')
        self.g_p3.adicionaAresta('a4', 'P', 'C')
        self.g_p3.adicionaAresta('a5', 'P', 'C')
        self.g_p3.adicionaAresta('a6', 'T', 'C')
        self.g_p3.adicionaAresta('a7', 'M', 'C')
        self.g_p3.adicionaAresta('a8', 'M', 'T')
        self.g_p3.adicionaAresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p4.adicionaAresta('a1', 'J', 'C')
        self.g_p4.adicionaAresta('a2', 'J', 'E')
        self.g_p4.adicionaAresta('a3', 'C', 'E')
        self.g_p4.adicionaAresta('a4', 'P', 'C')
        self.g_p4.adicionaAresta('a5', 'P', 'C')
        self.g_p4.adicionaAresta('a6', 'T', 'C')
        self.g_p4.adicionaAresta('a7', 'M', 'C')
        self.g_p4.adicionaAresta('a8', 'M', 'T')
        self.g_p4.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1', 'J', 'C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        self.g_d2 = MeuGrafo(['A', 'B', 'C', 'D'])

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z', 'E-J', 'P-J', 'M-J', 'T-J', 'Z-J', 'Z-C', 'P-E', 'M-E', 'T-E', 'Z-E', 'M-P', 'T-P',
                          'Z-P',
                          'Z-M'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D', 'C-A', 'D-A', 'C-B', 'D-B', 'D-C'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D', 'B-A', 'C-A', 'D-A', 'C-B', 'D-B', 'D-C'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())
    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def test_dfs(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertEqual(list(self.g_p.dfs('J').A), ['a1', 'a2', 'a4', 'a6', 'a8', 'a9'])
        self.assertEqual(list(self.g_p.dfs('C').A), ['a1', 'a2', 'a4', 'a6', 'a8', 'a9'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('M').A), ['a5', 'a1', 'a2', 'a3', 'a4', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('T').A), ['a4', 'a1', 'a2', 'a3', 'a5', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('Z').A), ['a7', 'a4', 'a1', 'a2', 'a3', 'a5'])
        self.assertEqual(list(self.g_c.dfs('C').A), ['a1', 'a2', 'a6'])
        self.assertEqual(list(self.g_c.dfs('E').A), ['a2', 'a1', 'a5'])
        self.assertEqual(list(self.g_c.dfs('P').A), ['a3', 'a1', 'a4'])
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_bfs(self):
        self.assertEqual(list(self.g_p.bfs('C').A), ['a1', 'a2', 'a4', 'a6', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.bfs('E').A), ['a2', 'a1', 'a4', 'a6', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.bfs('J').A), ['a1', 'a2', 'a4', 'a6', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.bfs('M').A), ['a7', 'a8', 'a1', 'a2', 'a4', 'a9'])
        self.assertEqual(list(self.g_p.bfs('P').A), ['a4', 'a1', 'a2', 'a6', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.bfs('T').A), ['a6', 'a8', 'a9', 'a1', 'a2', 'a4'])
        self.assertEqual(list(self.g_p.bfs('Z').A), ['a9', 'a6', 'a8', 'a1', 'a2', 'a4'])
        self.assertEqual(list(self.g_l1.bfs('A').A), ['a2'])
        self.assertEqual(list(self.g_l2.bfs('A').A), ['a1'])
        self.assertEqual(list(self.g_l3.bfs('C').A), ['a1'])
        self.assertEqual(list(self.g_l4.bfs('D').A), [])
        self.assertEqual(list(self.g_l5.bfs('C').A), ['a1'])
