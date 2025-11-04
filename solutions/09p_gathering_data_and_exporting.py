from helper_functions import clear_screen
clear_screen()

# ============================
# GATHERING DATA AND EXPORTING
# ============================

'''
OVERVIEW
--------
One way to can export data from python to a Pandas dataframe is to give Pandas
a list of dictionaries.

Instructions:

1. Create an empty list called "students" that will eventually hold multple 
   dictionaries with student data inside

2. Use a while loop to repeatedly:
   - Ask the user to enter a student's name.
   - Ask the user to enter that student's GPA.
   - Create a dictionary with two keys: "name" and "gpa".
   - Append this dictionary to the "students" list.

3. After adding a student, ask:
   "Add another student? (y/n)"
   - If the user enters "y", continue the loop.
   - If the user enters "n", end the loop.

4. When the loop ends:
   - Convert the list of dictionaries into a pandas DataFrame.
   - Export the DataFrame to an Excel file named
     "student_grades.xlsx" using df.to_excel().
   - Do not include the index column in the Excel file.

5. Test your program by running it and entering several students.
   Then open the Excel file to confirm that the data was saved.
'''
# Put code here

import pandas as pd

# list to hold each student's data
students = []

while True:
    name = input("Enter student's name: ").strip()
    gpa = input(f"Enter {name}'s GPA: ").strip()

    # store the data as a dictionary
    students.append({
        "name": name,
        "gpa": float(gpa)  # convert to number
    })

    # ask if user wants to continue
    another = input("Add another student? (y/n): ").strip().lower()             
    if another != "y":
        break

# create DataFrame from list of dictionaries
df = pd.DataFrame(students)

# show the data
print("\nCollected data:")
print(df)

# export to Excel
df.to_excel("student_grades.xlsx", index=False)

print("\nData saved to 'student_grades.xlsx'")

'''
EXTRA THOUGHT:
--------------
If you wanted to expand the functionality, you could make it keep adding to the
Excel file by trying to open an existing excel file, and then combining it with
the new pandas dataframe you create. 
'''