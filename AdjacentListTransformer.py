from AdjacentList import AdjacentList
from AdjacentMatrix import AdjacentMatrix
from UnorderedArcList import UnorderedArcList
from SortedArcsList import SortedArcList
from Edge import Edge
from Arc import Arc
from IncidenceMatrix import IncidenceMatrix

class AdjacentListTransformer:
    def __init__(self, adjList: AdjacentList):
        self.adjList = adjList

    def to_adjacent_matrix(self):
        am = AdjacentMatrix(self.adjList.n)
        for i, row in enumerate(self.adjList):
            for j, has_edge in enumerate(row):
                if has_edge:
                    am.add(Edge(i, j))
        return am
    
    def to_unordered_arc_list(self):
        unorderedArcList = UnorderedArcList(self.adjList.n)
        for i, row in enumerate(self.adjList):
            for j, has_edge in enumerate(row):
                if has_edge:
                    unorderedArcList.add(Edge(i, j))
        return unorderedArcList
    
    def to_ordered_arc_list(self):
        orderedArcList = SortedArcList(self.adjList.n)
        for i, row in enumerate(self.adjList):
            for j, has_edge in enumerate(row):
                if has_edge:
                    orderedArcList.add(Arc(i, j))
        return orderedArcList

    def to_incidence_matrix(self):
        edge_count = 0
        for _, v_verticles in enumerate(self.adjList):
            edge_count += len(v_verticles)
        incidenceMatrix = IncidenceMatrix(self.adjList.n, edge_count)
        edge_index = 0
        for v_from, _ in enumerate(self.adjList):
            for _, v_to in enumerate(v_from):
                incidenceMatrix.add(edge_index, Edge(v_from, v_to))
                edge_index += 1
        return incidenceMatrix