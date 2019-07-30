# working with generator functions
def first_n_numbers(n):
    number = 0
    while number <= n:
        yield number
        number += 1


for i in first_n_numbers(5000):
    print(i)
