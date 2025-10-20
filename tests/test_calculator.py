from src.calculator import add_integer

def test_positive_number():
    assert add_integer(2 , 3)

def test_negative_numer():
    assert add_integer(-2 , -3)
    
def test_posiive_negative_number():
    assert add_integer (-3 , 2)
    
def test_negative_negative_number():
    assert add_integer(-3 , -3)
    
