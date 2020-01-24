def solution(A, B):
    # No overlapping is possible.
    if len(A) < 2:      return len(A)
    count = 1  # The first segment starts a new cluster.
    end = B[0]
    index = 1  # The second segment.
    while index < len(A):
        # Skip all the segments in this cluster.
        while index < len(A) and A[index] <= end:   index += 1
        # All segments are processed.
        if index == len(A):                         break
        # Start a new cluster.
        count += 1
        end = B[index]
    return count


def solution(A, B):
    en = -1
    cl = 0
    siz = len(B)
    if siz == 0: return 0
    for seg in range(0, siz):
        print(seg, A[seg], en)
        if A[seg] > en:
            cl += 1
            en = B[seg]
    return cl
