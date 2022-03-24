from collections import Counter


def gcd(*args: int) -> int:
    """
    In mathematics, the greatest common divisor (GCD)
    of two or more integers, which are not all zero,
    is the largest positive integer that divides each of the integers.
    """
    answer = []
    dct = Counter(factor(args[0]))
    for _ in range(1, len(args)):
        cnt = Counter(factor(args[_]))
        for key, value in cnt.items():
            dct[key] = str(dct[key]) + str(value)
            if len(args) == len(dct[key]):
                answer.append(int(key) ** int(min(dct[key])))
    return multiply(answer)


def lcm(*args: int) -> int:
    """
    The least common multiple (LCM)
    of two integers is the smallest positive integer that is a multiple of both numbers.
    """
    answer = []
    dct = Counter(factor(args[0]))
    for _ in range(1, len(args)):
        cnt = Counter(factor(args[_]))
        for key, value in cnt.items():
            if key in dct:
                if dct[key] < value:
                    dct[key] = value
            elif key not in dct:
                dct[key] = value
    for key, value in dct.items():
        for _ in range(value):
            answer.append(key)
    return multiply(answer)


def multiply(lst: list) -> int:
    answer = 1
    for i in lst:
        answer *= i
    return answer


def factor(n: int) -> list:
    """
    A factor is a number that divides another number leaving no remainder.
    """
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

    assert gcd(36, 24, 12) == 12
    assert gcd(34, 12, 4) == 2
    assert gcd(15, 10, 5) == 5
    assert gcd(90, 20, 10) == 10
    assert gcd(13, 11, 2) == 1
    assert gcd(24, 32, 16) == 8

    assert gcd(36, 24, 12, 72) == 12
    assert gcd(34, 12, 4, 8) == 2
    assert gcd(15, 10, 5, 25) == 5
    assert gcd(90, 20, 10, 110) == 10
    assert gcd(13, 11, 2, 3) == 1
    assert gcd(24, 32, 16, 48) == 8

    assert gcd(36, 24, 12, 72, 12) == 12
    assert gcd(252, 180, 96, 60, 24) == 12

    assert lcm(36, 24) == 72
    assert lcm(34, 12) == 204
    assert lcm(15, 10) == 30
    assert lcm(36, 10) == 180
    assert lcm(13, 11) == 143
    assert lcm(24, 32) == 96

    assert lcm(36, 24, 12) == 72
    assert lcm(34, 4, 12) == 204
    assert lcm(15, 10, 5) == 30
    assert lcm(90, 20, 10) == 180
    assert lcm(32, 24, 16) == 96

    assert lcm(36, 24, 12, 72) == 72
    assert lcm(34, 12, 4, 8) == 408
    assert lcm(15, 10, 5, 25) == 150
    assert lcm(90, 20, 10, 110) == 1980
    assert lcm(13, 11, 2, 3) == 858
    assert lcm(24, 32, 16, 48) == 96
