from Edge import Edge


class AdjacentList:
    def __init__(self, n):
        self.list = [set() for _ in range(n)]
        self.n = n
        self.m = 0

    def to_adjacent_list(self):
        return self

    @staticmethod
    def from_adjacent_list(self):
        return self

    def add(self, edge: Edge):
        self.list[edge.start].add(edge.end)
        self.m += 1

    def print(self):
        for i in self.list:
            print(' '.join(str(i)))


    # def to_adjacent_matrix(self):
    #     am = AdjacentMatrix.AdjacentMatrix(self.n)
    #     for i, row in enumerate(self.list):
    #         for j, has_edge in enumerate(row):
    #             if has_edge:
    #                 am.add(Edge(i, j))
    #     return am

    # def to_unordered_arc_list(self):
    #     unordered_arc_list = UnorderedArcList(self.n)
    #     for i, row in enumerate(self.list):
    #         for j, has_edge in enumerate(row):
    #             if has_edge:
    #                 unordered_arc_list.add(Edge(i, j))
    #     return unordered_arc_list
    #
    # def to_ordered_arc_list(self):
    #     ordered_arc_list = SortedArcList(self.n)
    #     for i, row in enumerate(self.list):
    #         for j, has_edge in enumerate(row):
    #             if has_edge:
    #                 ordered_arc_list.add(Arc(i, j))
    #     return ordered_arc_list
    #
    # # def to_incidence_matrix(self):
    # #     edges_count = 0
    # #     for i in range(len(self.list)):
    # #         edges_count += sum(self.list[i])
    # #     incidence_matrix = IncidenceMatrix.IncidenceMatrix(self.n, edges_count)
    # #     edge_num = 0
    # #     for i in range(len(self.list)):
    # #         for j in range(len(self.list[i])):
    # #             incidence_matrix.add(edge_num, i, j)
    # #             edge_num += 1
    # #     return incidence_matrix
    #
    # def to_incidence_matrix(self):
    #     edge_count = 0
    #     for _, v_verticles in enumerate(self.list):
    #         edge_count += len(v_verticles)
    #     incidence_matrix = IncidenceMatrix(self.n, edge_count)
    #     edge_index = 0
    #     for v_from, _ in enumerate(self.list):
    #         for _, v_to in enumerate(v_from):
    #             incidence_matrix.add(edge_index, Edge(v_from, v_to))
    #             edge_index += 1
    #     return incidence_matrix
