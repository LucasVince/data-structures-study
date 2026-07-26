class hashMap:
    def __init__(self, size):
        self.size = size
        self.loadFactor = 0
        self.elements = 0
        self.limit = 0.8
        self.bucket = [None for _ in range(self.size)]
        self.alphabet = ['a', 'A', 'b', 'B','c', 'C','d', 'D','e', 'E','f', 'F','g', 'G','h', 'H','i', 'I','j', 'J','k', 'K','l', 'L','m', 'M','n', 'N','o', 'O','p', 'P','q', 'Q','r', 'R','s', 'S','t', 'T','u', 'U','v', 'V','w', 'W','x', 'X','y', 'Y','z', 'Z']

    def hash(self, key):
        hashed_string = ''

        for c in key:
            hashed_string += str(self.alphabet.index(c))

        return int(hashed_string)

    def get_bucket_index(self, hashed_string):
        return hashed_string % self.size

    def calc_load_factor(self):
        return self.elements / self.size

    def post(self, key, value):
        hashed_string = self.hash(key)
        bucket_index = self.get_bucket_index(hashed_string)

        if self.bucket[bucket_index] != None:
            self.bucket[bucket_index] = value
        
        self.elements += 1

        if self.calc_load_factor() > self.limit:
            self.bucket += [None for _ in range(32)]

        return (f'key: {key}, value: {value}, index: {bucket_index}')

    def get(self, key):
        hashed_string = self.hash(key)
        bucket_index = self.get_bucket_index(hashed_string)

        return self.bucket[bucket_index]

    def show_bucket(self):
        print(self.bucket)

Hmap = hashMap(10)
