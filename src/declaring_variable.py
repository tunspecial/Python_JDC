
def show_value_type(value:str):
    print(f"value of varaible : {value}")
    print(f"value of varaible type : {type(value).__name__}")
    print(value.numerator())
    

if __name__ == "__main__":

    name= "python"
    show_value_type(name)

    name:int = name * 3
    show_value_type(name)
    
    name = "hello"
    show_value_type(name)

name:str = "hello python"

