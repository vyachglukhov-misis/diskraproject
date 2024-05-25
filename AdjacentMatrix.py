from Edge import Edge


class AdjacentMatrix:
    def __init__(self, v):
        self.matrix = [[False for _ in range(v)] for _ in range(v)]
        self.v = v

    def add(self, edge: Edge):
        self.matrix[edge.start][edge.end] = True

    def print(self):
        for i in self.matrix:
            print(' '.join(['1' if j else '0' for j in i]))

