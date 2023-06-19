#prime number checker code


number = int(input("Please give the number to check: "))

if number < 2:
    print(number, "is not prime")
else:
    is_prime = True
    for i in range(2, int(number/2)):
        if (number%i==0):
            print("number is not prime")
            is_prime = False
            break
    

if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")