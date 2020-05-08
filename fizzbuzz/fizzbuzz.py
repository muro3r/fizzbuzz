from typing import List, Union


def fizzbuzz(number: int) -> Union[str, int]:
    if number % 15 == 0:
        return "fizzbuzz"
    if number % 5 == 0:
        return "buzz"
    if number % 3 == 0:
        return "fizz"

    return number


def main(number: int) -> List[Union[str, int]]:
    return [fizzbuzz(i) for i in range(1, number + 1)]
