def solution(A):
    days = len(A)
    # If the number of days is zero or one, there
    # is no time to get profit.
    if days < 2:
        return 0
    max_price_from_here = A[days-1]
    max_profit = 0
    for index in xrange(days-2, -1, -1):
        # max_price_from_here-A[index] means the maximum
        # profit from current day to end.
        max_profit = max(max_profit, max_price_from_here-A[index])
        max_price_from_here = max(A[index], max_price_from_here)
    return max_profit


def solution(A):
    max_ending = max_slice = 0
    for i in xrange(1, len(A)):
        max_ending = max(0, max_ending + A[i] - A[i - 1])
        max_slice = max(max_slice, max_ending)
    return max_slice