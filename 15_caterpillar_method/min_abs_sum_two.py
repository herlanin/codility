def solution(A):
    A.sort()  # Sort A in non-decreasing order
    if A[0] >= 0:   return A[0] + A[0]  # All non-negative
    if A[-1] <= 0:  return -A[-1] - A[-1]  # All non-positive
    front, back = len(A) - 1, 0
    minAbs = A[-1] + A[-1]  # Final result
    # Travel the array from both ends to some center point.
    # See following post for the proof of this method.
    # https://codesays.com/2014/solution-to-min-abs-sum-of-two-by-codility
    while back <= front:
        temp = abs(A[back] + A[front])
        # Update the result if needed
        if temp < minAbs:  minAbs = temp

        # Adjust the pointer for next trying
        if back == front:
            break
        elif abs(A[back + 1] + A[front]) <= temp:
            back += 1
        elif abs(A[back] + A[front - 1]) <= temp:
            front -= 1
        else:
            back += 1;
            front -= 1
    return minAbs


def solution(A):
    A.sort()
    back, front = 0, len(A) - 1
    min_abs_sum = abs(A[0] * 2)
    while back <= front:
        # These are three situations where we don't need to proceed because it won't get any better
        if A[back] > 0:
            # 1. First element (the smallest one) in the caterpillar is positive, which means all elements
            #    are positive. The smallest absolute sum for this caterpillar is if we sum this smallest
            #    element with itself. So there is no point in checking the others, just return either that
            #    sum or the current min_abs_sum.
            return min(min_abs_sum, A[back] * 2)
        if A[front] < 0:
            # 2. Last element (the biggest one) in the caterpillar is negative, which means all elements
            #    are negative. The smallest absolute sum for this caterpillar is if we sum this biggest
            #    (least negative) element with itself. So there is no point in checking the others,
            #    just return either that sum or the current min_abs_sum.
            return min(min_abs_sum, A[front] * (-2))
        if A[back] == 0 or A[front] == 0 or min_abs_sum == 0:
            # 3. If we ever get to the zero element or the min_abs_sum is zero, return zero.
            #    Nothing beats zero.
            return 0
        # This is the line where the min_abs_sum is updated - I'm checking the back and front of the
        # caterpillar and trying to lower my min_abs_sum.
        min_abs_sum = min(min_abs_sum, abs(A[back] + A[front]), abs(A[back] * 2), abs(A[front] * 2))
        # This is the part where I decide how to move from this position. If I'm having all positives
        # or all negatives or zero, I won't get to this line (as those are handled at the beginning of
        # the loop. So, I'm having the most positive number on the front, and the most negative number
        # on the back. I'll move from the more extreme one as I want to minimize the sum.
        if A[back] + A[front] < 0:
            back += 1
        else:
            front -= 1
    return min_abs_sum
