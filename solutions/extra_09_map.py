from helper_functions import clear_screen
clear_screen()

# ===
# MAP
# ===

'''
OVERVIEW
--------
One cool way to update column values is using .map

.map and .apply are really cool functions that can change any data using
custom functions and specifications

We don't have time to dive into it, but I do want to show you using .map with
a dictionary
'''

import pandas as pd

'''
IF THE NEXT LINE DOESN'T WORK ON YOUR COMPUTER:
-----------------------------------------------
You need to adjust the file path. Right click the
mock_sleeping_happiness_data.xlsx file and get the relative file path,
then paste it into the function below:
'''
df_mock_data = pd.read_excel(r"mock_sleeping_happiness_data.xlsx")
print(df_mock_data, '\n')


gender_dict = {"Male" : "M", "Female" : "F"}

# 1. UPDATE EXISTING VALUES USING A DICTIONARY
# Update the value of the "gender" column so that instead of "Male" and
# "Female" it shows "M" and "F". Use .map on the "gender" column and use the
# gender_dict as an argument
df_mock_data["gender"] = df_mock_data["gender"].map(gender_dict)
print(df_mock_data)
