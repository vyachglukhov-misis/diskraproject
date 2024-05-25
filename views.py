from AdjacentList import AdjacentList
from AdjacentMatrix import AdjacentMatrix
from IncidenceMatrix import IncidenceMatrix
from SortedArcsList import SortedArcList
from UnorderedArcList import UnorderedArcList
from ArcSheavesList import ArcSheavesList
from Edge import Edge
from Arc import Arc


class ViewTransformerUtil:
    @staticmethod
    def adj_matrix_to_adj_list(adj_matrix: AdjacentMatrix) -> AdjacentList:
        converting = AdjacentList(adj_matrix.v)
        for i in range(len(adj_matrix.matrix)):
            for j in range(len(adj_matrix.matrix[i])):
                if adj_matrix.matrix[i][j]:
                    new_edge = Edge(i, j)
                    converting.add(new_edge)
        return converting

    @staticmethod
    def sorted_arc_list_to_adj_list(sorted_arc_list: SortedArcList) -> AdjacentList:
        adj_list = AdjacentList(sorted_arc_list.n)
        for i, edge in enumerate(sorted_arc_list.arcs):
            edge = Edge(edge.start, edge.end)
            adj_list.add(edge)
        return adj_list

    @staticmethod
    def unordered_arc_list_to_adj_list(unordered_arc_list: UnorderedArcList) -> AdjacentList:
        adj_list = AdjacentList(unordered_arc_list.v)
        for i, edge in enumerate(unordered_arc_list.edges):
            edge = Edge(edge.start, edge.end)
            adj_list.add(edge)
        return adj_list

    @staticmethod
    def incidence_matrix_to_adj_list(incidence_matrix: IncidenceMatrix) -> AdjacentList:
        adj_list = AdjacentList(incidence_matrix.v)
        for e in range(incidence_matrix.e):
            edge = Edge(-1, -1)
            for v in range(incidence_matrix.v):
                if incidence_matrix.matrix[v][e] == 1:
                    edge.start = v
                if incidence_matrix.matrix[v][e] == -1:
                    edge.end = v
            if edge.start != -1 and edge.end != -1:
                adj_list.add(edge)
            else:
                raise 'Stranno netu rebra'
        return adj_list

    @staticmethod
    def arc_sheaves_list_to_adj_list(arc_sheave_list: ArcSheavesList) -> AdjacentList:
        adjacent_list = AdjacentList(arc_sheave_list.n)

        for i in range(arc_sheave_list.n):
            start = arc_sheave_list.I[i]
            end = arc_sheave_list.J[i]

            adjacent_list.add(Edge(start, end))

        return adjacent_list

    @staticmethod
    def adj_list_to_adj_matrix(adj_list: AdjacentList) -> AdjacentMatrix:
        am = AdjacentMatrix(adj_list.n)
        for i, row in enumerate(adj_list.list):
            for j, has_edge in enumerate(row):
                if has_edge:
                    am.add(Edge(i, j))
        return am

    @staticmethod
    def adj_list_to_unordered_arc_list(adj_list: AdjacentList) -> UnorderedArcList:
        unorderedArcList = UnorderedArcList(adj_list.n)
        for i, row in enumerate(adj_list.list):
            for j, has_edge in enumerate(adj_list, list):
                if has_edge:
                    unorderedArcList.add(Edge(i, j))
        return unorderedArcList

    @staticmethod
    def adj_list_to_ordered_arc_list(adj_list):
        orderedArcList = SortedArcList(adj_list.n)
        for i, row in enumerate(adj_list.list):
            for j, has_edge in enumerate(adj_list, list):
                if has_edge:
                    orderedArcList.add(Arc(i, j))
        return orderedArcList

    @staticmethod
    def adj_list_to_incidence_matrix(adj_list):
        edge_count = 0
        for _, v_verticles in enumerate(adj_list.list):
            edge_count += len(v_verticles)
        incidenceMatrix = IncidenceMatrix(adj_list.n, edge_count)
        edge_index = 0
        for v_from, _ in enumerate(adj_list.list):
            for _, v_to in enumerate(v_from):
                incidenceMatrix.add(edge_index, Edge(v_from, v_to))
                edge_index += 1
        return incidenceMatrix

    @staticmethod
    def adj_list_to_arc_sheaves_list(adj_list:AdjacentList) -> ArcSheavesList:
        edges = []
        for v_from, to_list in enumerate(adj_list.list):
            for _, v_to in enumerate(to_list):
                edges.append(Edge(v_from, v_to))

        return ArcSheavesList(adj_list.n, edges)

