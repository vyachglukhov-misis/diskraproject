class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        if self.start != other.start:
            return self.start < other.start
        else:
            return self.end == other.end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __gt__(self, other):
        return not self.__lt__(other) and not self.__eq__(other)
