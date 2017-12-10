# coding=utf-8
class MaxHeap:
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

        # Para saber a posição do objeto no MaxHeap
        lista[i].indice = i
        lista[j].indice = j

    @staticmethod
    def __heapify(lista, i):
        e = MaxHeap.__esquerdo(i)
        d = MaxHeap.__direito(i)

        maior = i
        if e < MaxHeap.size and lista[e] > lista[i]:
            maior =  e
        if d < MaxHeap.size and lista[d] > lista[maior]:
            maior = d
        if maior != i:
            MaxHeap.__trocar(lista, i, maior)
            MaxHeap.__heapify(lista, maior)

    @staticmethod
    def build_max_heap(lista):
        MaxHeap.size = len(lista)
        for i in reversed(range(0, MaxHeap.size/2)):
            MaxHeap.__heapify(lista, i)

    @staticmethod
    def maximum(lista):
        return lista[0]

    @staticmethod
    def extract_max(lista):
        if MaxHeap.size < 1:
            return "Erro: heap underflow!"
        max = lista[0]
        MaxHeap.__trocar(lista, 0, MaxHeap.size - 1)
        del lista[MaxHeap.size - 1]
        MaxHeap.size -= 1
        MaxHeap.__heapify(lista, 0)
        return max

    @staticmethod
    def increase_key(lista, pos):
        while (pos > 0) and (lista[MaxHeap.__pai(pos)] < lista[pos]):
            MaxHeap.__trocar(lista, pos, MaxHeap.__pai(pos))
            pos = MaxHeap.__pai(pos)

