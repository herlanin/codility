"""This is a demo task.

An array A consisting of N integers is given. An equilibrium index of this array is any integer P such that 0 ≤ P < N and the sum of elements of lower indices is equal to the sum of elements of higher indices, i.e.
A[0] + A[1] + ... + A[P−1] = A[P+1] + ... + A[N−2] + A[N−1].
Sum of zero elements is assumed to be equal to 0. This can happen if P = 0 or if P = N−1.

For example, consider the following array A consisting of N = 8 elements:

  A[0] = -1
  A[1] =  3
  A[2] = -4
  A[3] =  5
  A[4] =  1
  A[5] = -6
  A[6] =  2
  A[7] =  1
P = 1 is an equilibrium index of this array, because:

A[0] = −1 = A[2] + A[3] + A[4] + A[5] + A[6] + A[7]
P = 3 is an equilibrium index of this array, because:

A[0] + A[1] + A[2] = −2 = A[4] + A[5] + A[6] + A[7]
P = 7 is also an equilibrium index, because:

A[0] + A[1] + A[2] + A[3] + A[4] + A[5] + A[6] = 0
and there are no elements with indices greater than 7.

P = 8 is not an equilibrium index, because it does not fulfill the condition 0 ≤ P < N.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers, returns any of its equilibrium indices. The function should return −1 if no equilibrium index exists.

For example, given array A shown above, the function may return 1, 3 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647]."""


def solution(A):
    heading = 0       # The sum of A[0] + A[1] + ... + A[P-1]
    tailing = sum(A)  # The sum of A[P] + A[P+1] + ... + A[N-2] + A[N-1]
    for index in range(len(A)):
        tailing -= A[index] # The sum of A[P+1] + ... + A[N-2] + A[N-1]
        if heading == tailing:
            # A[0] + A[1] + ... + A[P-1] == A[P+1] + ... + A[N-2] + A[N-1]
            return index
        heading += A[index]
    else:
        # No equilibrium is found.
        return -1

def solution(A):
    right = sum(
        A[1:])  # Sum all values and start counting from second item since first should be considered equilibrium
    left = 0  # At beginning all the values at the left of the slice are zero
    for idx in range(len(A)):
        if idx > 0:  # Only proceed to add/substract numbers from the array slices when idx is major than zero since we do not consider the first item at beginnig
            left += A[idx - 1]
            right -= A[idx]
        if left == right:
            return idx
    # As double check I used the sum of arrays, which is not performant (n**2) to check if right and left slices sum is equal
    # print ('sum', sum(A[:idx]), sum(A[idx+1:]))
    # print ('lr', left, right)
    return -1