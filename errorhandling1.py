"""An exception is an error that occurs during program execution
python provides us try-except block to handle error
"""
try:
    a=int(input("Enter an integer number : "))
    print("The number is : ",a)
except:
    print("This is not an integer number")