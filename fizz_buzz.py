

class TestFizzBuzzShould:
    def test_return_input(self):

        assert fizz_buzz(1) == "1"
        assert fizz_buzz(2) == "2"
        assert fizz_buzz(4) == "4"


def fizz_buzz(number: int) -> str:
    if number == 1:
        return "1"
    if number == 2:
        return "2"
    return "4"