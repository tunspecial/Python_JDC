def do_job():
    done = 0
    while done < 5:
        done += 1
        result = input("please enter something : ")
        
        if result == "E":
            print(" Will Continus")
            continue
        
        if result == "Exit":
            break
        print(f"Your message is : {result}")
    else:
        print(f"Finish Successfully")
        
if __name__ == "__main__":
    do_job()
    