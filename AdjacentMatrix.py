from Edge import Edge
from AdjacentList import AdjacentList

"""
    Матрица смежности
    
    это квадратная целочисленная матрица matrix размера n x n, в которой значение элемента matrix[i][j] 
    равно булеву значению: 0, если из i-й вершины графа нет ребра в j-ю вершину, и 1, если наоборот. 
    
    минус матрицы смежности - высокое использование памяти - O(n^2) (где n - кол-во вершин), даже если граф - разряженный
    
    доступ к ребрам - O(1)
    
    пример построение графа:
    входные данные: вершины - 4, ребер - 5, ребра: (0, 1), (1, 2), (2, 3), (1, 3), (0, 4)
    
"""
class AdjacentMatrix:
    def __init__(self, v):
        self.matrix = [[False for _ in range(v)] for _ in range(v)]
        self.n = v

    # конвретация из списка смежности в матрицу смежности
    @staticmethod
    def from_adjacent_list(adjacent_list: AdjacentList):
        adj_matrix = AdjacentMatrix(adjacent_list.n)
        for i, row in enumerate(adjacent_list.list):
            for j in row:
                adj_matrix.add(Edge(i, j))
        return adj_matrix

    # добавление ребра - O(1)
    def add(self, edge):
        self.matrix[edge.start][edge.end] = True

    # обход матрицы с выводом на экран - O(n)
    def print(self):
        for i in self.matrix:
            print(' '.join(['1' if j else '0' for j in i]))

    # конвертация из матрицы смежности в список смежности O(n^2)
    def to_adjacent_list(self):
        adj_list = AdjacentList(self.n)
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j]:
                    adj_list.add(Edge(i, j))
        return adj_list

'''
пример построение графа

входные данные: вершины - 4, ребер - 5, ребра: (0, 1), (1, 2), (2, 3), (1, 3), (0, 2).
получим матрицу

0 1 1 0
0 0 1 1
0 0 0 1
0 0 0 0

'''