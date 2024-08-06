#  First Chapter -
def print_params(a=1, b='String', c=True):
    print(a, b, c)


# print_params(888)
# print_params(2, 4)
# print_params(555, c=False)
# print_params('TestString', 333, False)
print_params(b=25)
print_params(c=[1, 2, 3])

# Second chapter -
values_list = [888, 'Test', 4.4]
values_dict = {'a': 63, 'b': "I'mastring", 'c': False}
print_params(*values_list)
print_params(**values_dict)

# Third chapter -
values_list_2 = [54.32, 'STR']
print_params(*values_list_2, 42)
