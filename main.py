from AdjacentList import AdjacentList
from AdjacentMatrix import AdjacentMatrix
from Edge import Edge
from EdgeSheavesList import EdgeSheavesList
from OrderedEdgeList import OrderedEdgeList
from IncidenceMatrix import IncidenceMatrix
from UnorderedEdgeList import UnorderedEdgeList
from Transformer import transform


class Graph:
    def __init__(self):
        print('кол-во вершин')
        self._n = int(input())
        print('кол-во рёбер')
        self._m = int(input())
        print(
            'задать первичное представление графа\n 1. Матрица смежности\n 2. Матрица инцидентности\n '
            '3. Список смежности\n 4. Списки дуг\n 5. Отсортированные списки дуг\n 6. Списки пучков дуг'
        )
        self._viewMethod = int(input())

        assert 0 < self._viewMethod < 7

        self._graph = self.__construct_graph()

    def __construct_graph(self):
        match self._viewMethod:
            case 1:
                return self.adj_matrix()
            case 2:
                return self.incidence_matrix()
            case 3:
                return self.adj_list()
            case 4:
                return self.unordered_edge_list()
            case 5:
                return self.ordered_edge_list()
            case 6:
                return self.edge_sheaves_list()

    def print(self):
        self._graph.print()

    # def transform_to(self, ):
    #     ...

    def adj_matrix(self) -> AdjacentMatrix:
        am = AdjacentMatrix(self._n)

        for i in range(self._m):
            start, end = map(int, input().split(' '))
            am.add(Edge(start, end))

        return am

    def incidence_matrix(self) -> IncidenceMatrix:
        im = IncidenceMatrix(self._n, self._m)
        edge_index = 0

        for i in range(self._m):
            start, end = map(int, input().split(' '))
            im.add(edge_index, Edge(start, end))
            edge_index += 1

        return im

    def adj_list(self) -> AdjacentList:
        al = AdjacentList(self._n)

        for i in range(self._m):
            start, end = map(int, input().split(' '))
            al.add(Edge(start, end))

        return al

    def unordered_edge_list(self) -> UnorderedEdgeList:
        uel = UnorderedEdgeList(self._n)

        for i in range(self._n):
            start, end = map(int, input().split(' '))
            uel.add(Edge(start, end))

        return uel

    def ordered_edge_list(self) -> OrderedEdgeList:
        oel = OrderedEdgeList(self._n)

        for i in range(self._n):
            start, end = map(int, input().split(' '))
            oel.add(Edge(start, end))

        return oel

    def edge_sheaves_list(self) -> EdgeSheavesList:
        esl = EdgeSheavesList(self._n, self._m)

        for i in range(self._m):
            f, t = map(int, input().split(' '))
            esl.add(Edge(f, t))

        return esl


if __name__ == "__main__":
    graph = None
    while True:
        commands = ("Введите команду:\n"
                    "1. Создать граф\n"
                    "2. Вывести граф\n"
                    "3. Конвертировать граф\n"
                    )

        match int(input()):
            case 1:
                try:
                    graph = Graph()
                except AssertionError:
                    print("проверьте корректность ввода и попробуйте еще раз")
            case 2:
                if graph is None:
                    print("нет графа")
                    continue
                graph.print()
            case 3:
                if graph is None:
                    print("нет графа")
                    continue
                ...
                graph.transform_to()

        graph = Graph()
        graph.print()
