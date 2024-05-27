from Edge import Edge
from UnorderedEdgeList import UnorderedEdgeList

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


class OrderedEdgeList(UnorderedEdgeList):
    def __init__(self, n):
        super().__init__(n)

    def add(self, edge: Edge):
        # Еще можно бин поиском но сложность все равно останется линейной изза вставки
        i = len(self.starts) - 1
        while i >= 0 and Edge(self.starts[i], self.ends[i]) > edge:
            i -= 1

        self.starts.insert(i + 1, edge.start)
        self.ends.insert(i + 1, edge.end)
        self.m += 1


# # Test
# s = OrderedEdgeList(10)
# s.add(Edge(1, 2))
# s.add(Edge(2, 4))
# s.add(Edge(0, 2))
# s.print()
