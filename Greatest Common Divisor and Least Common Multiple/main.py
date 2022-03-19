# Greatest common divisor(GCD)
def gcd(*args: int) -> int:
    print('start-----------------------')
    answer = []
    count = 0
    list_factor = []
    for _ in args:
        list_factor.append(factor(_))

    print(list_factor)
    for g in args[1:]:
        for t in list_factor[0]:
            for z in list_factor[args.index(g)]:
                if t == z:
                    print(t, z, g)
                    count += 1
                    list_factor[args.index(g)].pop(list_factor[args.index(g)].index(z))
                    if count == len(args) - 1:
                        print('gggg')
                        answer.append(t)
                        #                        list_factor[0].pop(list_factor[0].index(t))
                        count = 0
                        break
                    break
    print(answer)
    print(list_factor)
    return multiply(answer)


# Least common multiple(LCM)
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

    assert gcd(36, 24, 12) == 12
    assert gcd(34, 12, 4) == 2
    assert gcd(15, 10, 5) == 5
    assert gcd(90, 20, 10) == 10
    assert gcd(13, 11, 2) == 1
    assert gcd(24, 32, 16) == 8

    assert gcd(36, 24, 12, 4) == 4
