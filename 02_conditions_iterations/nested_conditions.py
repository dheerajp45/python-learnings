age = int(input("Enter age: "))
has_id = input("Have ID? (yes/no): ")

if age >= 18:
    if has_id == "yes":
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Underage")