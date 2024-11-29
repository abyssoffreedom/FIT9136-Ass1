"""
This program checks whether the input name is included in the usernameslist.
"""

usernames = ["Ava", "Leo", "Raj", "Zoe", "Max", "Sam", "Eli", "Mia", "Ian", "Kim"]
#Use a while loop to repeatedly ask inputting username.
while True:
    name = input("Enter username: ")
#The following steps show the condition which breaks the while loop
#The next line checks if the input value is included in the usernameslist 
    if name in usernames:
        print("Login successful. Welcome", name, "!")
#Use "break" keyword to terminate the loop
        break
    else:
        print("Login incorrect.")
