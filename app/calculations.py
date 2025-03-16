def add(num1: int, num2: int):
  return num1 + num2

def subtract(num1: int, num2: int):
  return num1 - num2

def multiply(num1: int, num2: int):
  return num1 * num2

def divide(num1: int, num2: int):
  return num1 / num2

class InsufficientFunds(Exception):
  pass

class BankAccount(): 
  def __init__(self, starting_balance = 0):
    self.balance = starting_balance
  
  def depost(self, amount):
    self.balance += amount
    return self.balance
  
  def withdraw(self, amount):
    self.balance -= amount
    if self.balance < 0:
      raise InsufficientFunds("Insufficient funds")
    return self.balance
  
  def collect_interest(self): 
    self.balance *= 1.01
    return self.balance
