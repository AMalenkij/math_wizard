from main import Calculator
import pytest


@pytest.mark.parametrize('a, b, expected_result', [(36, 24, 12),
                                                   (34, 12, 2),
                                                   (15, 10, 5),
                                                   (90, 20, 10),
                                                   (13, 11, 1),
                                                   (24, 32, 8)])
def test_gcd_positive_two(a, b, expected_result):
    assert Calculator().gcd(a, b) == expected_result


@pytest.mark.parametrize('a, b, c, expected_result', [(36, 24, 12, 12),
                                                      (34, 12, 4, 2),
                                                      (15, 10, 5, 5),
                                                      (90, 20, 10, 10),
                                                      (13, 11, 2, 1),
                                                      (24, 32, 16, 8)])
def test_gcd_positive_three(a, b, c, expected_result):
    assert Calculator().gcd(a, b, c) == expected_result


@pytest.mark.parametrize('a, b, c, d, expected_result', [(36, 24, 12, 72, 12),
                                                         (34, 12, 4, 8, 2),
                                                         (15, 10, 25, 5, 5),
                                                         (90, 20, 110, 10, 10),
                                                         (13, 11, 3, 2, 1),
                                                         (24, 32, 48, 16, 8)])
def test_gcd_positive_four(a, b, c, d, expected_result):
    assert Calculator().gcd(a, b, c, d) == expected_result


def test_gcd_positive_five():
    assert Calculator().gcd(36, 24, 12, 72, 12) == 12
    assert Calculator().gcd(252, 180, 96, 60, 24) == 12


@pytest.mark.parametrize('a, b, expected_result', [(36, 24, 72),
                                                   (34, 12, 204),
                                                   (15, 10, 30),
                                                   (90, 20, 180),
                                                   (13, 11, 143),
                                                   (24, 32, 96)])
def test_lcm_positive_two(a, b, expected_result):
    assert Calculator().lcm(a, b) == expected_result


@pytest.mark.parametrize('a, b, c, expected_result', [(36, 24, 12, 72),
                                                      (34, 12, 4, 204),
                                                      (15, 10, 5, 30),
                                                      (90, 20, 10, 180),
                                                      (32, 24, 16, 96)])
def test_gcd_positive_three(a, b, c, expected_result):
    assert Calculator().lcm(a, b, c) == expected_result


@pytest.mark.parametrize('a, b, c, d, expected_result', [(36, 24, 24, 12, 72),
                                                         (34, 12, 4, 8, 408),
                                                         (15, 10, 25, 5, 150),
                                                         (90, 20, 110, 10, 1980),
                                                         (13, 11, 3, 2, 858),
                                                         (24, 32, 48, 16, 96)])
def test_gcd_positive_four(a, b, c, d, expected_result):
    assert Calculator().lcm(a, b, c, d) == expected_result
