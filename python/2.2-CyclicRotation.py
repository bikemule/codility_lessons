def solution(A, K):
    # write your code in Python 3.6
    
    if len(A) == 0 or len(A) == K:
        return A
        
    K = K % len(A)
    
    return A[-K:] + A[:len(A)-K]

