from OrderedEdgeList import OrderedEdgeList
from AdjacentList import AdjacentList
from Edge import Edge


class EdgeSheavesList:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.starts = [-1 for _ in range(m)]
        self.ends = [-1 for _ in range(m)]
        self.sheave_heads = [-1 for _ in range(n)]
        self.next_edge = [-1 for _ in range(m)]
        self.oel = None

    @staticmethod
    def from_adjacent_list(adjacent_list: AdjacentList):
        oel = OrderedEdgeList.from_adjacent_list(adjacent_list)
        esl = EdgeSheavesList(adjacent_list.n, adjacent_list.m)
        edge_index = 0
        sheave_index = -1
        last_source = -1
        for i in range(oel.m):
            if last_source != oel.starts[i]:
                last_source = oel.starts[i]
                sheave_index += 1
                esl.sheave_heads[oel.starts[i]] = i
                continue
            esl.next_edge[i - 1] = i

        for i, row in oel.list:
            esl.sheave_heads[i] = edge_index
            for j in range(1, len(row)):
                esl.next_edge[edge_index] = edge_index + 1
                edge_index += 1
        esl.oel = oel
        return esl

    def print(self):
        for i in range(self.n):
            # просмотр пучка дуг, выходящих из вершины i
            k = self.sheave_heads[i]
            while k != -1:
                print(self.starts[k], self.ends[k])
                k = self.next_edge[k]

    def to_adjacent_list(self) -> AdjacentList:
        adjacent_list = AdjacentList(self.n)

        for i in range(self.n):
            start = self.starts[i]
            end = self.ends[i]

            adjacent_list.add(Edge(start, end))

        return adjacent_list


arc = EdgeSheavesList(4, 5)

arc.print()
