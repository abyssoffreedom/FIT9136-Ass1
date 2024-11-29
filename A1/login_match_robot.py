"""
Tis program checks if the input name and input password match a paired combination and if not then does a robot check.
""" 

usernames = ["Ava", "Leo", "Raj", "Zoe", "Max", "Sam", "Eli", "Mia", "Ian", "Kim"]
passwords = ["12345", "abcde", "pass1", "qwert", "aaaaa", "zzzzz", "11111", "apple", "hello", "admin"]
tries = 3
#The following steps make a list of lists in which usernames and passwords are atched and paired
pairs_list = []
for index in range(len(usernames)):
    pairs_list.append([usernames[index], passwords[index]])

while True:
    name = input("Enter username: ")
    password = input("Enter password: ")
#To list the input name and pair so that it can be compared with the element of the long list
    pair = [name, password]
    tries -= 1
#The program terminates upon a succesful login
    if pair in pairs_list:
        print("Login successful. Welcome", name, "!")
        break
    else:
        print("Login incorrect. Tries left:", tries)
#When 3 tries are used up it then will do the robot check
        if tries == 0:
            while True:
                robot_check = input("Are you a robot (Y/n)? ")
                if robot_check == "Y" or robot_check == "":
#Fail to pass the robot check and the program terminates
                    exit()
                elif robot_check == "n":
                    tries = 3
#This "break" keyword is used to terminate the second while True loop and back to the first one
                    break
            

        
