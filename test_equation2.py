import equation2

class TestEquation:

    #Дискриминант больше нуля
    def test_equation_1_minus6_8(self):
        assert equation2.equation(1, -6, 8) == (4, 2)
    
    #Дискриминант равен нулю
    def test_equation_1_4_4(self):
        assert equation2.equation(1, 4, 4) == (-2)

    #Дискриминант меньше нуля
    #def test_equation_2_minus6_13(self):
        #assert circle.equation(2, -6, 13) == ("Дискриминант меньше нуля. Корней нет")

    #Дискриминат меньше нуля, использование комплексные числа
    def test_equation_1_6_45(self):
        assert equation2.equation(1, 6, 45) == (3+6j, 3-6j)