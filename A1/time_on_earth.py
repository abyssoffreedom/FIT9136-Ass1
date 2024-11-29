"""
This program converts seconds on earth into the form of 'seconds, minutes, hours'.
"""

print("TIME ON EARTH")
total_seconds = int(input("Input a time in seconds:\n"))
#The following steps calculate the total quantity of these units and their remainder after being converted. 
rem_seconds = total_seconds % 60
total_minutes = total_seconds // 60
rem_minutes = total_minutes % 60
total_hours = total_minutes // 60
print("\nThe time on Earth is", total_hours, "hours", rem_minutes, "minutes and", rem_seconds, "seconds.")
