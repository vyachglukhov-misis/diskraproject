from Arc import Arc

class SortedArcList:
    def __init__(self, num_v):
        self.arcs = []
        self.n = num_v

    def add_arc(self, arc: Arc):
        self.arcs.append(arc)
        self.arcs.sort()

    def print_arcs(self):
        for arc in self.arcs:
            print(f"Start: {arc.start}, End: {arc.end}")
