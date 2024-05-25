from Edge import Edge
from UnorderedEdgeList import UnorderedEdgeList


class OrderedEdgeList(UnorderedEdgeList):
    def __init__(self, n):
        super().__init__(n)

    def add(self, edge: Edge):
        # Еще можно бин поиском
        i = len(self.starts) - 1
        while i >= 0 and Edge(self.starts[i], self.ends[i]) > edge:
            i -= 1

        self.starts.insert(i + 1, edge.start)
        self.ends.insert(i + 1, edge.end)
        self.m += 1


# Test
s = OrderedEdgeList(10)
s.add(Edge(1, 2))
s.add(Edge(2, 4))
s.add(Edge(0, 2))
s.print()
