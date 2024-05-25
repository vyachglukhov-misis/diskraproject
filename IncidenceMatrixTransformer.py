from AdjacentList import AdjacentList
from AdjacentMatrix import AdjacentMatrix
from Edge import Edge
from IncidenceMatrix import IncidenceMatrix


class IncidenceMatrixTransformer:
    def __init__(self, incidMatrix: IncidenceMatrix):
        self.incidMatrix = incidMatrix

    def to_adjacent_matrix(self) -> AdjacentMatrix:
        adjacent_matrix = AdjacentMatrix(self.incidMatrix.v)
        for e in range(self.incidMatrix.e):
            edge = Edge(-1, -1)
            for v in range(self.incidMatrix.v):
                if self.incidMatrix.matrix[v][e] == 1:
                    edge.start = v
                if self.incidMatrix.matrix[v][e] == -1:
                    edge.end = v
            if edge.start != -1 and edge.end != -1:
                adjacent_matrix.add(edge)
            else:
                raise 'Stranno netu rebra'
        return adjacent_matrix

    def to_adjacent_list(self):
        adjacent_list = AdjacentList(self.incidMatrix.v)
        for e in range(self.incidMatrix.e):
            edge = Edge(-1, -1)
            for v in range(self.incidMatrix.v):
                if self.incidMatrix.matrix[v][e] == 1:
                    edge.start = v
                if self.incidMatrix.matrix[v][e] == -1:
                    edge.end = v
            if edge.start != -1 and edge.end != -1:
                adjacent_list.add(edge)
            else:
                raise 'Stranno netu rebra'
        return adjacent_list
