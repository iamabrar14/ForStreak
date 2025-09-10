try:
    num=10
    b=int(input("Enter a divisor : "))
    print("Result ",num/b)
except ZeroDivisionError:
    print("Divisor cannot be zero")
except ValueError:
    print("Wrong input")