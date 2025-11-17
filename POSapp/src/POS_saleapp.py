from src.util import show_message , get_operation_id

from src.operation import (
    add_prodct,
    product_list,
    create_voucher,
    sale_history
)


def main():
    show_message("Welcome to POS")
    
    while True:
        operation_id = get_operation_id()
        
        match operation_id:
            case "1":
                add_prodct()
            case "2":
                product_list()
            case "3":
                pass
            case "4":
                pass
            case _ :
                break
                
    show_message("Thank You!!!")
    

if __name__ == "__main__":
    main()