# python 2.7 needed by condition of the problem
import re


def solution(n):
    if len(n) < 200 and re.findall(r"[\W|\d|_|A-Z]", n) == []:

        variation_set = (n[0:i] for i in range(1, len(n) + 1))

        # entrance for each divisor
        max_entrance = len(max((n.split(i)[:-1] for i in variation_set if n.split(i))))

        return max_entrance if max_entrance != 1 else 0
    else:
        return "Commander Lambda doesn't like this! Check your cake"


# change print to print() for using in python 3
print solution('abcabcabcabc')


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
