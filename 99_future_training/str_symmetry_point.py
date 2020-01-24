def solution(S):
    sLen = len(S)
    # Symmetry point is possible, when and only when the
    # string's length is odd.
    if sLen % 2 == 0:   return -1
    # With a odd-length string, the only possible symmetry
    # point is the middle point.
    mid = sLen // 2
    begin, end = 0, sLen-1
    # The middle point of an odd-length string is symmetry
    # point, only when the string is symmetry.
    while begin < mid:
        if S[begin] != S[end]:      return -1
        begin += 1
        end -= 1
    return mid
