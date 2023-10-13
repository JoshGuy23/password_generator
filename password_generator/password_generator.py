import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_length = nr_letters + nr_symbols + nr_numbers
password = ""

for x in range(0, pass_length):
    char_choice = random.randint(1, 3) # Chooses a number from 1 to 3. Based on that number, a letter, symbol, or number is added respectively
    
    #If the chosen number is 1 and there are still letters left to choose, add a random letter. Otherwise, continue.
    if char_choice == 1 and nr_letters > 0:
        password += letters[random.randint(0, 51)]
        nr_letters -= 1
    else:
        char_choice = random.randint(2, 3)
        
    # If the chosen number is 2 and there are still symbols left to choose, add a random symbol.
    # Otherwise, randomly choose to add a letter or number. If letter, randomly choose a letter if one is still available.       
    if char_choice == 2 and nr_symbols > 0:
        password += symbols[random.randint(0, 8)]
        nr_symbols -= 1
    else:
        char_choice = random.randint(2, 3)
        if char_choice == 2 and nr_letters > 0:
            password += letters[random.randint(0, 51)]
            nr_letters -= 1
            
    # If the chosen number is 3 and there are still numbers left to choose, add a random number.
    # Otherwise, randomly choose to add a letter or symbol, if those are still available.
    if char_choice == 3 and nr_numbers > 0:
        password += numbers[random.randint(0, 9)]
        nr_numbers -= 1
    else:
        char_choice = random.randint(1, 2)
        if char_choice == 1 and nr_letters > 0:
            password += letters[random.randint(0, 51)]
            nr_letters -= 1
        else:
            char_choice = 2
            
        if char_choice == 2 and nr_symbols > 0:
            password += symbols[random.randint(0, 8)]
            nr_symbols -= 1
        else:
            if nr_letters > 0:
                password += letters[random.randint(0, 51)]
                nr_letters -= 1
            
print(f"Your password is: \n{password}")