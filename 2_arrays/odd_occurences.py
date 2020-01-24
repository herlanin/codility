"""A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times."""


# O(N) or O(N*log(N))
def solution1(A):
    A.sort()
    if len(A) == 1:
        return A[0]
    for a, b in [A[x:x + 2] for x in range(0, len(A), 2)][:-1]:
        if a != b:
            return a
    return A[-1]


# O(N) or O(N*log(N))
def solution2(A):
    bag = set()
    for n in A:
        if n in bag:
            bag.remove(n)
        else:
            bag.add(n)
    return bag.pop()


# O(N) or O(N*log(N))
def solution3(A):
    # write your code in Python 2.7
    ocurrences = dict()
    for n in A:
        if ocurrences.get(n):
            ocurrences[n] += 1;
        else:
            ocurrences[n] = 1;
    for n in ocurrences:
        if ocurrences[n] % 2 != 0:
            return n
    pass


# O(N) or O(N*log(N))
def solution4(A):
    result = 0
    for number in A:
        result ^= number
    return result


def main():
    solution1([9, 7, 9, 3, 9, 7, 9])
    solution2([9, 7, 9, 3, 9, 7, 9])
    solution3([9, 7, 9, 3, 9, 7, 9])
    solution4([9, 7, 9, 3, 9, 7, 9])



if __name__ == "__main__":
    main()
