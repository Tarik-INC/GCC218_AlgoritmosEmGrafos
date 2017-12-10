# coding=utf-8

from copy import copy
from arquivo import Arquivo
from grafo import Grafo
from vertice import Vertice
from algoritmos import Algoritmos
import math
import sys
import math

#Converte tempo em segundo para horas : minutos - (P2)
def seg_to_h_m(tempo_s):
    tot_mins = int(math.ceil(tempo_s / 60))
    horas = int(math.floor(tot_mins / 60))
    mins = tot_mins - (horas * 60)
    return "{0}:{1:02d}".format(horas, mins)

#Calcula a soma dos custos das arestas de um caminho - (P2)
def dist_cam(cam, w):
    dist = 0
    for i in range(len(cam) - 1):
        u = cam[i]
        v = cam[i + 1]
        dist += w[u.id][v.id]
    return dist

#Calcula a distância a distância total do grafo considerando que ele é euleriano
def dist_eu(grafo):
    dist_t = 0
    for u in range(1, len(grafo.vert)):
        for v in grafo.adj[u]:
            dist_t += grafo.w[u][v.id]  # Cálculo da distância percorrendo todas as arestas do grafo
    return dist_t

#Calcula o tempo que a máquina gasta para coletar a neve
def tempo_tot_maquina(grafo):
    #Se o grafo for euleriano todas as ruas serão percorridas uma única vez
    if grafo.euleriano:
        dist_t = dist_eu(grafo)
        temp_seg = dist_t / (20000.0/3600.0) #Todas as arestas são percorridas a 20km/h ou (20000/3600)m/s
        return seg_to_h_m(temp_seg)
    # Se não temos que achar o caminho mínimo entre os dois vértices mais próximos do pto. de partida
    # e duplicar as arestas dele para eulerizar o grafo com o menor custo possível
    else:
        ini = grafo.v_min_dist1
        fim = grafo.v_min_dist2

        dist_pp_ini = grafo.v_min_dist1.d # Distância entre o pto. de partida e o vértice mais próximo - (saída)
        dist_fim_pp = grafo.v_min_dist2.d # Distância entre o 2º vértice mais próximo e o pto. de partida - (retorno)

        dist_eul = dist_eu(grafo) #Distância total da "componente euleriana" do grafo

        #Aplique dijkistra para obter o caminho mínimo de ini até fim(caminho eulerizante)
        Algoritmos.dijkistra(grafo, grafo.w, ini, 2)

        cam_eulerizante = Algoritmos.cam_list(fim)
        dist_cam_eu = dist_cam(cam_eulerizante, grafo.w)

        v_min_ms = 20000.0 / 3600
        v_max_ms = 50000.0 / 3600

        # tempo = distância / velocidade (Considerando que as ruas que ligam o pto. de partida a outra rua ou vice-versa
        # também estarão iniciamente cobertas de neve)
        tempo_seg = (dist_pp_ini/ v_min_ms) + (dist_eul/v_min_ms) +\
                  (dist_cam_eu/v_max_ms) + (dist_fim_pp/v_min_ms)

        return seg_to_h_m(tempo_seg)

# Soluciona o problema 2
def solucionar_p2(nome_arq):
    print("\n***Solução da p2***\n")
    problema = 2  # Indica o n. do problema para saber como o grafo deve ser montado
    arquivo = Arquivo(nome_arq, problema)

    for g in arquivo.grafos:
       print("{0}\n".format(tempo_tot_maquina(g)))

def main():
    args = sys.argv
    solucionar_p2(args[1])

if __name__ == '__main__':
    main()