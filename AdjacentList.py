from Edge import Edge


class AdjacentList:
    #  Список смежности представляет собой набор неупорядоченных списков,
    #  используемых для представления конечного графа.
    #  Каждый неупорядоченный список в списке смежности описывает набор соседей определенной вершины графа.
    #  Является одним из самых распространённых представлений графов (наряду с матрицей смежности)
    
    #  Реализация: для каждой вершины составляется список вершин, с которыми первоначальная вершина имеет ребро.
    #  Пример
    #  сам граф: https://present5.com/presentation/3/816642_58668781.pdf-img/816642_58668781.pdf-4.jpg
    # Вершина i (начиная с нуля)      список вершин, в которые исходит связь из i-ной вершины
    # 0                                  [1]
    # 1                                  [2, 3, 4]
    # 2                                  [3]
    # 3                                  [4]
    # 4                                  []



    
    # конструктор для создания экземпляра списка смежности AdjacentList, принимает количество вершин.
    def __init__(self, n):
        self.list = [set() for _ in range(n)]
        self.n = n
        self.m = 0

    # для преобразования в список смежности, возвращает свой же экземпляр класса
    def to_adjacent_list(self):
        return self

    # для преобразования из списка смежности, возвращает свой же экземпляр класса
    @staticmethod
    def from_adjacent_list(self):
        return self

    # функция по добавлению ребра
    def add(self, edge: Edge):
        self.list[edge.start].add(edge.end)
        self.m += 1

    #  функция для вывода списка смежности
    def print(self):
        for i in self.list:
            print(' '.join(str(i)))


    # def to_adjacent_matrix(self):
    #     am = AdjacentMatrix.AdjacentMatrix(self.n)
    #     for i, row in enumerate(self.list):
    #         for j, has_edge in enumerate(row):
    #             if has_edge:
    #                 am.add(Edge(i, j))
    #     return am

    # def to_unordered_arc_list(self):
    #     unordered_arc_list = UnorderedArcList(self.n)
    #     for i, row in enumerate(self.list):
    #         for j, has_edge in enumerate(row):
    #             if has_edge:
    #                 unordered_arc_list.add(Edge(i, j))
    #     return unordered_arc_list
    #
    # def to_ordered_arc_list(self):
    #     ordered_arc_list = SortedArcList(self.n)
    #     for i, row in enumerate(self.list):
    #         for j, has_edge in enumerate(row):
    #             if has_edge:
    #                 ordered_arc_list.add(Arc(i, j))
    #     return ordered_arc_list
    #
    # # def to_incidence_matrix(self):
    # #     edges_count = 0
    # #     for i in range(len(self.list)):
    # #         edges_count += sum(self.list[i])
    # #     incidence_matrix = IncidenceMatrix.IncidenceMatrix(self.n, edges_count)
    # #     edge_num = 0
    # #     for i in range(len(self.list)):
    # #         for j in range(len(self.list[i])):
    # #             incidence_matrix.add(edge_num, i, j)
    # #             edge_num += 1
    # #     return incidence_matrix
    #
    # def to_incidence_matrix(self):
    #     edge_count = 0
    #     for _, v_verticles in enumerate(self.list):
    #         edge_count += len(v_verticles)
    #     incidence_matrix = IncidenceMatrix(self.n, edge_count)
    #     edge_index = 0
    #     for v_from, _ in enumerate(self.list):
    #         for _, v_to in enumerate(v_from):
    #             incidence_matrix.add(edge_index, Edge(v_from, v_to))
    #             edge_index += 1
    #     return incidence_matrix
