class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

# Iterator nesnesini oluştur
my_iter = MyIterator(5)

# Iterator üzerinde döngü yap
for num in my_iter:
    print(num)