# greatest common division(GCD)
def gcd(a: int = 90, b: int = 20) -> int:
    answer = []
    copy_b = factor(b)
    for t in factor(a):
        for z in copy_b:
            if t == z:
                answer.append(t)
                copy_b.pop(copy_b.index(z))
                break
    return multiply(answer)


def multiply(lst: list) -> list:
    answer = 1
    for i in lst:
        answer *= i
    return answer


def factor(n: int) -> list:
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
