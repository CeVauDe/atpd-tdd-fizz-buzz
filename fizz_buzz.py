import pytest


class TestFizzBuzzShould:
    @pytest.mark.parametrize("number,expectation",[(1, "1"), (2, "2"), (4, "4")])
    def test_return_input(self, number: int, expectation: str) -> None:

        assert fizz_buzz(number) == expectation


def fizz_buzz(number: int) -> str:
    return str(number)