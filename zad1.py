liczby = input("Podaj liczby rozdzielone przecinkami: ")

lcz = liczby.split(",")

minl = lcz[0]
maxl = lcz[0]
for i in range(0, len(lcz)):
    if lcz[i] < minl:
        minl = lcz[i]
    if lcz[i] > maxl:
        maxl = lcz[i]


print("min:", minl)
print("max:", maxl)
