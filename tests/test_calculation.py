from app.calculation import add, subtract, multiply, BankAccount
import pytest

# for using pytest file name should look like this test_anyname.py or anyname_test.py
# also naming of the function also metter when we auto tests
# the function name which we are going to test that name should be indecated in the test function name
# name of function should start with test


@pytest.fixture  # here fixture decoreate run this function first and will create instance of class bankaccout
def zero_bank_account():
    return BankAccount()


@pytest.fixture
def bank_account():
    return BankAccount(50)
# this is called parametrize which help us to give many test case


@pytest.mark.parametrize("num1,num2, result", [(2, 3, 5), (4, 5, 9), (23, 23, 46)])
def test_add(num1, num2, result):
    print("Testing  of the add funvtion")
    assert add(num1, num2) == result


def test_subtract():
    print("testing of  subtract function")
    assert subtract(9, 5) == 4


def test_multiply():
    print("testing of multiply function ")
    assert multiply(9, 11) == 99


def test_bank_set_intial_amount(bank_account):

    assert bank_account.balance == 50


def test_bank_defualt_amout(zero_bank_account):

    assert zero_bank_account.balance == 0


def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30


def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 70


def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55


@pytest.mark.parametrize("deposit,withdraw, total_ammout",
                         [(200, 100, 100), (300, 50, 250), (500, 150, 350)])
def test_bank_transation(zero_bank_account, deposit, withdraw, total_ammout):
    zero_bank_account.deposit(deposit)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == total_ammout


# for pytest to print print statemt use -s for more detail use -v then use the commad pytest -v -s
