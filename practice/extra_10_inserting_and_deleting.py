from helper_functions import clear_screen
clear_screen()

# ======================
# INSERTING AND DELETING
# ======================

'''
OVERVIEW
--------
You can add columns and rows, as well as delete columns and rows to a
DataFrame.
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


# ================
# DELETING COLUMNS
# ================

'''
del
---
You can use del to delete anything in python. Just do del and then a variable
name.
'''

# 3. DELETE A COLUMN USING DEL
# Delete the test_column using del. Print out the DataFrame afterwards.


'''
.drop()
-------
You can drop rows or columns. For columns, you need to specify axis=1

You can also choose whether to do the deletion in place or not. Also lets you
drop multiple columns at once.
'''

# 4. DELETE A COLUMN USING .drop()
# Use the .drop() method to drop the half_age column. Use axis=1
# Notice it returns a new DataFrame if you don't change the inplace parameter.


# =============
# DELETING ROWS
# =============

# 5. DELETE ROWS USING .drop()
# Provide a list of indices to .drop() to delete the 2 and 5th rows. The
# default value of axis is 0 (meaning rows) so you don't need to mention it.
# Try adding inplace=True to make it delete the rows in place.


# ===========
# ADDING ROWS
# ===========

# You might want to reimport the file again since we've been altering it:
df_mock_data = pd.read_excel(r"mock_sleeping_happiness_data.xlsx")

# creating a new DataFrame
df_new = pd.DataFrame({
    "first_name" : ["Jimmy", "John"],
    "last_name" : ["Simmy", "Song"],
    "age" : [20, 21], 
    "gender" : ["Male", "Female"],
    "hours_slept" : [8.0, 9.3],
    "happiness_rating": [87, 93]
})

'''
.concat()
---------
Use this to stick 2 or more DataFrames together. Just provide a list of
DataFrames as the first argument.

I also recommend using the ignore_index=True option, which will just start all
the indexes over from zero.
'''

# 6. ADD ROWS BY COMBINING DATAFRAMES WITH .concat()
# Use pd.concat() and provide a list of the original DataFrame and the new
# DataFrame. 


'''
ADDING ROWS WITH .loc[]
-----------------------
This works but you need to ensure the index you provide hasn't been used before
otherwise it will overwrite what is already there.

Provide a unique index, and then a list with a value for each column.
'''


# 7. ADD AN INDIVIDUAL ROW USING .loc[]
# Using the new_max_index above and the new_values, use .loc to add a new
# row to your DataFrame.

# new_max_index = combined_df.index.max() + 1
# new_values = ["George", "Harrison", 80, "Male", 8, 85]







