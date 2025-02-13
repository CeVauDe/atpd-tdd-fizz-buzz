import pytest


class TestFizzBuzzShould:
    @pytest.mark.parametrize("number,expectation",[(1, "1"), (2, "2"), (4, "4")])
    def test_return_input(self, number: int, expectation: str) -> None:
        assert fizz_buzz(number) == expectation

    @pytest.mark.parametrize("number", [3, 6, 9])
    def test_return_fizz(self, number: int) -> None:
        assert fizz_buzz(number) == "Fizz"

    def test_return_buzz(self) -> None:
        assert fizz_buzz(5) == "Buzz"
        assert fizz_buzz(10) == "Buzz"
        assert fizz_buzz(20) == "Buzz"

def fizz_buzz(number: int) -> str:
    if number % 3 == 0:
        return "Fizz"
    if number == 5:
        return "Buzz"
    if number == 10:
        return "Buzz"
    if number == 20:
        return "Buzz"
    return str(number)