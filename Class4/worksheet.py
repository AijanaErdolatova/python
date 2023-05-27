message = "Welcome to the cinema,"
message += "\nplease enter you age: "


while True:
    try:
        age = int(input(message))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        continue

    if age < 13:
        print(f"Sorry you're not allowed to pass")

    elif age >=13 and age < 18:
        print(f"Please call your legal guardian")

    elif age >= 18:
        print(f"Welcome in never ending loop")

    else:
        print("Please, enter a valid number!")
        break
