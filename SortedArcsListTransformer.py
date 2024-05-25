from Arc import Arc
from AdjacentList import AdjacentList
from Edge import Edge
from SortedArcsList import SortedArcList

class SortedArcListTransformer:
    def __init__(self, saList: SortedArcList):
        self.saList = saList

    def to_adjacent_list(self) -> AdjacentList:
        adjList = AdjacentList(self.saList.n)
        for i, arc in enumerate(self.saList.arcs):
            newArc = Arc(arc.start, arc.end)
            adjList.add(newArc)
        return adjList