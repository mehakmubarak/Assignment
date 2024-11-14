def double_until_hundred():
    while True:
        try:
            curr_value = float(input("Please enter your own valid number: "))
            break  
        except ValueError:
            print("Please enter a valid number.")
    while curr_value < 100:
        curr_value = curr_value * 2  
        print(curr_value)  

double_until_hundred()





