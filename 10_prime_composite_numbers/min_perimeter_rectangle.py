def solution(N):
    from math import sqrt
    for i in range(int(sqrt(N)), 0, -1):
        if N % i == 0:
            return 2*(i+N/i)