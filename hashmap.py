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
        hashSum = 0

        for c in value:
            hashSum += ord(c) - ord("a")

        return hashSum % 16

    def get():
        return 0

    def post():
        return 0