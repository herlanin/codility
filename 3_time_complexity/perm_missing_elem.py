"""An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)]."""

#O(N) or O(N * log(N))
def solution(A):
    length = len(A)
    xor_sum = 0
    for index in range(0, length):
        xor_sum = xor_sum ^ A[index] ^ (index + 1)
    return xor_sum ^ (length + 1)

#O(N) or O(N * log(N))
def solution2(A):
    N = len(A)
    mysum = 0
    for i in range(0, N):
        mysum += ((i + 1) - A[i])
    return mysum + (N + 1)

#O(N) or O(N * log(N))
def solution3(A):
    N = len(A) + 1
    sum_N = (N * (N+1)) / 2
    return int(sum_N - sum(A))


