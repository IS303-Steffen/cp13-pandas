from helper_functions import clear_screen
clear_screen()

# ============================
# ACCESSING DATA IN DATAFRAMES
# ============================

'''
OVERVIEW
--------
You can get access to data in a DataFrame in many ways. I will show you 3:

1. Direct column/row access (just using square brackets [])

2. .iloc (using integers for row/column locations)

3. .loc (using index and column labels)


OTHER WAYS I WILL NOT SHOW YOU
------------------------------
I will NOT show examples of the following. But here are short descriptions.
Feel free to look them up if they sound useful.

- .iat
    - Same as .iloc but can only get a single value. The advantage is it is
    faster at getting a single value.
- .at
    - Same as .loc but can only get a single value. The advantage is it is
    faster at getting a single value.
- .get()
    - If it can't find the data, returns a default value
'''

import pandas as pd

dancers_dict = {
    "Type" : ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
    "Dancer" : ["Jane", "Hadley", "Lyla", "London", "Zoey", "Millie", "Beck"],
    "Age" : [18, 23, 19, 20, 21, 22, 21]
}

df_dancers = pd.DataFrame(dancers_dict)
print(df_dancers, "\n")

# =============
# DIRECT ACCESS
# =============

# 1. ACCESS A SPECIFIC COLUMN
# You can access a specific column by giving its name in square brackets.
# Try printing out just the "Dancer" column


'''
WHY DID IT PRINT WEIRD WHEN THERE WAS ONLY ONE COLUMN?
------------------------------------------------------
When you only access a single column (or single row) in a DataFrame, it
actually gives you a different data type, called a Series (which is basically
just a one-dimensional DataFrame). 

It shows the name of the Series, and then its data type. By default, strings
are stored as "object" datatypes.
'''

# 2. UPDATE A COLUMN'S VALUES
# One big advantages of DataFrames is you can change multiple pieces of data
# without looping. It is faster to write and faster for your computer to run.
# Add 1 to the age of everyone in the DataFrame. Print out the DataFrame to
# see if you did it correctly.


# 3. ACCESS MULTIPLE COLUMNS
# You can access multiple columns by giving a list inside the square brackets
# Note, that means two square brackets on each side. Try printing out the
# "Dancer" and "Age" columns in one print statement.


# =============
# USING .iloc[]
# =============

# 4. ACCESS A SPECIFIC ROW WITH .iloc
# .iloc gets rows based on their integer index location. Note that you use
# square brackets with .iloc instead of parentheses, like .iloc[0]. Get the 3rd
# row and print it out.


# 5. ACCESS A SPECIFIC ROW AND COLUMN WITH .iloc
# After you specify a row location, you can specify a column location


# 6. ACCESS THE LAST ROW WITH .iloc
# You can access the last element by using -1, second to last using -2, etc.
# Try printing everything from the last row of the dataframe:


# 7. CHANGE DATA USING .iloc
# Try to change the age of the 3rd row, 3rd column to 30 using .iloc. Print out
# the dataframe again to see if your change occured.



'''
GETTING MULTIPLE ROWS/COLUMNS
-----------------------------
You can access multiple rows or columns using a colon : to specify a starting
and stopping index. It will grab everything at the starting, but stop before
the stopping index. For example: [1:4]

You can also provide a list with indices separated by commas if you want some
rows or columns that aren't right next to each other.
For example: [1, 3]
'''

# 8: GETTING A SUBSET OF THE DATA WITH .iloc
# Get the first 3 rows, and then the 1st and 3rd columns


# ============
# USING .loc[]
# ============

'''
.iloc vs .loc
-------------
Now we'll switch to using .loc. The main difference it it uses the LABELS for
indexes and columns instead of integer index locations. 

This can be confusing because by default, the index is named the same thing.
There are other advantages to using .loc
'''

# 9. ACCESS A SPECIFIC ROW WITH .loc
# Use .loc to print out the 3rd row


# 10. ACCESS A SPECIFIC ROW AND COLUMN WITH .loc
# Get the age of the person in the 3rd row with .loc


# 11. ACCESS MULTPLE ROWS AND COLUMNS WITH .loc
# You can access multiple rows or columns using a colon : to specify a starting
# row/column, and then an ending row/column. But notice that it is inclusive,
# and grabs the start and stopping element. Print out the 3rd to the 5th row
# with just the Dancer and Age columns


# 12. CHANGE DATA USING .loc
# Add " Smith" to the existing data in the "Dancer" column for the 3rd and 
# 6th rows. Using += will be useful here. Print out the DataFrame again to 
# make sure your change worked.
