def solution(K, A):
    # The number of tied ropes, whose lengths
    # are greater than or equal to K.
    count = 0
    # The length of current rope (might be a tied one).
    length = 0
    for rope in A:
        length += rope  # Tied with the previous one.
        # Find a qualified rope. Prepare to find the
        # next one.
        if length >= K:     count += 1; length = 0
    return count


def solution(k, A):
    cnt = 0
    previousNotLenght = 0
    for x in A:
        if x >= k:
            cnt += 1
            previousNotLenght = 0
        elif previousNotLenght + x >= k:
            cnt += 1
            previousNotLenght = 0
        else:
            previousNotLenght += x
    return cnt
