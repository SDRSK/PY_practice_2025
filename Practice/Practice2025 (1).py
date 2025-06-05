import math

list = [1, 2 ,3]

result = len(list)
print(len(list))

def function_name(first_name, last_name): 
    print(first_name + last_name)
    return first_name + last_name

print(function_name(12, 123))

function_name('1', 'asf') 

def no_return_function():
    print('')
    return None

def some_values_return():
    return ('dsf', 451)

func_result = some_values_return()[1]

def sum(a, b=2, c=4, d=1):
    return a + b + c


print(sum(1))
print(sum(1, 4))
print(sum(1, 4, 5))

a = 4
b = 5
c = 7

print(min(a, b))
print(min(a, b, c))

def sum_func(a, b, *c):
    sum = a + b
    for number in c:
        sum += number
    return sum

print(sum_func(1, 2))
print(sum_func(1, 2, 3))
print(sum_func(1, 2, 3, 4))
print(sum_func(1, 2, 3, 4, 5, 6))

print('-----')

z = 5
x = 44

def test_z(a):
    global z
    global x
    z = a
    x = 12
    print(z)

def another_func():
    print('another')

def new_func():
    another_func()
    some_values_return()

def get_folder_size(path):
    size = 0
    # iterate through dicrectory
    size += get_folder_size(path+'directory_path')

test_z(2)
print(z)


