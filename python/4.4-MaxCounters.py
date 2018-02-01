

def 1st_try_solution(N, A):
    """First try, failed on time, prob due to list construction, added maxed
	just to see if that would do it.
	
	Forgot 'and not maxed' at first, but it only solved the most extreme time
	test."""

    counters = [0] * N
	maxed = True

	for i in A:
	    if i == N + 1 and not maxed:
	        max_counter = max(counters)
	        counters = [max_counter for x in counters]
			maxed = True
		if i > 0 and i <= N:
			counters[i-1] += 1
			maxed = False

		return counters

# Doesn't quite work, exhausted
def solution(N, A):

	counters = [0] * N
	maxed = True
    for i in A:
		if i == N + 1 and not maxed:
			max_counter = max(counters)
			for index, val in enumerate(counters):
				counters[index] = max_counter
			maxed = True

			if i > 0 and i <= N:
	            counters[i-1] += 1
			    maxed = False

    return counters
