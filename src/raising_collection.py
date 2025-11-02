if __name__ == "__main__":
    my_fav_food:set = set()
    # my_fav_food:list = []
    
    while True:
        user_data = input("what is your fav food : ")
        
        if "Nothing" == user_data:
            break
        
        my_fav_food.add(user_data)
        # my_fav_food.append(user_data)
    print(f"your fav food is : {", ".join(my_fav_food)}")