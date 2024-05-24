from . import ListSmezhnosti, MatrixSmezh

class IncidenceMatrix:
    def __init__(self, num_vertices, num_edges):
        self.v = num_vertices
        self.e = num_edges
        self.matrix = [[0 for j in range(self.v)] for i in range(self.e)]

    def add_edge(self, edge_index, start_vertex, end_vertex):
        self.matrix[start_vertex][edge_index] = 1
        self.matrix[end_vertex][edge_index] = -1

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def toMatrixSmezh(self):
        matrixSmezh = MatrixSmezh.MatrixSmezhnosti(self.v)
        for i in range(self.v):
            start_point = 0
            end_point = 0
            for j in range(self.e):
                if self.matrix[j][i] == 1:
                    start_point = j
                if self.matrix[j][i] == -1:
                    end_point = j
            if start_point == 1 and end_point == -1:
                edge = MatrixSmezh.Edge(start_point, end_point)
                matrixSmezh.add_edge(edge)
    
    def toListSmezh(self): 
        listSmezh = ListSmezhnosti.ListSmezhnosti()
        for i in range(self.v):
            start_point = 0
            end_point = 0
            for j in range(self.e):
                if self.matrix[j][i] == 1:
                    start_point = j
                if self.matrix[j][i] == -1:
                    end_point = j
            if start_point == 1 and end_point == -1:
                edge = ListSmezhnosti.Edge(start_point, end_point)
                listSmezh.add_edge(edge)

