ACTION_NAME = {
    1 : "Show Student",
    2 : "Find One",
    3 : "Create Student"
}

if __name__ == "__main__":
    print("==========================")
    print("WELL COME TO OUR PROGRAM")
    print("==========================")
    print()
    
    while True:
        for id in ACTION_NAME.keys():
            print(f"{id} : {ACTION_NAME.get(id)}")
            
        print()
        
        respond = input("Please Select Action ID : ")
        action_id = int(respond)
        
        if action_id not in [1,2,3]:
            print("Invalid Action ID")
            break
        
        print(f"You Selected {action_id} : {ACTION_NAME.get(action_id)}")            
        