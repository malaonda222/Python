# T-Shirt
def make_shirt(size:str, sentence:str) -> list[str, str]:
    print(f"The t-shirt is size {size} and has the following sentence printed on it: {sentence}")

make_shirt("XL", "Daje tutta")
make_shirt(sentence="Daje tutta", size="XL")



def make_shirt(size: str, sentence: str):
    print(f"La taglia è {size} e la frase è {sentence}.")

maglia_1 = make_shirt("L", "Forza Roma")