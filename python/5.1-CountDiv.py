import math


def tests():

    test_cases = (((0, 1, 2), 1),
                  ((0, 1, 1), 2),
                  ((1, 2, 1), 2),
                  ((1, 2, 2), 1),
                  ((2, 3, 2), 1),
                  ((2, 4, 2), 2),
                  ((0, 10000, 1), 10001),
                  ((0, 9999, 1), 10000),
                  ((11, 14, 2), 3),
                  ((6, 12, 2), 4),
                  ((11, 345, 17), 20),
                  ((2, 7, 2), 3),
                  ((6, 11, 2), 3),
                  ((0, 1, 11), 1),
                  ((1, 1, 11), 0),
                  ((10, 10, 5), 1),
                  ((10, 10, 7), 0),
                  ((10, 10, 20), 0),
                  ((101, 1234560000, 10000), 123456))

    for case in test_cases:
        answer = solution(*case[0])
        if answer != case[1]:
            print("ERROR:", case, answer)


def solution(A, B, K):
    """Returns count of numbers divisible by K between A and B inclusive"""

    """
    if A != 0 and B % K == 0 and B - A > 0:
        return math.ceil((B - A) // K) + 1
    else:
        return math.ceil((B - A) // K)
    """

    div = 0
    if A == 0:
        div += 1

    if K == 1:
        return div + B - A

    if B - A == 0:
        return math.ceil((B - A) / K) + div

    return ((B - A) // K) + div

    """
    # nth try
    if A % K == 0 or B % K == 0:
        return math.ceil((B - A) / K) + 1
    else:
        return math.ceil((B - A) / K)



    #First try

    divisible = 0

    if A % K == 0:
        divisible += 1

    diff = B - A

    if diff == 1:
        return divisible

    return divisible + ((B-A) // K)
    """


if __name__ == '__main__':
    tests()
