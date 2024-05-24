class Arc:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class UnorderedArcList:
    def __init__(self):
        self.arcs = []

    def add_arc(self, arc):
        self.arcs.append(arc)

    def print_arcs(self):
        for arc in self.arcs:
            print(f"Start: {arc.start}, End: {arc.end}")
