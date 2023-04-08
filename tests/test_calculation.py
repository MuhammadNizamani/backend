from app.calculation import add

# for using pytest file name should look like this test_anyname.py or anyname_test.py


def test_add():
    assert add(5, 3) == 8
    assert add(9, 11) == 20
