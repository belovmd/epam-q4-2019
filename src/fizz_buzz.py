"""FizzBuzz script.

Another variant.
def FizzBuzz (number):
    fizz,buzz,str_number="Fizz","Buzz",str(number)
    if(number%3!=0):
        fizz=""
    else:
        str_number=""
    if(number%5!=0):
        buzz=""
    else:
        str_number=""
    print(fizz+buzz+str_number)


for number in range(1, 101, 1):
    FizzBuzz (number)
"""

for idx in range(1, 101):
    print("Fizz" * (idx % 3 == 0) + "Buzz" * (idx % 5 == 0) or str(idx))
