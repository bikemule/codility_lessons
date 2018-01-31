# says O(N) time, but depends on how you count sum
# It would be interesting to try in something like C
# Edit: definitely polynomial time


def correct_slow_solution(A):
    
    total = sum(A)
    difference = []
    
    for i in range(1, len(A)-1):
            difference.append(abs(sum(A[:i]) - sum(A[i:])))
            
    difference.append(abs(A[-1] - sum(A[:-1])))

    return min(difference)

def solution(A):
    # looks like I forgot about the last element or something because it's not 100% correct

    total = sum(A)
    remaining_total = total
    running_total = 0
    min_diff = 1000
    
    for i in range(0, len(A)):
        remaining_total -= A[i]
        running_total += A[i]
        diff = abs(running_total - remaining_total)
        if diff < min_diff:
            min_diff = diff
        
    return min_diff

