def solution(A):
    d = 6
    n = len(A)
    max_score = [A[0]] * d
    for p in range(1, n):
        max_score[p % d] = max(max_score) + A[p]
    return max_score[(n - 1) % d]