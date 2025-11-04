from helper_functions import clear_screen
clear_screen()

# =====================
# PANDAS AND DATAFRAMES
# =====================

'''
OVERVIEW
--------
The main point of using Pandas is to get access to a
data type (class) called a DataFrame, which is like a mini spreadsheet
with rows and columns.

STRUCTURE OF A DATAFRAME
------------------------
    - Rows and Columns
    - Rows have an "index" which is a unique identifier for rows.
        - By default the index just starts at 0, but you could change it to be
          anything you want, even strings.
    - Columns have "labels" which are just names for the columns.

WHY USE DATAFRAMES/PANDAS?
---------------------------
    - Makes it really easy to import from external sources of data like .csv
      files, excel, sql databases.
    - Also makes it easy to export to those sources.
    - Works well with existing Python data types like lists and dictionaries.
    - Makes it easy to deal with messy data, especially missing values.
    - A very computationally efficient way to filter and sort data.
'''
    
dancers_dict = {
    "Type" : ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
    "Dancer" : ["Jane", "Hadley", "Lyla", "London", "Zoey", "Millie", "Beck"],
    "Age" : [18, 23, 19, 20, 21, 22, 21]
}

# 1. IMPORT PANDAS
# Make sure to import pandas. Convention is to give pandas the alias "pd" but
# you can do whatever you want.
import pandas as pd

# 2. CREATE A DATAFRAME
# Using the provided dancer_dict, create a DataFrame object using
# pd.DataFrame(). Store the DataFrame in a new variable, and then print it out
df_dancers = pd.DataFrame(dancers_dict)
print(df_dancers)

'''
RULES FOR MAKING A DATAFRAME FROM A DICTIONARY:
-----------------------------------------------
- The keys become the column labels
- The values should be a list of data. Typically, you want each column to be
  of a single data type.
- The lists must be of the same length. If you need blank data, just use None
  as a value in one of the lists.
'''

# 3. SEE THE DATAFRAME'S INDEX AND LABELS
# Use .index and .columns to access row indexes and column labels
# To print them out nice, you can convert them to a list() first.

print("index:\n", list(df_dancers.index))
print("labels:\n", list(df_dancers.columns))

'''
CHANGING INDICES OR LABELS
--------------------------
This isn't something you'll need to do much in this class.
You can change indices all at once through .index or labels all at once
through .columns.

If you want to change just a single index or label, the .rename() method is an
easier way to do it.

'''
letters = ["A", "B", "C", "D", "F", "D", "E"]
# 4. CHANGE INDEX
# Use the provided letters list above and change the index to use the letters
# instead. Then print out the dataframe again.
df_dancers.index = letters
print(df_dancers)

labels = ["Dance_Type", "Dancer_Name", "Dancer_Age"]
# 5. CHANGE LABEL
# Use the provided labels list above and change the labels using .columns
# Then print out the DataFrame again.
df_dancers.columns = labels
print(df_dancers)


# 6. CHANGE A SINGLE COLUMN LABEL USING .rename()
# If you want to rename a single label (or index) it is easier to use .rename()
# Change the "Dancer_Name" label to "Name"
# using .rename(columns={"Dancer_Name": "Name"}, inplace=True)

df_dancers.rename(columns={"Dancer_Name":"Name"}, inplace=True)
print(df_dancers)