from AdjacentList import AdjacentList
import ArcSheavesList
from Edge import Edge

class ArcSheavesList:
    def __init__(self, arcSheavesList: ArcSheavesList):
        self.arcSheavesList = arcSheavesList
    
    def to_adjacent_list(self) -> AdjacentList:
        adjacent_list = AdjacentList(self.arcSheavesList.n)

        for i in range(self.arcSheavesList.n):
            start = self.arcSheavesList.I[i]
            end = self.arcSheavesList.J[i]

            adjacent_list.add(Edge(start, end))

        return adjacent_list