def solution(A):
    discs_count = len(A)            # The total number of discs
    range_upper = [0]*discs_count   # The upper limit position of discs
    range_lower = [0]*discs_count   # The lower limit position of discs
    # Fill the limit_upper and limit_lower
    for index in xrange(0, discs_count):
        range_upper[index] = index + A[index]
        range_lower[index] = index - A[index]
    range_upper.sort()
    range_lower.sort()
    range_lower_index = 0
    intersect_count = 0
    for range_upper_index in xrange(0, discs_count):
        # Compute for each disc
        while range_lower_index < discs_count and
            range_upper[range_upper_index] >= range_lower[range_lower_index]:
            # Find all the discs that:
            #    disc_center - disc_radius <= current_center + current_radius
            range_lower_index += 1
        # We must exclude some discs such that:
        #    disc_center - disc_radius <= current_center + current_radius
        #    AND
        #    disc_center + disc_radius <(=) current_center + current_radius
        # These discs are not intersected with current disc, and below the
        #    current one completely.
        # After removing, the left discs are intersected with current disc,
        #    and above the current one.
        # Attention: the current disc is intersecting itself in this result
        #    set. But it should not be. So we need to minus one to fix it.
        intersect_count += range_lower_index - range_upper_index -1
        if intersect_count > 10000000:
            return -1
    return intersect_count


def solution(A):
    counter = 0
    N = len(A)
    stop_intersecting = [0] * N
    for i in range(0, N):
        r = A[i]
        intersect_with = i if i - r < 0 else  i - stop_intersecting[i - r]
        counter += intersect_with
        if(counter > 10000000): return -1
        stop_intersecting_at = i + r + 1
        if stop_intersecting_at < N: stop_intersecting[stop_intersecting_at]+=1
        iNext = i + 1
        if iNext < N : stop_intersecting[iNext] += stop_intersecting[i]
    return counter