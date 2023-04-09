from app.calculation import add, subtract, multiply

# for using pytest file name should look like this test_anyname.py or anyname_test.py
# also naming of the function also metter when we auto tests
# the function name which we are going to test that name should be indecated in the test function name
# name of function should start with test


def test_add():
    print("Testing  of the add funvtion")
    assert add(5, 3) == 8
    assert add(9, 11) == 20

def test_subtract():
    print("testing of  subtract function")
    assert subtract(9,5)==4

def test_multiply():
    print("testing of multiply function ")
    assert multiply(9,11) == 99

# for pytest to print print statemt use -s for more detail use -v then use the commad pytest -v -s
