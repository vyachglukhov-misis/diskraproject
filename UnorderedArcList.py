from Edge import Edge


class UnorderedArcList:
    def __init__(self, v):
        self.edges = []
        self.v = v

    def add(self, edge: Edge):
        self.edges.append(edge)

    def print_bundle(self):
        for edge in self.edges:
            print(f"Start: {edge.start}, End: {edge.end}")
