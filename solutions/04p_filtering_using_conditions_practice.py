from helper_functions import clear_screen
clear_screen()

# =======================================
# PRACTICE - ACCESSING DATA IN DATAFRAMES
# =======================================

students_dict = {
    "Name" : ["Frank", "Jacob", "James", "Alice", "Emily"],
    "Math" : [45, 56, 78, 88, 99],
    "English" : [90, 87, 99, 99, 23],
    "Science" : [12, 56, 98, 44, 55]
}

# PART 1:
# Convert the dictionary to a Pandas DataFrame and print it out.
import pandas as pd
df_students = pd.DataFrame(students_dict)
print(df_students)


# PART 2: 
# - print all data but for only those that have a Math score over 85
# - do the same as above, but only show the names of the students.

print()
print(df_students.query("Math > 85"))
print()
print(df_students.query("Math > 85")["Name"])

# PART 3: 
# - Show all columns for all students that got an 85 or above in 
#   English, but also got a 50 or below in Science
print()
print(df_students.query("English > 85 and Science <= 50"))
