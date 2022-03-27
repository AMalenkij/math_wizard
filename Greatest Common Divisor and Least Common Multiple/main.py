from collections import Counter


class Calculator:
    @staticmethod
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

    @staticmethod
    def multiply(lst: list) -> int:
        answer = 1
        for i in lst:
            answer *= i
        return answer

    def prime_factorization_gcd(self, *args: int) -> list:
        """
        Prime factorization of a number is breaking a number down into the
        set of prime numbers which multiply together to result in the original number.
        """
        answer = []
        dct = Counter(self.factor(args[0]))
        for _ in range(1, len(args)):
            cnt = Counter(self.factor(args[_]))
            for key, value in cnt.items():
                dct[key] = str(dct[key]) + str(value)
                if len(args) == len(dct[key]):
                    answer.append(int(key) ** int(min(dct[key])))
        return answer

    def gcd(self, *args: int) -> int:
        """
        In mathematics, the greatest common divisor (GCD)
        of two or more integers, which are not all zero,
        is the largest positive integer that divides each of the integers.
        """
        return self.multiply(self.prime_factorization_gcd(*args))

    def prime_factorization_lcm(self, *args: int) -> list:
        """
        Prime factorization of a number is breaking a number down into the
        set of prime numbers which multiply together to result in the original number.
        """
        answer = []
        dct = Counter(self.factor(args[0]))
        for _ in range(1, len(args)):
            cnt = Counter(self.factor(args[_]))
            for key, value in cnt.items():
                if key in dct:
                    if dct[key] < value:
                        dct[key] = value
                elif key not in dct:
                    dct[key] = value
        for key, value in dct.items():
            for _ in range(value):
                answer.append(key)
        return answer

    def lcm(self, *args: int) -> int:
        """
        The least common multiple (LCM)
        of two integers is the smallest positive integer that is a multiple of both numbers.
        """
        return self.multiply(self.prime_factorization_lcm(*args))


