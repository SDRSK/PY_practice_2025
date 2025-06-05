import math
import random

tupl = (1, 'dsfas', True)
some_list = [1, 'dsfas', True]

print(f'Tuple size is: {tupl.__sizeof__()}')
print(f'List size is: {some_list.__sizeof__()}')

empty_tuple = ()
another_empty_tuple = tuple()
another_tuple = 1, True, 18.5

a = (3,)

tuple_from_list = tuple(some_list)
tuple_from_string = tuple('abcdefgh')
print(tuple_from_string[::2])

if 'C' in tuple_from_string:
    print('Exists')

# tuple_from_list[0] = 'afs'

# del tuple_from_list
# print(tuple_from_list)

some_list = list(tuple_from_list)

dictionary = {'key_1': 'value_1', 'key_2': 'value_2'}
empty_dict_1 = {}
empty_dict_2 = dict()

print(dictionary['key_2'])

if 'key_3' in dictionary:
    print('Key exists')

if 'value_1' in dictionary.values():
    print('Value exists')

dictionary['key_1'] = 'New value'
dictionary['key_2'] = False
dictionary['key_3'] = 'Rand'

del dictionary['key_2']


empty_dict_1.update(dictionary)

for element in empty_dict_1:
    print(element, empty_dict_1[element])

a = dictionary.copy()
print(dictionary.get('key_2', 'Default'))
dictionary.setdefault('key_4', 'Default')

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

result = dictionary.pop('key_1', 'default')
dictionary.clear()

some_literal = 'Text'
some_literal2 = "text \`sd"

long_text = """ sdafsadf asdf sa fasdf asdf' 
'a sdf asdf' 
'' 
' asdf"""

print(long_text)

empty_str = str()

# enter_text = input('Enter some text: ')

long_str = 'abc' + str(123)

test_str = 'abcd12345efgh67895e5'

print(test_str.startswith('b'))
print(test_str.endswith('b'))
print(test_str.count('5'))
print(test_str.isalpha())
print(test_str.isdecimal())
print(test_str.islower())

test_str_2 = 'hello world'

print(test_str_2.istitle())

print(test_str.upper())
print(test_str_2.swapcase())
print(test_str_2.capitalize())

print(test_str_2.replace('hel', '000'))

print(test_str.split(sep='1'))

some_set = {1, True, 'dsfaf'}
empty_set_1 = set()

str_to_set = '123124545'
numeric_set = set(str_to_set)

if 2 in numeric_set:
    print('exists')

for element in numeric_set:
    print(element)