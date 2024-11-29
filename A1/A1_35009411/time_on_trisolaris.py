"""
This program calculates time conversion both on earth and on trisolaris.
"""

print("TIME ON EARTH")
total_seconds = int(input("Input a time in seconds:\n"))
#The following steps calculate on earth the total quantity of these units and their remainder after being converted. 
rem_seconds = total_seconds % 60
total_minutes = total_seconds // 60
rem_minutes = total_minutes % 60
total_hours = total_minutes // 60
print("\nThe time on Earth is", total_hours, "hours", rem_minutes, "minutes and", rem_seconds, "seconds.\n")

print("TIME ON TRISOLARIS")
sec_to_min = int(input("Input the number of seconds in a minute on Trisolaris:\n"))
min_to_hr = int(input("Input the number of minutes in an hour on Trisolaris:\n"))
#The following steps calculate on trisolaris the total quantity of these units and their remainder after being converted. 
new_rem_seconds = total_seconds % sec_to_min
new_total_minutes = total_seconds // sec_to_min
new_rem_minutes = new_total_minutes % min_to_hr
new_total_hours = new_total_minutes // min_to_hr
print("\nThe time on Trisolaris is", new_total_hours, "hours", new_rem_minutes, "minutes and", new_rem_seconds, "seconds.")
