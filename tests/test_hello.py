from src.hello import say_hello

def test_say_hello():
    result = say_hello("python")
    assert "hello python" == result
