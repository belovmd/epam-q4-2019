'''
FizzBuzz 
'''

for i in range(100):

    if i % 5 == 0 and i % 3 == 0:
        i = "FizzBuzz" 

    elif i % 3 == 0:
        i = "Fizz" 

    elif i % 5 == 0:
        i = "Buzz"
        
    print(i)
