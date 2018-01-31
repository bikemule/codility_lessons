# says O(N) time, but depends on how you count sum
# It would be interesting to try in something like C

def solution(A):
    
    total = sum(A)
    difference = []
    
    for i in range(1, len(A)-1):
            difference.append(abs(sum(A[:i]) - sum(A[i:])))
            
    difference.append(abs(A[-1] - sum(A[:-1])))

    return min(difference)

