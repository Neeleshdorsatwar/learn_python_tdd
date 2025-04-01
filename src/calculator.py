#create Caculator class with add method 
import math
class Calculator:
    # constructor 
    def __init__(self):
        self.result = []


    def add(self, a, b):
        self.result.append( a + b )
        return a + b
    
    def substract(self, a, b):
        self.result.append( a - b )
        return a - b
    # ADD FACTORIAL METHOD
    def factorial(self, n):
        if n < 0:
            return None
        elif n == 0:
            return 1
        else:
            return math.factorial(n)
    # ADD MULTIPLICATION METHOD
    def multiply(self, a, b):
        self.result.append( a * b )
        return a * b  
    
    # ADD DIVISION METHOD
    def divide(self, a, b):
        if b == 0:
            return None
        else:
            self.result.append( a / b )
            return a / b


if __name__ == "__main__":
    calc1 = Calculator()  
    calc1.add(1, 2)
    calc1.add(2, 3)
    calc1.add(3, 4)

    calc2 = Calculator()  
    calc2.add(1, -2)
    calc2.add(2, 12)  

    calc3 = Calculator()
    calc3.add(1, 122)
    calc3.add(342, 3)

    print(calc1.result)
    print(calc2.result)
    print(calc3.result)