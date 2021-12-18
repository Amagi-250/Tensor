import equation

class TestEquation:

    def test_equation_1_minus6_8(self):
        assert equation.equation(1, -6, 8) == (4, 2)
    
    def test_equation_1_4_4(self):
        assert equation.equation(1, 4, 4) == (-2)

    def test_equation_1_6_45(self):
        assert equation.equation(1, 6, 45) == (3+6j, 3-6j)