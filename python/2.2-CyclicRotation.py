def solution(A, K):
    """Return the list A rotated to the right K times.
    A is a list of integers in the range [-1000,1000]
    K is an integer between 0 and 100"""
    if len(A) == 0 or len(A) == 1 or len(A) == K:
        return A

    K = K % len(A)

    if K == 1:
        return A[-1:] + A[:-1]

    return A[-K:] + A[:-K]
