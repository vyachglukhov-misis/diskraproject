from AdjacentMatrix import AdjacentMatrix
from AdjacentList import AdjacentList
from Edge import Edge
from IncidenceMatrix import IncidenceMatrix

class AdjacentMatrixTransformer():
    def __init__(self, adjMatrix: AdjacentMatrix):
        self.adjMatrix = adjMatrix

    def to_adjacent_list(self) -> AdjacentList:
        adjList = AdjacentList(self.v)
        for i in range(len(self.adjMatrix)):
            for j in range(len(self.adjMatrix[i])):
                if self.adjMatrix[i][j]:
                    new_edge = Edge(i, j)
                    adjList.add(new_edge)
        return adjList

    def to_incidence_matrix(self) -> IncidenceMatrix:
        edges_count = 0
        for i in range(len(self.adjMatrix)):
            edges_count += sum(self.adjMatrix[i])
        edge_index = 0
        incidence_matrix = IncidenceMatrix(self.v, edges_count)
        for i in range(len(self.adjMatrix)):
            for j in range(len(self.adjMatrix[i])):
                if self.adjMatrix[i][j]:
                    incidence_matrix.add(edge_index, Edge(i, j))
                    edge_index += 1
        return incidence_matrix
