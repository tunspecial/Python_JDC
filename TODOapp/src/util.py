## {} က placeholder ဖြစ်ပြီး နောက်ပိုင်းမှာ format() method နဲ့ message တစ်ခုကို ထည့်သုံးမှာဖြစ်တယ်

titel = """
========================
{} 
========================
"""

def show_message(message:str):
    print(titel.format(message))
    
operation = """
Select Operation
1. Show Tasks
2. Create Task
3. Find Tasks
4. Delete Task
"""

def get_operation_id() -> str:
    print(operation)
    result = input("Select ID : ")
    print()
    return result



