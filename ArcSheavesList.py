from Edge import Edge


class ArcSheavesList:
    def __init__(self, n, edges: list[Edge]):
        self.n = n
        self.m = len(edges)
        self.I = []
        self.J = []
        self.h = [-1 for _ in range(n)]
        self.l = [-1 for _ in range(self.m)]

        for edge in edges:
            self.I.append(edge.start)
            self.J.append(edge.end)

        for i in range(self.m):
            v = self.I[i]
            self.l[i] = self.h[v]
            self.h[v] = i

    def print(self):
        for i in range(self.n):
            # просмотр пучка дуг, выходящих из вершины i
            k = self.h[i]
            while k != -1:
                print(self.I[i], self.J[k])
                k = self.l[k]

        print("\nh:\n")

        for i in self.h:
            print(i)

        print("\nl:\n")

        for i in self.l:
            print(i)
