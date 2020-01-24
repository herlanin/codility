def solution(A):
    from math import sqrt
    A_max = max(A)
    A_len = len(A)
    # Compute the frequency of occurrence of each
    # element in array A
    count = {}
    for element in A:
        count[element] = count.get(element,0)+1
    # Compute the divisors for each element in A
    divisors = {}
    for element in A:
        # Every nature number has a divisor 1.
        divisors[element] = [1]
    # In this for loop, we only find out all the
    # divisors less than sqrt(A_max), with brute
    # force method.
    for divisor in xrange(2, int(sqrt(A_max))+1):
        multiple = divisor
        while multiple  <= A_max:
            if multiple in divisors and not divisor in divisors[multiple]:
                divisors[multiple].append(divisor)
            multiple += divisor
    # In this loop, we compute all the divisors
    # greater than sqrt(A_max), filter out some
    # duplicate ones, and combine them.
    for element in divisors:
        temp = [element/div for div in divisors[element]]
        # Filter out the duplicate divisors
        temp = [item for item in temp if item not in divisors[element]]
        divisors[element].extend(temp)
    # The result of each number should be, the array length minus
    # the total number of occurances of its divisors.
    result = []
    for element in A:
        result.append(A_len-sum([count.get(div,0) for div in divisors[element]]))
    return result

