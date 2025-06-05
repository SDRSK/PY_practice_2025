import math
import random


a = 0
b = 0

range_var = range(4)
range_var2 = range(1, 20, 2)

string = '12345'
# print(sum(range_var))

some_list = [0, 1, '2', 3, '4', '5', 6, 7, 8, 99]
empty_list = list(range_var)

copy_list = some_list[:]
del copy_list[0]

print(some_list)
print(copy_list)

copy_list.insert(3, True)
copy_list.remove('5')
copy_list.clear()
del copy_list[:]

copy_list.reverse()

# for value in range_var2:
#     print(value)

# while a < 10:
#     while b < 10:
#         print(b)
#         b += 1
#     a += 1
#     print(a)
# else:
#     print('a is > 10')

# c = a + b

# if (a + b < 10) or (a - b > 3):
#     print('Not equal')
# elif not (c > 10):
#     print('Greater or equal')
# elif a < b - 10:
#     print("some sdfsf")
# else:
#     print('Is equal')



# try:
#     x = int(input())
#     k = 10 / x
#     if x > 10:
#         raise(ValueError)
# except ValueError:
#     print("Integer value was expected")
# except ZeroDivisionError:
#     print('Zero division is forbidden')
# except Exception as mes:
#     print(f'Unknow error: {mes}')
# else:
#     print(k)
# finally:
#     print('Try except block is completed')