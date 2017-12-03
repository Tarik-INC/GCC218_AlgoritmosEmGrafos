# coding=utf-8

import math

class Vertice(object):
    def __init__(self, id, d=float("inf"), f=float("inf"), pai=None, coord=None):

        self.id = id
        self.pi = pai
        self.d = d
        self.f = f

        # para ser usado no MaxHeap
        self.indice = id - 1

        # para ser usado no p2
        self.coord = coord

    # Sobrecarga do operador < (considera o valor de d na comparação)
    def __lt__(self, other):
        return self.d < other.d

    # Sobrecarga do operador > (considera o valor de d na comparação)
    def __gt__(self, other):
        return self.d > other.d

        # Calcula a distância entre dois vértices(Comprimento da rua)

    @staticmethod
    def distancia(u, v):
        x1 = u.coord[0]
        y1 = u.coord[1]
        x2 = v.coord[0]
        y2 = v.coord[1]
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

