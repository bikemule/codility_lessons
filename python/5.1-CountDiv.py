def sum_1_to_n(n):
    """Calculates sum of values 1 to n""" 
    return n*(n+1)//2


def solution(A, B, K):
    # write your code in Python 3.6
	    
    if A % K == 0:
        return (B - A) // K + 1
    else:
        return (B - A) // K
												    
    """
    #First try
														    
															    divisible = 0
																    
																	    if A % K == 0:
																		        divisible += 1
																				        
																		    diff = B - A
																							    
																					if diff == 1:
																				  					        return divisible
																											    
																				    return divisible + ((B-A) // K)
																				    """

