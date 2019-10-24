"""
Determine if given number is polynome.
"""
num = int(input("Please, enter number to test\n"))

ditgits = []
while num:
    ditgits.append(num % 10)
    num //= 10

while ditgits:
    if ditgits[:1] != ditgits[-1:]:
        print("not poly")
        break
    ditgits = ditgits[1:-1]
else:
    print("poly")
