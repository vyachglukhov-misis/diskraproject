from AdjacentList import AdjacentList
from Edge import Edge


class EdgeSheavesList:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.starts = []
        self.ends = []
        self.sheaf_heads = [-1 for _ in range(self.n)]
        self.next_edge = [-1 for _ in range(self.m)]

    def add(self, edge: Edge):
        self.starts.append(edge.start)
        self.ends.append(edge.end)

        #когда закончили добавлять ребра, надо обновить значения в sheaf_heades и next_edge
        if len(self.starts) == self.m:
            for i in range(self.m):
                v = self.starts[i]
                self.next_edge[i] = self.sheaf_heads[v]
                self.sheaf_heads[v] = i

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

    def to_adjacent_list(self) -> AdjacentList:
        adj_list = AdjacentList(self.n)

        for i in range(self.n):
            start = self.starts[i]
            end = self.ends[i]

            adj_list.add(Edge(start, end))

        return adj_list


# test
#пример графа и ожидаемого результата на стр 24 учебника
print("From adj list")
adj_list = AdjacentList(4)

adj_list.add(Edge(0, 1))
adj_list.add(Edge(1, 2))
adj_list.add(Edge(2, 3))
adj_list.add(Edge(1, 3))
adj_list.add(Edge(0, 2))

EdgeSheavesList.from_adjacent_list(adj_list).print()

print("From constructor")
esl = EdgeSheavesList(4, 5)

esl.add(Edge(0, 1))
esl.add(Edge(1, 2))
esl.add(Edge(2, 3))
esl.add(Edge(1, 3))
esl.add(Edge(0, 2))

esl.print()

#всё вроде корректно - на бумажке проверил
