def solution(X, A):
    covered_time = [-1]*X  # Record the time, each position is covered
    uncovered = X          # Record the number of uncovered position
    for index in range(0,len(A)):
        if covered_time[A[index]-1] != -1:
            # This position is already covered
            continue
        else:
            # This position is to be covered
            covered_time[A[index]-1] = index
            uncovered -= 1
            if uncovered == 0:
                # All positions are covered
                return index
    # Finally, some positions are not covered
    return -1


def solution2(X, A):
    checker=0
    final_val=pow(2,5)-1
    for x in range(len(A)):
        checker=checker| 1<<(A[x]-1)
        if(checker==final_val):
            return x
    return -1


def solution3(X, A):
    # write your code in Python 3.6

    bridge = [0] * (X + 2)
    k = 0
    for idx, i in enumerate(A):
        bridge[i] = 1
        while k <= X and bridge[k + 1] == 1:
            k += 1

        if k == X:
            return idx

    return -1