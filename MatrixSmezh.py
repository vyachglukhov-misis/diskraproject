from . import ListSmezhnosti, IncidenceMatrix
class Edge:
    def __init__(self, start, end): 
        self.start = start
        self.end = end


class MatrixSmezhnosti:
    def __init__(self, v):
        self.matrix = [[0 for j in range(v)] for i in range(v)]
        self.v = v

    def add_edge(self, edge):
        self.matrix[edge.start][edge.end] = 1

    def print_Matrix(self):
        for i in range(len(self.matrix)):
            print(' '.join(self.matrix[i]))

    def toListSmezhnosti(self):
        converting = ListSmezhnosti.ListSmezhnosti(self.v)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if(self.matrix[i][j] == 1):
                    new_edge = Edge(i, j)
                    converting.add_edge(new_edge)
        return converting

    def toIncidenceMatrix(self):
        edges_count = 0
        for i in range(len(self.matrix)):
            edges_count += sum(self.matrix[i])
        edge_num = 0
        incidenceMatrix = IncidenceMatrix.IncidenceMatrix(self.v, edges_count)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if(self.matrix[i][j] == 1):
                    incidenceMatrix.add_edge(edge_num, i, j)
                    edge_num += 1
        return incidenceMatrix