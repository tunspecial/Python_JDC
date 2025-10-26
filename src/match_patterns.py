##Case Values :
    ##literlals booleans, numbers, strings, enums
    
def get_status(value:int) -> str:
    result = ""
    
    match value:
        case 100 :
            result = "Informational responses"
        case 200 :
            result = "Successful responses"
        case 300 :
            result = "Redirection messages"
        case 400 :
            result = "Client error responses"
        case 500 :
            result = "Server error responses"
        case _ :
            result = "This is Impossible"
    
    return result

##Case Patterns :
    ##structures like sequences, mappings, classes, gurded patterns
def pass_grande(mark : int) -> str:
    result = "Nothing"
    
    match mark:
        case m if m >= 0 and m < 40:
            result = "Fail"
        case m if m >= 40 and m < 80:
            result = "Pass"
        case m if m >= 80  and m <= 100:
            result = "Excellent"
        case _ :
            result = "This is Impossible"
            
    return result

## Case Mixed Patterns
def show(data):
    
    match data :
        case n if type(data).__name__ == "int" and  n >= 0 :
            print("Positive Number")
        case n if type(data).__name__ == "int" and n < 0 :
            print("Negative Number")
        case [1,2,3]:
            print("Sequence Number : 1,2,3")
        case [1 , *rest ]:
            print("Sequence Start with 1")
        case{"name" : name , "age" : age}:
            print(f"your name is {name} and age is {age} years old")
        case _:
            print("None Of Above Pathen")
            
if __name__ == "__main__":
    # print(get_status(400))
    # print(pass_grande(-1))
    (show(1))
    (show(-1))
    (show([1,2,3]))
    (show([1,2,3,4,5,6]))
    (show({"name" : "Mg Mg" , "age" : 21}))