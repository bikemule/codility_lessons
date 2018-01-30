# Doesn't solve problem with O(1) storage??

def solution(A):
    foo = {}

    # Get a count of all items in the array
    for x in A:
        if x in foo:
            foo[x] += 1
        else:
            foo[x] = 1

    # only one is odd, according to the problem statement
    for k in foo:
        if foo[k] % 2 != 0:
            return k

if __name__ == '__main__':
    solution([9,3,9,3,9,7])
