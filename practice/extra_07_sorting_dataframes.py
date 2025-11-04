from helper_functions import clear_screen
clear_screen()

# ==================
# SORTING DATAFRAMES
# ==================

'''
OVERVIEW
--------
You can sort DataFrames in a similar way to lists. You can sort things in place
or just return a sorted copy.
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

# 1. SORT IN ASCENDING AND DESCENDING ORDER
# Print out mock sleeping data in ascending order by hours_slept using
# .sort_values() Then, print it out in descending order by setting "ascending"
# to False


'''
TIP
---
IF you only want to show a few of the first few rows of data, you can add
.head(<number of rows>) to the end of the DataFrame to only print X number
of rows.
'''

# 2. SORT INPLACE
# Sort the mock sleeping data by happiness_rating in descending order. But this
# time, add inplace=True so that it changes the original DataFrame. Print out
# the DataFrame afterwards.


# 3. SORT BY MULTIPLE COLUMNS
# You can provide sort_values with a list of column names, as well as the 
# ascending parameter a list of True or False values. Sort the mock sleeping
# data in descending order by gender, but ascending order by hours_slept

