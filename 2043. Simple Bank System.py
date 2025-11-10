from typing import List
class Bank:
    def __init__(self, balance: List[int]):
        self.balances = balance
        self.balances.insert(0,0)
        self.max_x = len(balance)
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.max_x or account2 > self.max_x or self.balances[account1] < money:
            return False
        self.balances[account1] -= money
        self.balances[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > self.max_x:
            return False
        self.balances[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.max_x or money > self.balances[account]:
            return False
        self.balances[account] -= money
        return True

        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)