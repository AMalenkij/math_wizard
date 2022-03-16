# greatest common division(GCD)
def gcd(a: int = 34, b: int = 12) -> int:
    ans = 0
    while True:
        print('test')
        if a > b:
            ans = a - b
        elif b > a:
            ans = b - a
        if ans > 0:
            if a % ans == 0 and b % ans == 0:
                return ans
                break


if __name__ == '__main__':
    assert gcd(36, 24) == 12
    assert gcd(34, 12) == 2
    assert gcd(15, 10) == 5
    assert gcd(90, 20) == 10
