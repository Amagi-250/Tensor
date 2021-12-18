import circle

class TestCircle:

    def test_square_5(self):
        assert circle.square(5) == 78.53981633974483

    def test_perimeter_5(self):
        assert circle.perimeter(5) == 31.41592653589793