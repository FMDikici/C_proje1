def my_generator(limit):
    current = 0
    while current < limit:
        yield current
        current += 1

# Generator nesnesini oluştur
gen = my_generator(5)

# Generator üzerinde döngü yap
for num in gen:
    print(num)
