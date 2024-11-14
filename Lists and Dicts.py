def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."
def index_game():
    lst = [1, 2, 3, 4, 5] 
    print("Current list:", lst)
    print("Choose an operation:")
    print("1. Access element")
    print("2. Modify element")
    print("3. Slice list")
    print(f"Hey Dear!!")
    operation = input("Enter operation (1/2/3): ")

    if operation == "1":
        index = int(input("Enter index to access: "))
        print("Accessed element:", access_element(lst, index))
    elif operation == "2":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print("Modified list:", modify_element(lst, index, new_value))
    elif operation == "3":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print("Sliced list:", slice_list(lst, start, end))
        print(f"thank you ")
    else:
        print("Invalid operation.")
index_game()

