class Counter:
    counter = 0

    @classmethod
    def increment(cls):
        cls.counter += 1
    
    @classmethod
    def get_count(cls):
        return cls.counter
    
   

Counter.increment()
Counter.increment()
Counter.increment()


print(f"Valore attuale del contatore: {Counter.get_count()}.")