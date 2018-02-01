"""
Naive attempt at solution using theoretical sum (N*N+1//2) vs actual sum
got all results except the ones designed to have the correct sum, but
are not permutations. Also, one of the extreme_values cases (all the same
values, N = ~100,000). That was a performance test, but can't see why
performance would be an issue.
"""
def solution(A):
    """Return 1 if A is a permutation, 0 otherwise.
    A permutation is a sequence containing each element from 1 to N once,
    and only once."""
    
    # Keep track of all digits in range
    counters = [1] * len(A)

    # Decrement counter when you see an element
    for n in A:
	# If element is is out of list range, it's not a permutation.
        try:
	    # counter should be 1, otherwise not a permutation.
            if counters[n-1] == 1:
                counters[n-1] -= 1
            else:
                return 0
        except IndexError:
            return 0
    
    return 1

