from AdjacentList import AdjacentList


class SortedArcList:
    def __init__(self, num_v):
        self.arcs = []
        self.n = num_v

    def add(self, arc):
        self.arcs.append(arc)
        self.arcs.sort()

    def print_arcs(self):
        for arc in self.arcs:
            print(f"Start: {arc.start}, End: {arc.end}")

    def to_adjacent_list(self) -> AdjacentList:
        adj_list = AdjacentList(self.v)
        for i, edge in enumerate(self.edges):
            edge = Edge(edge.start, edge.end)
            adj_list.add(edge)
        return adj_list
