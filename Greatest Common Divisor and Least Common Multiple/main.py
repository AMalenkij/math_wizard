# greatest common division(GCD)
def gcd(a: int = 90, b: int = 20) -> int:
    answer = []
    for x in range(min(len(factor(a)), len(factor(b)))):
        if factor(a)[x] == factor(b)[x]:
            answer.append(factor(a)[x])
    return multiply(answer)


def multiply(lst):
    answer = 1
    for i in lst:
        answer *= i
    return answer


def factor(n):
    anse = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            anse.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        anse.append(n)
    return anse


if __name__ == '__main__':
    assert gcd(36, 24) == 12
    assert gcd(34, 12) == 2
    assert gcd(15, 10) == 5
    assert gcd(90, 20) == 10
