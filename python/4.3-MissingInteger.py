def solution(A):
    # write your code in Python 3.6
    occurred = [False] * 1000000
            
    for n in A:
        if n > 0 and not occurred[n-1]:
            occurred[n-1] = n
    for i, n in enumerate(occurred):
        if n == 0:
            return i + 1

