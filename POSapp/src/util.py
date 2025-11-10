welcome_message = """=======================
{}
======================="""

def show_message(message:str):
    print(welcome_message.format(message))

    
selection_operation = """
Select Operation:
1. Add Product
2. Product List
3. Create Voucher
4. Sale History
"""

def get_operation_id() -> str:
    print(selection_operation)
    result = input("Select Operation ID : ")
    print()
    return result

