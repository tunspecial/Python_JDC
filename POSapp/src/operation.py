id = 0
datas:dict[int , dict[str , str] ] = {}

def operation(name:str):
    def decorator(func):# func parameter - decorate လုပ်မယ့် original function
        def warapper(*args , **kwargs): # Innder Function
            print(name)
            print("--------------------------------------------")
            func(*args, **kwargs) ##original function မှာ ရှိနိုင်တဲ့ arguments အားလုံးကို receive လုပ်တယ်
            print("--------------------------------------------")
        return warapper
    return decorator

def message(table:str):
    def decorator(func):
        def warraper(*args , **kwargs):
            print(table)
            print("-------------------------------")
            print("ID  Product           Price")
            print("-------------------------------")
            func(*args, **kwargs)
            print("-------------------------------")
        return warraper
    return decorator

@operation("1. Add Product")
def add_prodct():
    while True:
        product_name = input("Product Name   : ")
        product_price = input("Product Price  : ")
        if product_name == "" and product_price == "":
            print("Product Name and Price cannot be empty!\n")
        else:
            global id ## Global scope မှာရှိတဲ့ id variable ကို modify လုပ်ဖို့ declare လုပ်တယ်
            id += 1 
            datas[id] = {"name" : product_name , "price" : product_price}
            print(f"Product Name : {product_name} is create at ID : {id}")
            break

@message("2. Product List")
def product_list():
    if len(datas) > 0 :
        for key , product in datas.items():
            print(f"{key}.  {product["name"]:<18}{product["price"]}")
            
    else:
        print("There is No Product List")

@operation("3. Create Voucher")
def create_voucher():
    pass

@operation("4. Sale History")
def sale_history():
    pass