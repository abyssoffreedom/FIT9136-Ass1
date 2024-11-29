"""
This program ask for an input string, and then display the actions that a robot takes to print this input.
"""

your_variable_name = \
    ["abcdefghijklm",
     "nopqrstuvwxyz"]
#This function is used to find the row and column of a char in this keyboard
def position(char):
    for string in your_variable_name:
        if char in string:
            return [your_variable_name.index(string), string.index(char)]
    return False

def instruct_robot(string):
    cur_position = [0, 0]
    operation_string = ""

    for char in string:
#If any char in this string is not on the board, the whole string cannot be typed
        if position(char) == False:
#Return keyword will immediately terminate this function
            return "The string cannot be typed out."
        
        else:
#The following steps calculate the vertical and horizontal distances between two consecutive characters
            pre_position = cur_position
            cur_position = position(char)
            position_distance = [cur_position[0] - pre_position[0], cur_position[1] - pre_position[1]]
#Use relative distances to type char
            if position_distance[1] >= 0 and position_distance[0] <= 0:
                operation_string += "r" * position_distance[1] + "u" * (0 - position_distance[0]) + "p"
            elif position_distance[1] >= 0:
                operation_string += "r" * position_distance[1] + "d" * position_distance[0] + "p"
            elif position_distance[0] <= 0:
                operation_string += "l" * (0 - position_distance[1]) + "u" * (0 - position_distance[0]) + "p"
            else:
                operation_string += "l" * (0 - position_distance[1]) + "d" * position_distance[0] + "p"
    return "The robot must perform the following operations:\n" + operation_string

input_string = input("Enter a string to type: ")
print(instruct_robot(input_string))
