"""You are given an integer n. Count the total of 1+2+ ... + n."""


def solution(N):
    return N * (N + 1) // 2


def main():
    print(solution(4))


if __name__ == "__main__":
    main()
