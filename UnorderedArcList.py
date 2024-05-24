from AdjacentList import AdjacentList
from Edge import Edge

class UnorderedArcList:
    def __init__(self, v):
        self.edges = []
        self.v = v

    def add(self, edge):
        self.edges.append(edge)

    def print_bundle(self):
        for edge in self.edges:
            print(f"Start: {edge.start}, End: {edge.end}")

    def to_adjacent_list(self):
        adjList = AdjacentList(self.v)
        for i, edge in enumerate(self.edges):
            edge = Edge(edge.start, edge.end)
            adjList.add(edge)
        return adjList
    
