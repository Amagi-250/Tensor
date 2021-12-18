import circle


class TestCircle:

    
    #Первая часть разработки через тестирование TDD
    def test_square_5(self):
        assert circle.square(5) == 78.53981633974483
    
    
    #Вторая часть (новое условие задачи) разработки через тестирование TDD
    def test_perimeter_5(self):
        assert circle.perimeter(5) == 31.41592653589793
