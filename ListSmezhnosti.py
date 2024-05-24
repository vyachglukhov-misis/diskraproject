from . import MatrixSmezh, IncidenceMatrix

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class ListSmezhnosti:
    def __init__(self, v):
        self.list = [[] for i in range(v)]
        self.v = v

    def add_edge(self, edge):
        self.list[edge.start].append(edge.end)

    def print_bundle(self):
        for i in self.list:
            print(' '.join(self.list[i]))

    def toMatrixSmezh(self):
        new_matrix = MatrixSmezh.MatrixSmezhnosti(self.v)
        for i in range(len(self.list)):
            for j in range(len(self.list[i])):
                new_matrix[i][self.list[i][j]] = 1
        return new_matrix
    
    def toIncidenceMatrix(self):
        edges_count = 0
        for i in range(len(self.list)):
            edges_count += sum(self.list[i])
        incidenceMatrix = IncidenceMatrix.IncidenceMatrix(self.v, edges_count)
        edge_num = 0
        for i in range(len(self.list)):
            for j in range(len(self.list[i])):
                incidenceMatrix.add_edge(edge_num, i, j)
                edge_num += 1
        return incidenceMatrix
        