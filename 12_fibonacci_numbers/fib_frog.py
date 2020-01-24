def fibonacciDynamic(n):
    # Generate and return all the Fibonacci numbers,
    # less than or equal to n, in descending order.
    # n must be larger than or equal to one.
    fib = [0] * (n + 2)
    fib[1] = 1
    for i in xrange(2, n + 2):
        fib[i] = fib[i - 1] + fib[i - 2]
        if fib[i] > n:
            return fib[i - 1: 1: -1]
        elif fib[i] == n:
            return fib[i: 1: -1]


def solution(A):
    class Status(object):
        # Object to store the status of attempts
        __slots__ = ('position', 'moves')

        def __init__(self, pos, moves):
            self.position = pos
            self.moves = moves
            return

    lenA = len(A)  # Array length
    fibonacci = fibonacciDynamic(lenA + 1)  # Fibonacci numbers
    statusQueue = [Status(-1, 0)]  # Initially we are at position
    # -1 with 0 move.
    nextTry = 0  # We are not going to delete the tried attemp.
    # So we need a pointer to the next attemp.
    accessed = [False] * len(A)  # Were we in this position before?
    while True:
        if nextTry == len(statusQueue):
            # There is no unprocessed attemp. And we did not
            # find any path yet. So no path exists.
            return -1
        # Obtain the next attemp's status
        currentStatus = statusQueue[nextTry]
        nextTry += 1
        currentPos = currentStatus.position
        currentMoves = currentStatus.moves
        # Based upon the current attemp, we are trying any
        # possible move.
        for length in fibonacci:
            if currentPos + length == lenA:
                # Ohhh~ We are at the goal position!
                return currentMoves + 1
            elif currentPos + length > lenA
                or A[currentPos + length] == 0
                or accessed[currentPos + length]:
                # Three conditions are moving too far, no
                # leaf available for moving, and being here
                # before respectively.
                # PAY ATTENTION: we are using Breadth First
                # Search. If we were here before, the previous
                # attemp must achieved here with less or same
                # number of moves. With completely same future
                # path, current attemp will never have less
                # moves to goal than previous attemp. So it
                # could be pruned.
            continue
            # Enqueue for later attemp.
            statusQueue.append(
                Status(currentPos + length, currentMoves + 1))
            accessed[currentPos + length] = True


def F_upto_A(L):
    # Fibonacci sequence up to the
    # length of A (include starting and destination position)
    F = []
    F.append(0)
    F.append(1)
    while F[-1] <= L:
        F.append(F[-1] + F[-2])
    return F[1:-1]


def solution(A):
    # add starting position to A
    A.insert(0, 1)
    # add destination position to A
    A.append(1)  # [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1]
    n = len(A)  # 13
    # store available fibonacci jumps
    F = F_upto_A(n)  # [1, 1, 2, 3, 5, 8, 13]
    # S mapping A in position
    # and storing the minimum step count to every "1" position
    S = [n] * n
    S[0] = 0  # [0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
    for i in range(1, n):
        # check if the position is 1 in A
        if A[i] == 1:
            # loop the Fibonacci sequence
            for x in F:
                # previous position
                prev = i - x
                if prev >= 0:
                    # (the minimum step count of the previous position)
                    # plus
                    # (one more step to the existing position)
                    # if less than the step count of the existing position
                    # update the step count of the existing position
                    if S[prev] + 1 < S[i]:
                        S[i] = S[prev] + 1
                else:
                    break
    # return the last position of S, if S[-1]==n ,
    # means destination can'tbe reached
    # S:[0, 13, 13, 13, 13, 1, 13, 2, 13, 13, 13, 13, 3]
    return S[-1] if S[-1] < n else -1
