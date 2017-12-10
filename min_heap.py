# coding=utf-8
from vertice import Vertice
class MinHeap:
    size = 0

    @staticmethod
    def __pai(i):
        return (i - 1)/2

    @staticmethod
    def __esquerdo(i):
        return 2*i + 1

    @staticmethod
    def __direito(i):
        return 2*i + 2

    @staticmethod
    def __trocar(lista, i, j):
        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp

        # Para saber a posição do objeto no MinHeap
        lista[i].indice = i
        lista[j].indice = j

    @staticmethod
    def __heapify(lista, i):
        e = MinHeap.__esquerdo(i)
        d = MinHeap.__direito(i)

        maior = i
        if e < MinHeap.size and lista[e] < lista[i]:
            maior =  e
        if d < MinHeap.size and lista[d] < lista[maior]:
            maior = d
        if maior != i:
            MinHeap.__trocar(lista, i, maior)
            MinHeap.__heapify(lista, maior)

    @staticmethod
    def build_min_heap(lista):
        MinHeap.size = len(lista)
        for i in reversed(range(0, MinHeap.size/2)):
            MinHeap.__heapify(lista, i)

    @staticmethod
    def minimum(lista):
        return lista[0]

    @staticmethod
    def extract_min(lista):
        if MinHeap.size < 1:
            return "Erro: heap underflow!"
        max = lista[0]
        MinHeap.__trocar(lista, 0, MinHeap.size - 1)
        del lista[MinHeap.size - 1]
        MinHeap.size -= 1
        MinHeap.__heapify(lista, 0)
        return max

    @staticmethod
    def decrease_key(lista, pos):
        while (pos > 0) and (lista[MinHeap.__pai(pos)] > lista[pos]):
            MinHeap.__trocar(lista, pos, MinHeap.__pai(pos))
            pos = MinHeap.__pai(pos)

