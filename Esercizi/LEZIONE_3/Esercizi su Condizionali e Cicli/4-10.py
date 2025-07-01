# Slices
cubi = [1, 3, 9, 27, 64, 125, 216, 343, 512, 729, 1000]

print(f"I primi tre elementi della lista sono: ", cubi[:3])

m = len(cubi)//2
cubi_meta = cubi[m:m+3]
print(f"I primi 3 elementi a partire della metà sono: ", cubi_meta)

print(f"Gli ultimi 3 elementi della lista sono: ", cubi[-3:])