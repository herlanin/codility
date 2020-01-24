def gcd(x, y):
    ''' Compute the greatest common divisor.
    '''
    if x%y == 0:
        return y;
    else:
        return gcd(y, x%y)
def removeCommonPrimeDivisors(x, y):
    ''' Remove all prime divisors of x, which also exist in y. And
        return the remaining part of x.
    '''
    while x != 1:
        gcd_value = gcd(x, y)
        if gcd_value == 1:
            # x does not contain any more
            # common prime divisors
            break
        x /= gcd_value
    return x
def hasSamePrimeDivisors(x, y):
    gcd_value = gcd(x, y)   # The gcd contains all
                            # the common prime divisors
    x = removeCommonPrimeDivisors(x, gcd_value)
    if x != 1:
        # If x and y have exactly the same common
        # prime divisors, x must be composed by
        # the prime divisors in gcd_value. So
        # after previous loop, x must be one.
        return False
    y = removeCommonPrimeDivisors(y, gcd_value)
    return y == 1
def solution(A, B):
    count = 0
    for x,y in zip(A,B):
        if hasSamePrimeDivisors(x,y):
            count += 1
    return count





def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def solution(A, B):
    # write your code in Python 2.7
    cnt = 0
    for i in xrange(len(A)):
        a, b = A[i], B[i]
        g = gcd(a, b)
        while True:
            d = gcd(a, g)
            if 1 == d:
                break
            a /= d
        while True:
            d = gcd(b, g)
            if 1 == d:
                break
            b /= d
        cnt += 1 if a == 1 and b == 1 else 0
    return cnt