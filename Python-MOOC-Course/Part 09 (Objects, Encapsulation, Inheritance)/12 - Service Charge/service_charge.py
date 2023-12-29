class BankAccount:
    def __init__(self, name: str, acct_num: str, balance: float):
        self.__name = name
        self.__acct_num = acct_num
        self.__balance = balance
    
    def deposit(self, amount: float):
        self.__balance += amount 
        self.__service_charge()
    
    def withdraw(self, amount: float):
        self.__balance -= amount
        self.__service_charge()

    @property
    def balance(self):
        return self.__balance
    
    def __service_charge(self):
        self.__balance *= 0.99
    
if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)