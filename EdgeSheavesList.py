from AdjacentList import AdjacentList
from Edge import Edge

'''
    Список пучков дуг
    
    Каждый пучок дуг будет представлен в виде одностороннего списка, sheaf_heads[i] – номер первой дуги в списке дуг,
    выходящих из вершины i, next_edge[i] – номер следующей в списке дуги, выходящей из той же вершины, что и дуга k.
    
    Трудоемкость обхода пучка дуг - такая же, как и для упорядоченного списка: пропорциональна количеству дуг пучка
    
    просмотр дуги - O(1)
    
    сложность построения - O(m)
'''


class EdgeSheavesList:
    def __init__(self, n, m):
        # количество вершин
        self.n = n
        # количество дуг
        self.m = m
        # массив начал дуг. Например, если есть дуги (0,1), (0,2), то starts = [0, 0]
        self.starts = []
        # массив концов дуг. Например, если есть дуги (0,1), (0,2), то ends = [1, 2]
        self.ends = []
        # sheaf_heads[i] хранит номер первой дуги в списке дуг
        self.sheaf_heads = [-1 for _ in range(self.n)]
        # next_edge[i] – номер следующей в списке дуги
        self.next_edge = [-1 for _ in range(self.m)]

    # метод добавления дуги
    def add(self, edge: Edge):
        self.starts.append(edge.start)
        self.ends.append(edge.end)

        # когда закончили добавлять дуги, надо обновить значения в sheaf_heades и next_edge
        if len(self.starts) == self.m:
            for i in range(self.m):
                v = self.starts[i]
                self.next_edge[i] = self.sheaf_heads[v]
                self.sheaf_heads[v] = i

    # статический метод по конвертации списка смежности в список пучков дуг, ассимптотика O(n+m)
    @staticmethod
    def from_adjacent_list(adj_list: AdjacentList):
        edges_count = 0
        for edges in adj_list.list:
            edges_count += len(edges)

        esl = EdgeSheavesList(adj_list.n, edges_count)

        for v_from, to_list in enumerate(adj_list.list):
            for _, v_to in enumerate(to_list):
                esl.add(Edge(v_from, v_to))

        return esl

    # обход списка пучков дуг с выводом всей информации на экран
    def print(self):
        for i in range(self.n):
            # просмотр пучка дуг, выходящих из вершины i
            k = self.sheaf_heads[i]
            while k != -1:
                print(self.starts[k], self.ends[k])
                k = self.next_edge[k]

        print("heads: ")
        for sheaf_head in self.sheaf_heads:
            print(sheaf_head)

        print("next edge: ")
        for edge_end in self.next_edge:
            print(edge_end)

    # конвертация списка пучков дуг в список смежности, ассимптотика O(m)
    def to_adjacent_list(self) -> AdjacentList:
        adj_list = AdjacentList(self.n)

        for i in range(self.m):
            start = self.starts[i]
            end = self.ends[i]

            adj_list.add(Edge(start, end))

        return adj_list


'''
пример построение графа

входные данные: вершины - 4, ребер - 5, ребра: (0, 1), (1, 2), (2, 3), (1, 3), (0, 2).
значения полей: starts = [0,1,2,1,0], ends = [1,2,3,3,2], heads = [4,3,2,-1], next_edge=[-1,-1,-1,1,0]
'''
