from Edge import Edge


class ArcSheavesList:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.I = []
        self.J = []
        self.h = [-1 for _ in range(n)]
        self.l = [-1 for _ in range(self.m)]

    def add(self, edge: Edge):
        self.I.append(edge.start)
        self.J.append(edge.end)

        #когда закончили добавлять ребра, что обновить значения в h и l
        if len(self.I) == self.m:
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

        print("h:")

        for i in self.h:
            print(i)

        print("l:")

        for i in self.l:
            print(i)
