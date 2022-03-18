# Greatest common divisor(GCD)
def gcd(a: int, b: int) -> int:
    answer = []
    copy_b = factor(b)
    for t in factor(a):
        for z in copy_b:
            if t == z:
                answer.append(t)
                copy_b.pop(copy_b.index(z))
                break
    return multiply(answer)


# Least common multiple
def lcm(a: int, b: int) -> int:
    answer = []
    copy_b = factor(b)
    copy_a = factor(a)
    for t in factor(a):
        for z in copy_b:
            if t == z:
                answer.append(t)
                copy_b.pop(copy_b.index(z))
                copy_a.pop(copy_a.index(t))
                break
    return multiply(answer + copy_b + copy_a)


def multiply(lst: list) -> int:
    answer = 1
    for i in lst:
        answer *= i
    return answer


def factor(n: int) -> list:
    answer = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            answer.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        answer.append(n)
    return answer


if __name__ == '__main__':
    assert gcd(36, 24) == 12
    assert gcd(34, 12) == 2
    assert gcd(15, 10) == 5
    assert gcd(90, 20) == 10
    assert gcd(13, 11) == 1
    assert gcd(24, 32) == 8

    assert lcm(36, 24) == 72
    assert lcm(34, 12) == 204
    assert lcm(15, 10) == 30
    assert lcm(90, 20) == 180
    assert lcm(13, 11) == 143
    assert lcm(24, 32) == 96
