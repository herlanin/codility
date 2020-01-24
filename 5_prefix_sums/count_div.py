def solution(A, B, K):
    if A % K == 0:
        return (B - A) // K + 1
    else:
        return (B - (A - A % K)) // K


def solution(A, B, K):
    edge = 1 if A % K == 0 else 0
    return B // K - A // K + edge
