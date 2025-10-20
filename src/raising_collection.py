if __name__ == "__main__":
    my_fav_food:set = set()
    
    while True:
        user_data = input("what is your fav food : ")
        
        if "Nothing" == user_data:
            break
        
        my_fav_food.add(user_data)
    
    print(f"your fav food is : {", ".join(my_fav_food)}")