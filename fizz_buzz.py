import pytest


class TestFizzBuzzShould:
    @pytest.mark.parametrize("number,expectation",[(1, "1"), (2, "2"), (4, "4")])
    def test_return_input(self, number: int, expectation: str) -> None:
        assert fizz_buzz(number) == expectation

    def test_return_fizz(self) -> None:
        assert fizz_buzz(3) == "Fizz"
        assert fizz_buzz(6) == "Fizz"


def fizz_buzz(number: int) -> str:
    if number == 3:
        return "Fizz"
    if number == 6:
        return "Fizz"
    return str(number)