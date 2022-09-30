from random import randint


elements = ["terre", "air", "eau", "feu", "fer", "vide", "lumière"]
index = randint(0, len(elements) - 1)
print(elements[index])