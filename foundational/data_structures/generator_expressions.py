from sys import getsizeof
if __name__ == '__main__':
    print('creating list with list comprehension')
    value_list = [x for x in range(1000)]
    print(f'list is of size {getsizeof(value_list)}')

    print('creating generator')
    value_generator = (x for x in range(1000))
    print(f'generator is of size {getsizeof(value_generator)}')
