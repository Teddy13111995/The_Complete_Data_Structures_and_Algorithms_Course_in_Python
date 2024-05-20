class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def addVertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
            return True
        return False

    def printGraph(self):
        for vertex in self.gdict:
            print(vertex, ":", self.gdict[vertex])

    def addEdgeInBothVertex(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        return False

    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            try:
                self.gdict[vertex1].remove(vertex2)
                self.gdict[vertex2].remove(vertex1)
                return True
            except ValueError:
                pass
        return False

    def removeVertex(self, vertex):
        if vertex in self.gdict.keys():
            for otherVertex in self.gdict[vertex]:
                self.gdict[otherVertex].remove(vertex)
            del self.gdict[vertex]
            return True
        return False

    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = [vertex]
        while queue:
            currentVertex = queue.pop(0)
            print(currentVertex)
            for adjacentVertex in self.gdict[currentVertex]:
                if adjacentVertex not in visited:
                    visited.add(adjacentVertex)
                    queue.append(adjacentVertex)

    def dfs(self, vertex):
        visited = set()
        stack = [vertex]
        while stack:
            currentVertex = stack.pop()
            if currentVertex not in visited:
                print(currentVertex)
                visited.add(currentVertex)
            for adjacentVertex in self.gdict[currentVertex]:
                if adjacentVertex not in visited:
                    stack.append(adjacentVertex)
