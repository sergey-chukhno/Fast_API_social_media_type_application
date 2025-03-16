import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFunds

@pytest.fixture
def zero_bank_account():
  return BankAccount()

@pytest.fixture
def bank_account():
  return BankAccount(100)

@pytest.mark.parametrize("num1, num2, result", [(5,3,8), (5,4,9), (7,3,10), (6,3,9)])

def test_add(num1, num2, result): 
  print("testing add function")
  assert add(num1, num2)==result
  print("add function test passed")


def test_subtract():
  assert subtract(5,3)==2
  print("subtract function test passed")

def test_multiply():
  assert multiply(5,3)==15
  print("multiply function test passed")

def test_divide():
  assert divide(6,3)==2
  print("divide function test passed")

def test_bank_account(bank_account):
  assert bank_account.balance==100

def test_bank_default_amount(zero_bank_account):
  assert zero_bank_account.balance==0

def test_withdraw(bank_account):
  assert bank_account.withdraw(50)==50

def test_deposit(bank_account):
  assert bank_account.depost(50)==150

def test_collect_interest(bank_account): 
  assert bank_account.collect_interest()==101
  print("collect_interest function test passed")

def test_transaction(zero_bank_account):
  zero_bank_account.depost(50)
  zero_bank_account.withdraw(20)
  assert zero_bank_account.balance==30
  print("transaction test passed")

def test_insufficient_funds(bank_account):
  with pytest.raises(InsufficientFunds):
    bank_account.withdraw(500)
