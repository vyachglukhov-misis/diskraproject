from Edge import Edge


class ArcSheavesList:
    def __init__(self, n, edges: list[Edge]):
        self.n = n
        self.m = len(edges)
        self.I = [-1 for _ in range(self.m)]
        self.J = [-1 for _ in range(self.m)]
        self.h = [-1 for _ in range(n)]
        self.l = [-1 for _ in range(self.m)]

        for f, t in edges:
            self.I.append(f)
            self.J.append(t)

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
