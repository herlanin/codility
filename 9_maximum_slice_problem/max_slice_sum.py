def solution(A):
    max_slice_ending_here = A[0]
    max_slice = A[0]
    for element in A[1:]:
        max_slice_ending_here = max(element, max_slice_ending_here+element)
        max_slice = max(max_slice, max_slice_ending_here)
    return max_slice

def solution(A):
    max_ending = max_slice = 0
    max_A = max(A)
    if max_A > 0:
        for i in xrange(len(A)):
            max_ending = max(0, max_ending + A[i])
            max_slice = max(max_slice, max_ending)
    else:
        max_slice = max_A
    return max_slice