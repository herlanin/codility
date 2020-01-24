def solution(A):
    counter = [0]*len(A)
    limit = len(A)
    for element in A:
        if not 1 <= element <= limit:
            return 0
        else:
            if counter[element-1] != 0:
                return 0
            else:
                counter[element-1] = 1
    return 1

def solution2(A):
    if set(A) == set(range(1, 1+len(A))):
        return 1
    else:
        return 0