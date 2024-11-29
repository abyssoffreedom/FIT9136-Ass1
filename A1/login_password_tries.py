"""
Tis program checks if the input name and input password are included in usernameslist and passwordslist respectively.
"""

usernames = ["Ava", "Leo", "Raj", "Zoe", "Max", "Sam", "Eli", "Mia", "Ian", "Kim"]
passwords = ["12345", "abcde", "pass1", "qwert", "aaaaa", "zzzzz", "11111", "apple", "hello", "admin"]
tries = 3
#Use while loop to repeatedly ask for input Value
while True:
    name = input("Enter username: ")
    password = input("Enter password: ")
#After each iteration tries will minus one
    tries -= 1
#The loop terminates if both input values are correct
    if name in usernames and password in passwords:
        print("Login successful. Welcome", name, "!")
        break
#In other cases the program will print left tries and continue the loop
    else:
        print("Login incorrect. Tries left:", tries)
#But if 3 tries are used up, the loop terminates
        if tries == 0:
            break
