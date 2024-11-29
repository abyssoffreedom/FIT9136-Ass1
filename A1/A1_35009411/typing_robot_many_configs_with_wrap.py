"""
This program asks for an input and then display the minimal actions that a robot takes to print this input.
"""

keyboard0 = ["abcdefghijklm",
             "nopqrstuvwxyz"]
keyboard1 = ["789",
             "456",
             "123",
             "0.-"]
keyboard2 = ["chunk",
             "vibex",
             "gymps",
             "fjord",
             "waltz"]
keyboard3 = ["bemix",
             "vozhd",
             "grypt",
             "clunk",
             "waqfs"]
keyboards_list = [keyboard0, keyboard1, keyboard2, keyboard3]

#This function is used to locate a char's position on a certain keyboard
def position(char, keyboard):
    for string in keyboard:
        if char in string:
            return [keyboard.index(string), string.index(char)]
    return False

#This function returns the operations the robot takes on a certain keyboard to type a string, and collects these results in a list
def instruct_robot(string):
#Use this list to collect every required operations to type a certain string on each keyboard
    results_list = []
#To traverse every keyboard
    for keyboard in keyboards_list:
        cur_position = [0, 0]
#Record every required operations as a list in the form of [index of the keyboard, required operations]
        result_list = [keyboards_list.index(keyboard)]
        operation_string = ""
#To traverse every char in a certain string, this line must be combined with line 34
        for char in string:
#Attention! In this condition, a char in the string cannot be found on a keyboard
#leading to the whole string cannot be typed on this keyboard
            if position(char, keyboard) == False:
                operation_string = None
#This break is extremely important to end the for char in string Loop
#It can prevent the robot to type other chars in this string which can be found in this keyboard
                break
            else:
                pre_position = cur_position
                cur_position = position(char, keyboard)
#The below distance does not include the wrap
                position_distance = [cur_position[0] - pre_position[0], cur_position[1] - pre_position[1]]
                if position_distance[1] >= 0 and position_distance[0] <= 0:
#len(keyboard[0]) - position_distance[1] represents the horizontal distance by wrapping
#position_distance[1] represents the horizontal distance without wrapping
#The same as the vertical distance
                    if len(keyboard[0]) - position_distance[1] <= position_distance[1] and len(keyboard) + position_distance[0] <= -position_distance[0]:
                        operation_string += "l" * (pre_position[1] + 1) + "w" + "l" * (len(keyboard[0]) - cur_position[1] - 1) + "d" * (len(keyboard) - pre_position[0]) + "w" + "d" * cur_position[0] + "p"
                    elif len(keyboard[0]) - position_distance[1] <= position_distance[1]:
                        operation_string += "l" * (pre_position[1] + 1) + "w" + "l" * (len(keyboard[0]) - cur_position[1] - 1) + "u" * (0 - position_distance[0]) + "p"
                    elif len(keyboard) + position_distance[0] <= -position_distance[0]:
                        operation_string += "r" * position_distance[1] + "d" * (len(keyboard) - pre_position[0]) + "w" + "d" * cur_position[0] + "p"
                    else:
                        operation_string += "r" * position_distance[1] + "u" * (0 - position_distance[0]) + "p"
                elif position_distance[1] >= 0:
                    if len(keyboard[0]) - position_distance[1] <= position_distance[1] and len(keyboard) - position_distance[0] <= position_distance[0]:
                        operation_string += "l" * (pre_position[1] + 1) + "w" + "l" * (len(keyboard[0]) - cur_position[1] - 1) + "u" * (pre_position[0] + 1) + "w" + "u" * (len(keyboard) - cur_position[0] - 1) + "p"
                    elif len(keyboard[0]) -position_distance[1] <= position_distance[1]:
                        operation_string += "l" * (pre_position[1] + 1) + "w" + "l" * (len(keyboard[0]) - cur_position[1] - 1) + "d" * position_distance[0] + "p"
                    elif len(keyboard) - position_distance[0] <= position_distance[0]:
                        operation_string += "r" * position_distance[1] + "u" * (pre_position[0] + 1) + "w" + "u" * (len(keyboard) - cur_position[0] - 1) + "p"
                    else:
                        operation_string += "r" * position_distance[1] + "d" * position_distance[0] + "p"
                elif position_distance[0] <= 0:
                    if len(keyboard[0]) + position_distance[1] <= -position_distance[1] and len(keyboard) + position_distance[0] <= -position_distance[0]:
                        operation_string += "r" * (len(keyboard[0]) - pre_position[1]) + "w" + "r" * cur_position[1] + "d" * (len(keyboard) - pre_position[0]) + "w" + "d" * cur_position[0] + "p"
                    elif len(keyboard[0]) + position_distance[1] <= -position_distance[1]:
                        operation_string += "r" * (len(keyboard[0]) - pre_position[1]) + "w" + "r" * cur_position[1] + "u" * (0 - position_distance[0]) + "p"
                    elif len(keyboard) + position_distance[0] <= -position_distance[0]:
                        operation_string += "l" * (0 - position_distance[1]) + "d" * (len(keyboard) - pre_position[0]) + "w" + "d" * cur_position[0] + "p"
                    else:
                        operation_string += "l" * (0 - position_distance[1]) + "u" * (0 - position_distance[0]) + "p"
                else:
                    if len(keyboard[0]) + position_distance[1] <= -position_distance[1] and len(keyboard) - position_distance[0] <= position_distance[0]:
                        operation_string += "r" * (len(keyboard[0]) - pre_position[1]) + "w" + "r" * cur_position[1] + "u" * (pre_position[0] + 1) + "w" + "u" * (len(keyboard) - cur_position[0] - 1) + "p"
                    elif len(keyboard[0]) + position_distance[1] <= -position_distance[1]:
                        operation_string += "r" * (len(keyboard[0]) - pre_position[1]) + "w" + "r" * cur_position[1] + "d" * position_distance[0] + "p"
                    elif len(keyboard) - position_distance[0] <= position_distance[0]:
                        operation_string += "l" * (0 - position_distance[1]) + "u" * (pre_position[0] + 1) + "w" + "u" * (len(keyboard) - cur_position[0] - 1) + "p"
                    else:
                        operation_string += "l" * (0 - position_distance[1]) + "d" * position_distance[0] + "p"
#We check this string on every keyboard and add the result into the list
        results_list.append([keyboards_list.index(keyboard), operation_string])
    return results_list

#This function is used to delete element in the results_list which has no operations
#meaning that this string cannot be typed on this keyboard
def list_after_delete(string):
    new_results_list = instruct_robot(string)
    for result_list in instruct_robot(string):
        if result_list[1] == None:
            new_results_list.remove(result_list)
    return new_results_list

def output(string):
#If every list has no operations, this string cannot be typed on any keyboard
    if len(list_after_delete(string)) == 0:
        print("The string cannot be typed out.")
    else:
#The following steps calculate the minimal moves taken to type this string
#And record the corresponding index of keyboard and operations
#The minimal moves must exclude the "w", because "w" is not considered as a separate operation!!!
        min_moves = len(list_after_delete(string)[0][1]) - list_after_delete(string)[0][1].count("w")
#Initialised as a list so that it can be mutated during the for loop
#And pass the value outside the loop
        index_keyboard = [list_after_delete(string)[0][0]]
        to_print_operations = [list_after_delete(string)[0][1]]
        for result_list in list_after_delete(string):
            if len(result_list[1]) - result_list[1].count("w")< min_moves:
                min_moves = len(result_list[1]) - result_list[1].count("w")
                index_keyboard[0] = result_list[0]
                to_print_operations[0] = result_list[1]
#Decompose the diagram into three parts, up, mid, and bottom
#Use a loop to print the mid part  
        print("Configuration used:")
        print("-" * (len(keyboards_list[index_keyboard[0]][0]) + 4))
        for i in range(len(keyboards_list[index_keyboard[0]])):
            print("|", keyboards_list[index_keyboard[0]][i], "|")
        print("-" * (len(keyboards_list[index_keyboard[0]][0]) + 4))
        print("The robot must perform the following operations:")
        print(to_print_operations[0])

output(input("Enter a string to type: "))
