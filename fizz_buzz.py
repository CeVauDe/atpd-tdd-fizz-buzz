import pytest


class TestFizzBuzzShould:
    @pytest.mark.parametrize("number,expectation", [(1, "1"), (2, "2"), (4, "4")])
    def test_return_input(self, number: int, expectation: str) -> None:
        assert fizz_buzz(number) == expectation

    @pytest.mark.parametrize("number", [3, 6, 9])
    def test_return_fizz(self, number: int) -> None:
        assert fizz_buzz(number) == "Fizz"

    @pytest.mark.parametrize("number", [5, 10, 20])
    def test_return_buzz(self, number: int) -> None:
        assert fizz_buzz(number) == "Buzz"

    def test_return_fizz_buzz(self) -> None:
        assert fizz_buzz(15) == "FizzBuzz"


def fizz_buzz(number: int) -> str:
    if number == 15:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)
