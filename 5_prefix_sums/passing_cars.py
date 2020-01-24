def solution(A):
    west = 0    # The number of west-driving cars so far
    passing = 0 # The number of passing
    for index in xrange(len(A)-1,-1,-1):
        # Travel the list from the end to the beginning
        if A[index] == 0:    # A east-driving car
            passing += west
            if passing > 1000000000:
                return -1
        else:                # A west-driving car
            west += 1
    return passing

def solution(A):
    #initialize pairs to zero
     pairs = 0
     #count the numbers of zero discovered while traversing 'A'
     #for each successive '1' in the list, number of pairs will
     #be incremented by the number of zeros discovered before that '1'
     zero_count = 0
     #traverse through the list 'A'
     for i in range(0, len(A)):
         if A[i] == 0:
             #counting the number of zeros discovered
             zero_count += 1
         elif A[i] == 1:
             #if '1' is discovered, then number of pairs is incremented
             #by the number of '0's discovered before that '1'
             pairs += zero_count
             #if pairs is greater than 1 billion, return -1
             if pairs > 1000000000:
                 return -1
    #return number of pairs
     return pairs