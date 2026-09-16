class AdjacentMatrix:
    def __init__(self, size):
        self.size = size
        self.occupation = 0
        self.elements = [0 for _ in range(size)]
        self.matrix = []

    def addNode(self, data):
        if self.occupation + 1 > self.size:
             print("Graphs are now full!!!")
             return

        self.elements[self.occupation] = data

        if len(self.matrix) < 1:
            self.matrix = [[0]]
        else:
            for line in self.matrix:
                line += [0]

            self.matrix += [[0 for _ in range(len(self.matrix) + 1)]]

        self.occupation += 1
        return

    def addSingleEdge(self, src, end):
        self.matrix[src][end] = 1
        return

    def addDoubleEdge(self, src, end):
        self.matrix[src][end] = 1
        self.matrix[end][src] = 1
        return

    def checkAdjacency(self, src, end):
        return self.matrix[src][end]

    def printMatrix(self):

        for i in range(len(self.matrix)):
                print(f'{self.elements[i]} {self.matrix[i]}')

graph = AdjacentMatrix(5)

graph.addNode('A')
graph.addNode('B')
graph.addNode('C')
graph.addNode('D')
graph.addNode('E')

graph.printMatrix()