from AdjacentList import AdjacentList
from Edge import Edge


class IncidenceMatrix:

    # Матрица инцидентности — одна из форм представления графа, в которой указываются связи между
    # инцидентными элементами графа (ребро(дуга) и вершина).
    # Столбцы матрицы соответствуют ребрам, строки — вершинам.
    # Ненулевое значение в ячейке матрицы указывает связь между вершиной и ребром (их инцидентность).
    # В случае ориентированного графа каждой дуге <x,y> ставится в соответствующем столбце: «1» в строке вершины x и «-1» в строке вершины y;
    # если связи между вершиной и ребром нет, то в соответствующую ячейку ставится «0».

    # Из особенностей: может использоваться для представления гиперграфов

    # Представление: идёт соотношение ребра в котором состоят две вершины и самих вершин,
    # причем из которой выходит ставится -1, в которую входит ставится 1 
    # сам граф: https://present5.com/presentation/3/816642_58668781.pdf-img/816642_58668781.pdf-4.jpg
    #
    #    e1 e2 e3 e4 e5 e6
    # v1  1  0  0  0  0  0
    # v2 -1  1  1  1  0  0
    # v3  0 -1  0  0  0  1
    # v4  0  0 -1  0  1 -1
    # v5  0  0  0 -1 -1  0


    # чтобы создать экземпляр классса IncidenceMatrix, необходимо указать количество вершин и количество рёбер
    def __init__(self, num_vertices, num_edges):
        self.n = num_vertices
        self.e = num_edges
        self.matrix = [[0 for _ in range(self.e)] for _ in range(self.n)]

    # статический метод для перевода AdjacentList -> IncidenceMatrix в классе Transformer
    @staticmethod
    def from_adjacent_list(adjacent_list: AdjacentList):
        edge_count = 0
        for i in adjacent_list.list:
            edge_count += len(i)

        inc_matrix = IncidenceMatrix(adjacent_list.n, edge_count)
        edge_index = 0
        for i, row in enumerate(adjacent_list.list):
            for j in row:
                inc_matrix.add(edge_index, Edge(i, j))
                edge_index += 1

        return inc_matrix

    # функция для добавления вершины
    def add(self, edge_index, edge: Edge):
        self.matrix[edge.start][edge_index] = 1
        self.matrix[edge.end][edge_index] = -1
    
    # функция для вывода матрицы
    def print(self):
        for row in self.matrix:
            print(row)

    # функция для конвертации в список смежности
    def to_adjacent_list(self):
        adjacent_list = AdjacentList(self.n)
        for e in range(self.e):
            edge = Edge(-1, -1)
            for v in range(self.n):
                if self.matrix[v][e] == 1:
                    edge.start = v
                if self.matrix[v][e] == -1:
                    edge.end = v
            if edge.start != -1 and edge.end != -1:
                adjacent_list.add(edge)
            else:
                raise 'Stranno netu rebra'

        return adjacent_list
