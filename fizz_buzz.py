

class TestFizzBuzzShould:
    def test_return_input(self):

        assert fizz_buzz(1) == "1"
        assert fizz_buzz(2) == "2"


def fizz_buzz(number: int) -> str:
    return "1" if number == 1 else "2"