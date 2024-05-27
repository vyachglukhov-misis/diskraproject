from Edge import Edge
from AdjacentList import AdjacentList

'''
    Отсортированный список дуг

    Представляет собой два массива starts и ends - начало и конец i-ой дуги соответсвенно, 
    отсортированные по вершинам: приоритет сортировки исток потом сток
    Обход всех дуг O(m)
    Просмотр дуги O(1)
    Просмотр пучка дуг O(m) при использовании бин поиска
    Нахождение дуги по истоку O(log n) или O(1) при использовании доп хеш таблицы 
    Построение О(m**2) на самом деле можно за O(n log n) если использовать бинарное дерево
'''


class OrderedEdgeList:
    starts: list[int]
    ends: list[int]
    n: int
    m: int

    @staticmethod
    def from_adjacent_list(adjacent_list: AdjacentList):
        oel = OrderedEdgeList(adjacent_list.n)
        for i, row in enumerate(adjacent_list.list):
            for j in row:
                oel.add(Edge(i, j))
        return oel
    
    def __init__(self, n):
        self.n = n
        self.starts = []
        self.ends = []
        self.m = 0

    def add(self, edge: Edge):
        assert edge.start < self.n
        assert edge.end < self.n
        self.starts.append(edge.start)
        self.ends.append(edge.end)
        self.m += 1

    def print(self):
        for i in range(len(self.starts)):
            print(f"Start: {self.starts[i]}, End: {self.ends[i]}")

    def to_adjacent_list(self) -> AdjacentList:
        adj_list = AdjacentList(self.n)
        for i in range(len(self.starts)):
            adj_list.add(Edge(self.starts[i], self.ends[i]))

        return adj_list
# # Test
# s = OrderedEdgeList(10)
# s.add(Edge(1, 2))
# s.add(Edge(2, 4))
# s.add(Edge(0, 2))
# s.print()
