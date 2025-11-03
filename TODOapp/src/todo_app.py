from src.util import show_message , get_operation_id
from src.operation import show_all , create_task , find_task , delete_task

def main(): # user interface နဲ့ program flow ကို manage လုပ်ပေးတဲ့ function ဖြစ်ပါတယ်။
    show_message("TODO Application")
    
    while True:
        operation_id = get_operation_id()
        
        match operation_id :
            case "1":
                show_all()
            case "2":
                create_task()
            case "3" :
                find_task()
            case "4":
                delete_task()
            case _:
                break
            
    show_message("Thank You!!")
        
if __name__ == "__main__":
    main()
