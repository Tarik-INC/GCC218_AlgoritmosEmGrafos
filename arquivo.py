# coding=utf-8
from grafo import Grafo
from vertice import Vertice
import math


class Arquivo:
    # Construtor
    def __init__(self, nome_arq, problema):
        self.problema = problema    # N. do problema a ser resolvido
        self.grafos = []            # lista dos grafos montados a partir do arquivo
        if problema == 1:
            self.ler_arquivo_p1(nome_arq)
        elif problema == 2:
            self.ler_arquivo_p2(nome_arq)

    # Lê o arquivo de entrada e constrói os grafos a partir dele
    def ler_arquivo_p1(self, nome_arq):
        with open(nome_arq, 'r') as arq_in:
            linha = arq_in.readline()
            aux = linha.split()
            soma = int(aux[0]) + int(aux[1])  # Para verificar se é o fim do arquivo
            while (soma != 0):
                aux = linha.split()
                n = int(aux[0])
                m = int(aux[1])

                # Cria a lista de vertices
                verts = (n + 1) * [None]

                # Cria a lista de adj
                adj = []
                for i in range(n + 1):
                    adj.append([])

                # Cria w
                w = []
                for i in range(n + 1):
                    w.append((n + 1) * [0])

                # Lê as arestas e preenche a lista de adj e w, considerando o grafo como não-direcionado
                for i in range(m):
                    linha = arq_in.readline()
                    aux = linha.split()

                    u = int(aux[0])
                    if verts[u] == None:
                        verts[u] = Vertice(u, float("inf"), float("inf"), None)

                    v = int(aux[1])
                    if verts[v] == None:
                        verts[v] = Vertice(v, float("inf"), float("inf"), None)

                    p = float(aux[2])
                    w[u][v] = p
                    w[v][u] = p
                    adj[u].append(verts[v])
                    adj[v].append(verts[u])

                # Lê a origem e o destino
                linha = arq_in.readline()
                aux = linha.split()
                origem = verts[int(aux[0])]
                destino = verts[int(aux[1])]
                t_turistas = int(aux[2])

                g = Grafo(verts, adj, w, origem, destino, t_turistas)
                self.grafos.append(g)

                linha = arq_in.readline()
                aux = linha.split()
                soma = int(aux[0]) + int(aux[1])


    def ler_arquivo_p2(self, nome_arq):
        with open(nome_arq, 'r') as arq_in:
            n_casos = int(arq_in.readline()) # Lê a quantidade de casos
            pt_partida = []
            linha = arq_in.readline()  # Salta linha em branco
            for i in range(n_casos):
                linha = arq_in.readline() # Lê o ponto de partida da máquina
                linha = linha.split()
                pt_de_partida = [int(linha[0]), int(linha[1])]

                verts = [None]
                adj = [[]]
                w = []
                n_verts = 0
                euleriano = False
                min_dist1 = float("inf")
                min_dist2 = float("inf")
                v_min_dist1 = None
                v_min_dist2 = None

                #Lê as coordenadas de todas as ruas de um caso e monta o grafo
                linha = arq_in.readline().split() #Lê as coordenadas da primeira rua
                while(len(linha) == 4): # Enquanto o que estiver sendo lido for uma coord. de rua
                    coord = [int(linha[0]), int(linha[1]), int(linha[2]), int(linha[3])] # Pts. inicial e final da rua (Xi, Yi, Xf, Yf)
                    u_coord = [coord[0], coord[1]]

                    pos_u = self.pos_vertice(u_coord, verts)
                    if pos_u == -1: # Se o vértice não existir, crie
                        n_verts += 1
                        d = self.dist_coords(pt_de_partida, u_coord)
                        u = Vertice(n_verts, d, float("inf"), None, u_coord)
                        if (d < min_dist1):
                            v_min_dist1 = u
                            min_dist1 = d
                        elif(d < min_dist2):
                            v_min_dist2 = u
                            min_dist2 = d

                        verts.append(u)
                        adj.append([])
                        pos_u  = n_verts

                    v_coord = [coord[2], coord[3]]
                    pos_v = self.pos_vertice(v_coord, verts)
                    if pos_v == -1: # Se o vértice não existir, crieert)):
                        n_verts += 1
                        d = self.dist_coords(pt_de_partida, v_coord)
                        v = Vertice(n_verts, d, float("inf"), None, v_coord)
                        if (d < min_dist1):
                            v_min_dist1 = v
                            min_dist1 = v
                        elif (d < min_dist2):
                            v_min_dist2 = v
                            min_dist2 = d
                        verts.append(v)
                        adj.append([])
                        pos_v = n_verts

                    if self.eq_coord(u_coord, pt_de_partida) or \
                            self.eq_coord(v_coord, pt_de_partida):
                        euleriano = True

                    adj[pos_u].append(verts[pos_v]) # Adicionando nova aresta, considerando o grafo DIRECIONADO
                    adj[pos_v].append(verts[pos_u]) # Idem ao anterior

                    linha = arq_in.readline().split() # Salta linha em branco

                w = self.montar_w(adj, verts)
                g = Grafo(verts, adj, w, None, None, 0, pt_partida,
                          euleriano, v_min_dist1, v_min_dist2)
                self.grafos.append(g)



    # Retorna a posição do vértice em G.V com as coordenadas informadas, -1 se não existir
    def pos_vertice(self, coord, lista_verts):
        for i in range(1, len(lista_verts)):
            if self.eq_coord(coord, lista_verts[i].coord):
                return i
        return -1

    # Calcula a distância entre duas coordenadas
    def dist_coords(self, c1, c2):
        return math.sqrt(math.pow((c2[0] - c1[0]), 2) + math.pow((c2[1] - c1[1]), 2))

    # Cria w a partir de adj, supondo que o peso de (u, v) está em v | v pertence a adj[u]
    def montar_w(self, adj, verts):
        w = []
        n = len(adj)
        for i in range(n):
            w.append(n*[float("inf")])

        for i in range(1, len(adj)):
            for v in adj[i]:
                dist = Vertice.distancia(verts[i], v)
                w[i][v.id] = dist
        return w

    # Verifica se duas coordenadas são iguais
    def eq_coord(self, c1, c2):
        return c1[0] == c2[0] and c1[1] == c2[1]

'''
a = Arquivo("arquivoTesteP2.txt", 2)
for g in a.grafos:
    print(g)
for v in g.vert:
    if v != None:
        print(v.id)

for l in g.w:
    print(l)
'''
