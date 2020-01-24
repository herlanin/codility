def solution(A):
    # Since S could be 1 or -1, it does not matter that
    # each element in A is positive or negative.
    A = [abs(item) for item in A]
    sumOfA = sum(A)
    # Get the number distribution. So we do not need to try
    # each number for multiple times.
    numbers = {}
    for item in A:  numbers[item] = numbers.get(item, 0) + 1
    # This is the KEY point.
    # Typically, we will use possible = [False] * len to track, which numbers
    # could be the result by summing up subsets of A.
    # For a number, appeared for many times, there will be multiple attempts
    # for it. But in this way, when we are trying number n,
    # possible[i] == -1 means it is impossible.
    # possible[i] == i >= 0 means it is possible and there are i n(s) left to use.
    # So for ALL number n(s), we only need ONE scan over the record.
    possible = [-1] * (sumOfA // 2 + 1)
    possible[0] = 0
    for number in numbers:      # Try each distinct number
        for trying in xrange(sumOfA//2+1):
            if possible[trying] >= 0:
                # Can be reached with previous numbers
                possible[trying] = numbers[number]
            elif trying >= number and possible[trying-number] > 0:
                # Cannot be reached with only previous numbers.
                # But could be achieved with previous numbers AND current one.
                possible[trying] = possible[trying-number] - 1
    # Divide the A into two parts: P and Q, with restriction P <= Q.
    # So P <= sumOfA // 2 <= Q. We want the largest possible P, so that
    # Q-P is minimized.
    for halfSum in xrange(sumOfA//2, -1, -1):
        if possible[halfSum] >= 0:
            return sumOfA - halfSum - halfSum
    raise Exception("Should never be here!")
    return 0