subject = [
    "Java" , "Python" , "C++" , "JavaScript" , "TypeScript" , "Dart" , "Kotlin"
]

def find_with_lenght(input: tuple[str,...] , size: int)-> tuple[str,...]:
    result:list[str] = []
    
    for element in input:
        if len(element) == size :
            result.append(element)
                
    return tuple(result)


if __name__ == "__main__":
    final_result = find_with_lenght(tuple(subject) , 6)
    print(final_result)