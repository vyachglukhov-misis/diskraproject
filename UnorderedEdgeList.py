from AdjacentList import AdjacentList
from Edge import Edge


class UnorderedEdgeList:
    starts: list[int]
    ends: list[int]
    n: int
    m: int

    @staticmethod
    def from_adjacent_list(adjacent_list: AdjacentList):
        uel = UnorderedEdgeList(adjacent_list.n)
        for i, row in enumerate(adjacent_list.list):
            for j in row:
                uel.add(Edge(i, j))
        return uel

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
