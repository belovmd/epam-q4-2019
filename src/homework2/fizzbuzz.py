for i in range(1, 100):
    if (i % 3 == 0 or i % 5 == 0):
        print("Fizz" * (not (i % 3)) + "Buzz" * (not (i % 5)))
    else:
        print(i)
