class Node:
    def __init__(self, key, value, index):
        self.key = key
        self.value = value
        self.index = index

class HashMap:
    def __init__(self, size):
        self.size = size
        self.loadFactor = 0
        self.elements = 0
        self.limit = 0.8
        self.bucket = [None for _ in range(self.size)]

    def hasher(self, key):
        h = 0
        base = 31

        for c in key:
            h = (h * base + ord(c)) % self.size
        return h

    def printBucket(self):
        for n in self.bucket:
            if n is not None:
                print(f"(value: {n.value}, index: {n.index})")
            else:
                print(n)

    def get(self, key):
        i = self.hasher(key)

        if self.bucket[i] is not None:
            return self.bucket[i].value
        else:
            return -1

    def post(self, key, value):
        i = self.hasher(key)

        if self.bucket[i] is not None:
            if self.bucket[i].value == value:
                self.bucket[i].value = value
                return
            
            print("collision")
            return

        data = Node(key, value, i)
        self.bucket[i] = data

hMap = HashMap(64)

hMap.post('abacate', 23)
hMap.post('morango', 2)

