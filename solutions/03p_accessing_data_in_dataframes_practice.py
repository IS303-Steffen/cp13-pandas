from helper_functions import clear_screen
clear_screen()

# =======================================
# PRACTICE - ACCESSING DATA IN DATAFRAMES
# =======================================

# 1. PRACTICE
'''
Practice Problem: Managing a Classroom with Pandas

You are given a task to manage a classroom's score record using Pandas.
The class has 5 students and they have scores in three subjects:
Math, English, and Science. 
'''

students_dict = {
    "Names" : ["Frank", "Jacob", "James", "Alice", "Emily"],
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
# - Print the Math scores of all students.
# - Print the name and scores of all subjects of the third student.
print(df_students["Math"], "\n") # gets a specific column
print(df_students.iloc[2], "\n")


# PART 3:
# - Update the English score of the first student to 75.
# - Update the Science score of the last student to 85.

print(df_students.loc[0, "English"])
df_students.loc[0, "English"] = 75
print(df_students.loc[0, "English"])

# Science is the 4th column. Get the last row by doing -1. Or just put 4.
print(df_students.iloc[-1, 3])
df_students.iloc[-1, 3] = 85
print(df_students.iloc[-1, 3])

# PART 4:
# Add 10 to the Math scores of all students
df_students["Math"] += 10
print(df_students)

