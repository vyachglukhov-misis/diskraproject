from Edge import Edge


class AdjacentList:
    def __init__(self, n):
        self.list = [set() for _ in range(n)]
        self.n = n

    def add(self, edge: Edge):
        self.list[edge.start].add(edge.end)

    def print(self):
        for i in self.list:
            print(' '.join(i))
