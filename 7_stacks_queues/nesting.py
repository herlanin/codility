def solution(S):
    parentheses = 0
    for element in S:
        if element == "(":
            parentheses += 1
        else:
            parentheses -= 1
            if parentheses < 0:
                return 0
    if parentheses == 0:
        return 1
    else:
        return 0

def solution(S):
    stack = []
    for p in S:
        if p == '(':
            stack.append(p)
        else:
            try:
                stack.pop()
            except Exception as e:
                return 0
    return 1 if not stack else 0