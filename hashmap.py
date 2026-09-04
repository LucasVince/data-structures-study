class node:
    def __init__(self, value):
        self.value = value
        self.index

class hashmap:
    def __init__(self, size):
        self.size = size
        self.loadFactor = 0
        self.elements = 0
        self.limit = 0.8
        self.bucket = [None for _ in range(self.size)]

    def hasher(self, value):
        h = 0
        base = 31

        for c in value:
            h = (h * base + ord(c)) % self.size

        return h

    def getIndex(self, value):
        return 0

    def get(self, value):
        return 0

    def post(self, value):
        return 0

hMap = hashmap(64)

print(hMap.hasher('abacate'))
print(hMap.hasher('banana'))