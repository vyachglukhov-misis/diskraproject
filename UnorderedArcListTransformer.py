from AdjacentList import AdjacentList
from Edge import Edge
from UnorderedArcList import UnorderedArcList

class UnorderedArcListTransformer:
    def __init__(self, uoaList: UnorderedArcList):
        self.uoaList = uoaList

    def to_adjacent_list(self) -> AdjacentList:
        adjList = AdjacentList(self.uoaList.v)
        for i, edge in enumerate(self.uoaList.edges):
            new_edge = Edge(edge.start, edge.end)
            adjList.add(new_edge)
        return adjList
    

