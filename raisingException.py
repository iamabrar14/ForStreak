def set_age(age):
    if age<0:
        raise ValueError("Age cannot be negative")
    else:
        print("Age set to : ",age)
set_age(25)
set_age(-5)