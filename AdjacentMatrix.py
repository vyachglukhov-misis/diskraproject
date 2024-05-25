from Edge import Edge
from IncidenceMatrix import IncidenceMatrix
from AdjacentList import AdjacentList


class AdjacentMatrix:
    def __init__(self, v):
        self.matrix = [[False for _ in range(v)] for _ in range(v)]
        self.v = v

    def add(self, edge):
        self.matrix[edge.start][edge.end] = True

    def print(self):
        for i in self.matrix:
            print(' '.join(['1' if j else '0' for j in i]))

    def to_adjacent_list(self):
        converting = AdjacentList(self.v)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]:
                    new_edge = Edge(i, j)
                    converting.add(new_edge)
        return converting

    def to_incidence_matrix(self):
        edges_count = 0
        for row in self.matrix:
            edges_count += sum(row)
        edge_index = 0
        incidence_matrix = IncidenceMatrix(self.v, edges_count)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]:
                    incidence_matrix.add(edge_index, Edge(i, j))
                    edge_index += 1
        return incidence_matrix
