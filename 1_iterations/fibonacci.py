"""The Fibonacci numbers form a sequence of integers defined recursively in the
following way. The first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. The first few elements in this sequence are: 0,
1, 1, 2, 3, 5, 8, 13. Let’s write a program that prints all the Fibonacci numbers, not exceeding
a given integer n."""


def solution(n):
    a = 0
    b = 1
    while a <= n:
        print(a)
        c = a + b
        a = b
        b = c


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


def main():
    solution(10)
    print('/n/n/n/n')
    for i in range(10):
        print(recur_fibo(i))

if __name__ == "__main__":
        main()
