from helper_functions import clear_screen
clear_screen()

# =================
# LIST TO DATAFRAME
# =================

'''
OVERVIEW
--------
These are a few examples of putting lists into a DataFrame. I don't cover it
in class since using dictionaries is easier since that more elegantly handles
column lables. You'll have to manually add column labels afterwards if you use
lists.
'''

import pandas as pd 

# list of dances
dances_list = ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"]

# 1. CREATE A DATAFRAME FROM A LIST
# Use the list provided above to make a DataFrame. Print it out afterwards.


# Another list of data
names_dances_list = [
    ["Ballet","Jane"],
    ["Jazz", "Hadley"],
    ["Modern", "Lyla"],
    ["Tap", "London"],
    ["Tango", "Zoey"],
    ["Square", "Millie"],
    ["Hip-Hop", "Beck"]
]

# 2. CREATE A DATAFRAME FROM A LIST
# Create another DataFrame and print it out using the above list.


# 3. RENAME THE COLUMNS
# if you wanted to rename the columns, you can change the .columns attribute of
# the dataframe give it a list of column titles, like "Dancer Type"
# and "Dancer Name"
column_labels = ["Dance Type", "Dancer Name"]


