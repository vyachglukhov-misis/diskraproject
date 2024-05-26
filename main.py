class Graf:
    def __init__(self):
        print('кол-во вершин')
        self._n = int(input())
        print('кол-во рёбер')
        self._m = int(input())
        print(
            'задать первичное представление графа\n 1. Матрица смежности\n 2. Матрица инцидентности\n 3. Список смежности\n 4. Отсортированные списки дуг\n 5. Списки пучков дуг')
        self._viewMethod = int(input())

    def MatrixSmezh(self):
        verticles = self._n
        m = []
        for i in range(verticles):
            m.append(list(map(int, input().split())))
        print(m)

    def MatrixIncident(self):
        num_v = self._n
        num_e = self._m
        edges = []
        for i in range(num_e):
            edges.append(list(map(int, input().split(' '))))
        result_matrix = [[0 for j in range(num_v)] for i in range(num_e)]
        for i, edge in enumerate(edges):
            result_matrix[edge[0]][i] = 1
            result_matrix[edge[1]][i] = 1
        print(result_matrix)

    def ListSmezhnost(self):
        num_e = self._m
        edges = []
        smezhnosti_matrix = [[] for i in range(num_e)]
        for i in range(num_e):
            edges.append(list(map(int, input().split(' '))))
        for i in range(len(edges)):
            smezhnosti_matrix[edges[0]].append(edges[1])
        print(smezhnosti_matrix)

    def NonSortedArcsList(self):
        num_arcs = self._m
        arcs = []
        for i in range(num_arcs):
            arcs.append(list(map(int, input().split(' '))))
        for i in range(num_arcs):
            print(arcs[i])

    def SortedArcsList(self):
        num_arcs = self._m
        arcs = []


graph = Graf()
graph.MatrixSmezh()
