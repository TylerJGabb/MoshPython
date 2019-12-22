import sys
from timeit import timeit

with_raise = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can not be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as verr:
    pass
"""

without_raise = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age
xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""


def print_percentage(completion):
    sys.stdout.write('\r|' + ('#' * completion) + ('_' * (100 - completion)) + '| ' + str(completion) + "%")
    sys.stdout.flush()


avg = 0
completion = -1
iters = 10000
print('calculating performance improvement of not raising exception...')
for i in range(iters):
    percent = int(100 * (i + 1) / iters)
    if percent > completion:
        completion = percent
        print_percentage(completion)
    with_raise_performance = timeit(with_raise, number=10000)
    without_raise_performance = timeit(without_raise, number=10000)
    ratio = with_raise_performance / without_raise_performance
    avg = (avg * i + ratio) / (i + 1)

print()
print(avg)
