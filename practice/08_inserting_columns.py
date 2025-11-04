from helper_functions import clear_screen
clear_screen()

# ======================
# INSERTING AND DELETING
# ======================

'''
OVERVIEW
--------
You can add columns and rows, as well as delete columns and rows to a
DataFrame. In this file we just focus on adding columns.
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


# =================
# INSERTING COLUMNS
# =================

'''
.insert()
---------
.insert(location_index, "column label", data)

If data is a single value, it will apply to all rows.
If you provide a list or a DataFrame column, it needs to be the same length
as the DataFrame.
'''

# 1. INSERTING A NEW COLUMN
# Insert a new column in the first position called "test_column" with an empty
# string as the data


# 2. INSERTING A NEW COLUMN BASED ON EXISTING COLUMN
# Now make a column called "half_age" that is the
# original age column divided by 2 put it right after the original age column.


'''
If you want more info on inserting/deleting stuff in a dataframe, see the extra
file included in this repository on inserting/deleting.
'''