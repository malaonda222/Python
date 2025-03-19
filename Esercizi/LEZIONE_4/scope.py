global lock

def thread():
    
    if not lock:
        import json
        lock = True
        
        dict_1 = json.load("file.json")
        
        lock = False


value = 0
print(f"Prima: {value=}")

def modify():
    value = 1
    print(f"Mentre: {value=}")

modify()
print(f"Dopo: {value=}")


value = 0
print(f"Prima: {value=}")

def modify(value):
    value = 1
    print(f"Mentre: {value=}")
    for i in range(10):
        value += 1
        print(f"Nel For: {value=}")
    
    print(f"Dopo il For: {value=}")

modify(value)
print(f"Dopo: {value}")



lock = False
def thread():
    global lock
    if not lock:    
        lock = True
        import json
        json.load("file.json")
        lock = False

print(f"Thread: {lock=}")

