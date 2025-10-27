subject = [
    "Java" , "Python" , "C++" , "JavaScript" , "TypeScript" , "Dart" , "Kotlin"
]


if __name__ == "__main__":
    subject_dict:dict[int, str] = {}
    
    for id , subject in enumerate(subject , start=1):
        subject_dict[id] = subject
        
    for entry in subject_dict.items():
        print(f"Entry is : {entry}")

    
    
    