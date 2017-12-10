# coding=utf-8

from arquivo import Arquivo
from grafo import Grafo
from vertice import Vertice
from algoritmos import Algoritmos
import math
import sys

def solucionar_p1(nome_arq):
    print("\n***Solução da p1***\n")
    problema = 1 #Indica o n. do problema para saber como o grafo deve ser montado
    arquivo = Arquivo(nome_arq, problema)

    caso = 1
    for g in arquivo.grafos:
        Algoritmos.dijkistra(g, g.w, g.origem, 1)

        turistas_por_viagem = g.destino.d - 1 # Descontando o motorista
        n_viagens = int(math.ceil(g.t_turistas/turistas_por_viagem))

        print("Caso #{0}".format(caso))
        print ("Mínimo de viagens: {0}".format(n_viagens))
        print("Rota: {0}\n".format(Algoritmos.caminho(g.destino)))

        caso += 1

def main():
    args = sys.argv
    solucionar_p1(args[1])

if __name__ == '__main__':
    main()