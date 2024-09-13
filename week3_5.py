def main():
    #No. 1
    a = 0
    b = 0
    while a == 0 and b == 0 or ((a < 0 and b > 0) or (a > 0 and b < 0)):
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))
        
        if ((a < 0 and b > 0) or (a > 0 and b < 0)):
            print("a and b must be same in sign, try again...")
        else:
            print(f"The GCD of first and second integer is: {GCD(a, b)} ")
            if GCD(a, b) == 1:
                print("(Coprime)")

    #No.2
    x = -1
    while x < 0:
        x = int(input("\nEnter natural number: "))
        if x < 0:
            print("Negative is not valid, try again...")
    
    print(f"f({x}) = {x}^2 + 3")
    print(f"f({x}) = {naturalNum(x)}")

    #No.3
    n = int(input("\nEnter integer number: "))
    print(f"f({n}) = 3({n})")
    print(f"f({n}) = {intNum(n)}")

def GCD(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

def naturalNum(x):
    return x**2 + 3

def intNum(n):
    return 3 * n

main()