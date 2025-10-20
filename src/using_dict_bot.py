if __name__ == "__main__":
    dictionary = {}
    print("""
+++++++++++++++++
Welcome To My Bot
+++++++++++++++++
          """)
    
    while True:
        question = input("you ===> : ")
        
        if  "Exit" == question:
            break
        
        answer = dictionary.get(question)
        
        if answer != None:
            print(f"Bot ===> {answer}")
            
        else:
            print("I have no idea , please train me")
            
            result = input("you ===> : ")
            
            if result == "Exit":
                break
            
            dictionary[question] = result
            print("Thank you for kind!!")
    print("""
---------------------
Thank You!! Take Care
---------------------
          """)