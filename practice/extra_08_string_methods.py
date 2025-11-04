from helper_functions import clear_screen
clear_screen()

# ================
# STRING FUNCTIONS
# ================

'''
OVERVIEW
--------
Use .str to treat a column as a string. Then you can apply any string methods
you already know to it.
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

# 1. APPLY STRING FUNCTIONS TO A COLUMN
# Make the "last_name" column all uppercase. Use .str after getting a column
# to treat it like a string. Then add the string methods, like str.upper()



'''
.split()
--------
Remember .split() from your first project? Pandas has its own version of split
that works on columns. After accessing a column, add

.str.split("character to split by", expand = True)

expand makes it so it separates out what you split into separate columns in a
new dataframe
'''
# 2. SPLIT A COLUMN
# Use the split() method on the "gender" column. Split it using "a" as the
# character you split by. Use expand=True so that it gives you a new DataFrame.
# Print out the new DataFrame




