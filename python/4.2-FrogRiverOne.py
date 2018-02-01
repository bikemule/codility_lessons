def solution(X, A):
    """Return the first index where all positive integers <= X exist
    in the array to the left. Return -1 otherwise"""

    # Track which numbers have been seen
    counter = [0] * X
    
    # Calculate theoretical total
    total_should_be = X * (X + 1) // 2
    
    for index, val in enumerate(A):
        # Verify val in range and not already seen
        if val <= X and counter[val-1] == 0:
            counter[val-1] = val
            total_should_be -= val
            
            # Tracking total is the easiest way to know we're done.
            if total_should_be == 0:
                return index
    
    return -1

