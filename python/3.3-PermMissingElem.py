def solution(A):
    # write your code in Python 3.6
    
    biggest = len(A) + 1
    total_should_be = biggest * (biggest + 1) //2
    total = sum(A)
    
    return total_should_be - total

