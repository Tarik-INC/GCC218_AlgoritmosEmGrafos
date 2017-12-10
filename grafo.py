# coding=utf-8
import sys
from vertice import Vertice

class Grafo(object):
    def __init__(self, verts, adj, w, origem=None, destino=None,
                 t_turistas=0, pt_partida=None, euleriano=False,
                 v_min_dist1=None, v_min_dist2=None):
        self.vert = verts #Lista de vértices do grafo(a posição 0 não é usada)
        self.adj = adj  #Lista de adjacência que pode armazenar o grafo
        self.w = w    #Matriz contendo os pesos das arestas

        # Os atributos a seguir são usados apenas quando for aplicado um algortimo
        # de caminho mínimo
        self.origem = origem
        self.destino = destino

        # Armazena o total de turistas a serem transportados
        self.t_turistas = t_turistas

        # Atributos p2
        self.pto_de_partida = []
        self.euleriano = euleriano
        self.v_min_dist1 = v_min_dist1 #Vértice com menor distância do ponto de partida da máquina
        self.v_min_dist2 = v_min_dist2 #Vértice com a segunda menor distância do ponto de partida da máquina

    # Sobrescrita para poder dar print no objeto grafo
    def __str__(self):
        adju = ""
        for u in range (1, len(self.adj)):
            adju = adju + str(u)
            for v in self.adj[u]:
                adju += "-->" + str(v.id)
            adju += "-->NIL\n"
        return adju











