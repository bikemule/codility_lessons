def solution(A):
    # write your code in Python 3.6
    
    total = sum(A)
    difference = []
    
    for i in range(len(A)-1):
        if i == 0:
            difference.append(abs(A[0] - sum(A[1:])))
        else:
            difference.append(abs(sum(A[:i]) - sum(A[i:])))
            
    difference.append(abs(A[-1] - sum(A[:-1])))

    return min(difference)

