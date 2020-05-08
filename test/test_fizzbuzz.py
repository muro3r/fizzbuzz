import pytest

from fizzbuzz import fizzbuzz, main


@pytest.mark.parametrize("number", [3, 6, 9])
def test_fizz(number):
    assert fizzbuzz(number) == "fizz"


@pytest.mark.parametrize("number", [5, 10, 20])
def test_buzz(number):
    assert fizzbuzz(number) == "buzz"


@pytest.mark.parametrize("number", [15, 30, 45])
def test_fizzbuzz(number):
    assert fizzbuzz(number) == "fizzbuzz"


def test_numbers():
    assert main(10) == [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz"]
