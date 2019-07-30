# working with lambda functions and map/filter

my_list = [10, 11, 2, 78, 125, 12678, 693, 95]
print(list(map(lambda x: x * 2, my_list)))
print(list(map(lambda x: 'big' if x > 100 else 'small', my_list)))
print("map doesn't change original list: ", my_list, "\n")

print(list(filter(lambda x: x % 2 == 0, my_list)))
print("filter doesn't change original list: ", my_list, "\n")
