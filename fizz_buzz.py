

class TestFizzBuzzShould:
    def test_return_input(self):

        assert fizz_buzz(1) == "1"
        assert fizz_buzz(2) == "2"
        assert fizz_buzz(4) == "4"


def fizz_buzz(number: int) -> str:
    return str(number)