def solution(A):
    from math import sqrt
    A_len = len(A)
    next_peak = [-1] * A_len
    peaks_count = 0
    first_peak = -1
    # Generate the information, where the next peak is.
    for index in xrange(A_len-2, 0, -1):
        if A[index] > A[index+1] and A[index] > A[index-1]:
            next_peak[index] = index
            peaks_count += 1
            first_peak = index
        else:
            next_peak[index] = next_peak[index+1]
    if peaks_count < 2:
        # There is no peak or only one.
        return peaks_count
    max_flags = 1
    max_min_distance = int(sqrt(A_len))
    for min_distance in xrange(max_min_distance + 1, 1, -1):
        # Try for every possible distance.
        flags_used = 1
        flags_have = min_distance-1 # Use one flag at the first peak
        pos = first_peak
        while flags_have > 0:
            if pos + min_distance >= A_len-1:
                # Reach or beyond the end of the array
                break
            pos = next_peak[pos+min_distance]
            if pos == -1:
                # No peak available afterward
                break
            flags_used += 1
            flags_have -= 1
        max_flags = max(max_flags, flags_used)
    return max_flags


