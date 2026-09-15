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

    def calcLoadFactor(self):
        lf = self.elements / self.size
        self.loadFactor = lf

        return self.loadFactor

    def doubleBucket(self):
        self.bucket += [None for _ in range(self.size)]
        self.size *= 2
        return

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

    def rehash(self):
        notNullNodes = []
        for n in self.bucket:
            if n is not None:
                notNullNodes.append(n)

        self.bucket = [None for _ in range(self.size)]

        for n in notNullNodes:
            self.post(n.key, n.value)
                
    def post(self, key, value):
        i = self.hasher(key)

        if self.bucket[i] is not None:
            if self.bucket[i].value == value:
                self.bucket[i].value = value
                return
            
            auxIndex = self.size + 1
            
            self.doubleBucket()

            data = Node(key, value, auxIndex)
            self.bucket[auxIndex] = data

            self.elements += 1

            self.rehash()
            return

        data = Node(key, value, i)
        self.bucket[i] = data

        self.elements += 1

        if self.calcLoadFactor() >= self.limit:
            self.doubleBucket()
        return

hMap = HashMap(10)
