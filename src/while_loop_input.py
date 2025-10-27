ACTION_Name = {
    1 : "Show Student",
    2 : "Find ONE",
    3 : "Create Studen"
}


def start_app():
    while True:
        action_id = get_action()
        
        if action_id not in [1,2,3]:
            print("Invalid Action ID")
            break
        
        print(f"{action_id} : {ACTION_Name.get(action_id)}")
            

def get_action() -> int:
    print("Selection Action")
    for id in ACTION_Name.keys():
        print(f"{id} : {ACTION_Name.get(id)}")
    print()
    respond = input("Please Select the ID : ")
    return int(respond)

if __name__ == "__main__":
    start_app()
    