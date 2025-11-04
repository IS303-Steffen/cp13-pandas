from helper_functions import clear_screen
clear_screen()

# ==========================
# LOOPING THROUGH DATAFRAMES
# ==========================

'''
OVERVIEW
--------
You can loop through columns and rows of a DataFrame. If you are looping so
that you can update a value in the DataFrame, I'd recommend just seeing if you
can use .iloc or .loc to update a value since that is more computationally 
efficient.
'''

import pandas as pd

dancers_dict = {
    "Type" : ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
    "Dancer" : ["Jane", "Hadley", "Lyla", "London", "Zoey", "Millie", "Beck"],
    "Age" : [18, 23, 19, 20, 21, 22, 21]
}

df_dancers = pd.DataFrame(dancers_dict)

# Reminder Hint:
example_string = "Strings are like lists of characters"
print(example_string[0])

# 1. PRACTICE
# Given the above DataFrame:
# - Loop through it, and add 3 to the age of every dancer who's first name
#   starts with "L". 
# HINT: When you find a match (a dancer whose name starts with "L") use the 
# index of the loop you're on to edit the original DataFrame.


# using iterrows()
for index, row in df_dancers.iterrows():
    if row["Dancer"][0] == "L":
        df_dancers.iloc[index, 2] += 3
print(df_dancers)

# # not using iterrows()
for index, row in enumerate(df_dancers["Dancer"]):
    if row[0] == "L":
        df_dancers.loc[index, "Age"] += 3

print(df_dancers)

# alternate without doing a loop
df_dancers.loc[df_dancers["Dancer"].str[0] == "L", "Age"] += 3
