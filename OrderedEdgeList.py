from Edge import Edge
from UnorderedEdgeList import UnorderedEdgeList
from AdjacentList import AdjacentList


class OrderedEdgeList():
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

    def add(self, edge: Edge):
        # Еще можно бин поиском
        i = len(self.starts) - 1
        while i >= 0 and Edge(self.starts[i], self.ends[i]) > edge:
            i -= 1

        self.starts.insert(i + 1, edge.start)
        self.ends.insert(i + 1, edge.end)
        self.m += 1

    def print(self):
        for i in range(len(self.starts)):
            print(f"Start: {self.starts[i]}, End: {self.ends[i]}")

    def to_adjacent_list(self) -> AdjacentList:
        adj_list = AdjacentList(self.n)
        for i in range(len(self.starts)):
            adj_list.add(Edge(self.starts[i], self.ends[i]))

        return adj_list
