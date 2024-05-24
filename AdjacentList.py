import AdjacentMatrix
import IncidenceMatrix
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

    def to_adjacent_matrix(self):
        am = AdjacentMatrix.AdjacentMatrix(self.n)
        for i, row in enumerate(self.list):
            for j, has_edge in enumerate(row):
                if has_edge:
                    am.add(Edge(i, j))
        return am


    # def to_incidence_matrix(self):
    #     edges_count = 0
    #     for i in range(len(self.list)):
    #         edges_count += sum(self.list[i])
    #     incidence_matrix = IncidenceMatrix.IncidenceMatrix(self.n, edges_count)
    #     edge_num = 0
    #     for i in range(len(self.list)):
    #         for j in range(len(self.list[i])):
    #             incidence_matrix.add(edge_num, i, j)
    #             edge_num += 1
    #     return incidence_matrix
