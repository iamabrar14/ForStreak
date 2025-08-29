class Bank:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance #encapsulated using (__)
    def deposit(self,amount):
        self.__balance +=amount
    def get_balance(self):
        return self.__balance
obj=Bank("Abrar",1000)
obj.deposit(500)
print(obj.get_balance()) #Accesing private value by calling function