from Edge import Edge


class IncidenceMatrix:
    def __init__(self, num_vertices, num_edges):
        self.v = num_vertices
        self.e = num_edges
        self.matrix = [[0 for _ in range(self.e)] for _ in range(self.v)]

    def add(self, edge_index, edge: Edge):
        self.matrix[edge.start][edge_index] = 1
        self.matrix[edge.end][edge_index] = -1

    def print(self):
        for row in self.matrix:
            print(row)
