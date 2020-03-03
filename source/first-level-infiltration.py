# python 2.7 needed by condition of the problem
import re
from functools import reduce


def solution(n):
    if len(n) < 200 and re.findall(r"[\W|\d|_|A-Z]", n) == []:

        # find variation set
        def find_variation_set(list_char):
            variation = []  # unfortunately mutable
            [[variation.append(list_char[0:i])] for i in range(1, len(list_char) + 1)]  # 2.7 scan imitation
            return list(map(lambda elem: reduce(lambda a, b: a + b, elem), variation))

        # check entrance for each divisor (find divisors encapsulated in filter)
        def max_entrance():
            return len(max(map(lambda x: x[:-1],
                               filter(lambda elem: all(item == '' for item in elem),
                                      [n.split(i) for i in find_variation_set(n)]))))

        return max_entrance() if max_entrance() != 1 else 0
    else:
        return "Commander Lambda doesn't like this! Check your cake"


# change print to print() for using in python 3
print (solution('abcabcabcabc'))


# experimental functions:

# def scan(func, sequence, acc):
#     return [acc := func(acc, x) for x in sequence]

# def divisors(x):
#     return filter(lambda y: (x % y) == 0, range(1, x))

# print(scan(lambda acc, x: acc + x, range(1, 20), 0))

# transpose
# matrix = [
#         [1, 2, 3, 4, 1],
#         [5, 6, 7, 8, 1],
#         [9, 10, 11, 12, 1],
#     ]
# print [[row[i] for row in matrix] for i in range(len(max(matrix)))]
