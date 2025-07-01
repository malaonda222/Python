class MathOperations:
    @staticmethod 
    def add(a: float, b: float) -> float:
        return a + b 
    
    @staticmethod
    def multiply(c: float, d: float) -> float:
        return c * d 


print(f"Somma di 12.3 e 18.2: {MathOperations.add(12.3, 18.2)}")
print(f"Moltiplicazione di 17.9 e 18.5: {MathOperations.multiply(17.9, 18.5)}")
