from AdjacentList import AdjacentList
from Edge import Edge


class IncidenceMatrix:
    def __init__(self, num_vertices, num_edges):
        self.n = num_vertices
        self.e = num_edges
        self.matrix = [[0 for _ in range(self.e)] for _ in range(self.n)]

    @staticmethod
    def from_adjacent_list(adjacent_list: AdjacentList):
        edge_count = 0
        for i in adjacent_list.list:
            edge_count += len(i)

        inc_matrix = IncidenceMatrix(adjacent_list.n, edge_count)
        edge_index = 0
        for i, row in enumerate(adjacent_list.list):
            for j in row:
                inc_matrix.add(edge_index, Edge(i, j))
                edge_index += 1

        return inc_matrix

    def add(self, edge_index, edge: Edge):
        self.matrix[edge.start][edge_index] = 1
        self.matrix[edge.end][edge_index] = -1

    def print(self):
        for row in self.matrix:
            print(row)

    # def to_adjacent_matrix(self) -> AdjacentMatrix:
    #     adjacent_matrix = AdjacentMatrix(self.v)
    #     for e in range(self.e):
    #         edge = Edge(-1, -1)
    #         for v in range(self.v):
    #             if self.matrix[v][e] == 1:
    #                 edge.start = v
    #             if self.matrix[v][e] == -1:
    #                 edge.end = v
    #         if edge.start != -1 and edge.end != -1:
    #             adjacent_matrix.add(edge)
    #         else:
    #             raise 'Stranno netu rebra'
    #     return adjacent_matrix

    def to_adjacent_list(self):
        adjacent_list = AdjacentList(self.n)
        for e in range(self.e):
            edge = Edge(-1, -1)
            for v in range(self.n):
                if self.matrix[v][e] == 1:
                    edge.start = v
                if self.matrix[v][e] == -1:
                    edge.end = v
            if edge.start != -1 and edge.end != -1:
                adjacent_list.add(edge)
            else:
                raise 'Stranno netu rebra'

        return adjacent_list
