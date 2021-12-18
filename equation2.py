
import math

def equation(a, b, c):

    D = b**2 - 4*a*c
    
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return x1, x2
    elif D == 0:
        x = -b / (2*a)
        return x
    
    #else:
        #print("Дискриминант меньше нуля. Корней нет")

    else:
        x1 = complex(b, math.sqrt(abs(D))) / (2*a)
        x2 = complex(b, -math.sqrt(abs(D))) / (2*a)
        return x1, x2