def fizzbuzz() :
    z = 1
    while z < 100:

        if z % 5 == 0 and z % 3 == 0:
            print (str(z) + " FizzBuzz")
        elif z % 3 == 0:
            print(str(z) + " Fizz")
        elif z % 5 ==0:
            print( str(z) + " Buzz")
        z += 1
    print("Program Complete")

fizzbuzz()
