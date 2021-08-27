def num_gen():
    for odd_nums in range(1, n + 1):
        if odd_nums % 2 != 0:
            yield odd_nums


n = 15
odd_to_15 = []
# for odd_nums in range(1, n + 1):
#     if odd_nums % 2 == 0:
#         odd_to_15.append(odd_nums)
odd_to_15 = num_gen()
print(odd_to_15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))