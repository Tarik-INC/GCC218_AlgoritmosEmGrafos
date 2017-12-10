# coding=utf-8

from arquivo import Arquivo
from copy import copy
from max_heap import MaxHeap
from min_heap import MinHeap
from vertice import Vertice


class Algoritmos:

    # Método para inicializar os vértices de um grafo na aplicação de um algoritmo
    # de caminho mínimo(problema 2) ou o "caminho com maior vazão"(problema 1)
    @staticmethod
    def init_single_source(grafo, origem, prob):
        for i in range(1, len(grafo.vert)):
            if prob == 1:
                grafo.vert[i].d = 0
            else:
                grafo.vert[i].d = float("inf")
            grafo.vert[i].pi = None
        if prob == 1:
            origem.d = float("inf")
        else:
            origem.d = 0

    # Método relax para atualizar v.d e v.pi
    @staticmethod
    def relax(heap, u, v, w, prob):
        if prob == 1:
            max_gargalo = min(u.d, w[u.id][v.id])
            if v.d < max_gargalo:
                v.d = max_gargalo
                MaxHeap.increase_key(heap, v.indice) # Reorganiza o heap
                v.pi = u
        else:
            new_d = u.d + w[u.id][v.id]
            if v.d > new_d:
                v.d = new_d
                MinHeap.decrease_key(heap, v.indice)
                v.pi = u

    # Algoritmo de Dijkistra modificado especificamente para a questão 1
    @staticmethod
    def dijkistra(grafo, w, origem, prob):

        Algoritmos.init_single_source(grafo, origem, prob)

        # Faz uma cópia dos vértices do 'grafo' para ser usada em um MaxHeap
        # Importa copy cria uma nova lista vert, mas mantém as referências dos vértices inalteradas
        verts = copy(grafo.vert)
        del verts[0] # O primeiro elemento contém apenas lixo

        # Transforma verts em um MaxHeap
        if prob == 1:
            MaxHeap.build_max_heap(verts)
        else:
            MinHeap.build_min_heap(verts)

        # Percorre adj[u], onde um é o menor valor extraído de verts
        # aplicando relax_q1, até que verts esteja vazia
        while verts != []:
            u = Vertice(-1)
            if prob == 1:
                u = MaxHeap.extract_max(verts)
            else:
                u = MinHeap.extract_min(verts)

            #print("Extraído: " + str(u.id))

            for i in range (len(grafo.adj[u.id])):
                v = grafo.adj[u.id][i]
                Algoritmos.relax(verts, u, v, w, prob)

    # Função recursiva que retorna o caminho(str) de uma origem a um destino
    # a origem não precisa ser especificada pois pi[origem] é NIL
    @staticmethod
    def caminho(destino):
        if destino.pi != None:
            return Algoritmos.caminho(destino.pi) + "-->" + str(destino.id)
        return str(destino.id)

    # Retorna o caminho em forma de lista
    @staticmethod
    def cam_list(destino):
        v = destino
        c = []
        while v != None:
            c.append(v)
            v = v.pi
        c = reversed(c)
        return list(c)




