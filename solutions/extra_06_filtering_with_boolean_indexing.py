from helper_functions import clear_screen
clear_screen()

# ============================
# BOOLEAN INDEXING WITH .loc[]
# ============================

'''
OVERVIEW
--------
This is another way to filter. The primary advantage is that you can filter
down to something and then change it all in one go. The syntax, however,
is more complex.

'''

import pandas as pd

dancers_dict = {
    "Type" : ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
    "Dancer" : ["Jane", "Hadley", "Lyla", "London", "Zoey", "Millie", "Beck"],
    "Age" : [18, 23, 19, 20, 21, 22, 21]
}

df_dancers = pd.DataFrame(dancers_dict)
print(df_dancers, "\n")

# ============================
# BOOLEAN INDEXING WITH .loc[]
# ============================

'''
Boolean indexing just means you are getting the indexes with a True or False
value attached to them. 

I personally think this is uglier, but also much more useful because you can
change the values that you get. .query() only lets you get the values.
'''

# recreating the DataFrame just in case the previous code messes it up.
df_dancers = pd.DataFrame(dancers_dict)
print(df_dancers, "\n")

# 5. PRINT OUT BOOLEAN INDEX RESULTS OF A CONDITION
# Print out this piece of code: df_dancers["Age"] > 21
# What is it giving you? Why is this useful?

print(df_dancers["Age"] > 21, '\n')

# 6. FILTER USING BOOLEAN INDEXING WITH .loc[]
# Use .loc[] but inside the brackets, put df_dancers["Age"] > 21. That will
# provide the specific rows to keep and which to get rid of.
print(df_dancers.loc[df_dancers["Age"] > 21], '\n')

# 7. FILTER USING BOOLEAN INDEXING, SHOW A SINGLE COLUMN
# Do the same thing as above, but only show the Age column
print(df_dancers.loc[df_dancers["Age"] > 21, "Age"])

# 8 UPDATE VALUES BASED ON BOOLEAN INDEXING FILTERING
# This is the main advantage of boolean indexing over .query.
# Add 3 to the age of any dancer that is exactly 21 years old. Print out the
# DataFrame to make sure your changes happened.
df_dancers.loc[df_dancers["Age"] == 21, "Age"] += 3
print(df_dancers, '\n')


'''
MULTIPLE CONDITIONS WITH BOOLEAN INDEXING
-----------------------------------------
To add multiple logical conditions, you need to:
    1. put each condition in parentheses
    2. Use panda's version of operators:
        - and: &
        - or:  |
        - not: ~

    e.g. df.loc[(df["Column"] == "X") & (df["Column2"] < 10)]
'''

# 9. FILTER USING MULTIPLE CONDITIONS
# Print out dancers under 22 or any that dance the Tango
print(df_dancers.loc[(df_dancers["Age"] < 22) | (df_dancers["Type"] == "Tango")], '\n')

# 10. FILTER USING MULTIPLE CONDITIONS
# Do the same thing, but only print out the Dancer name.
print(df_dancers.loc[ (df_dancers["Age"] < 22) 
                    | (df_dancers["Type"] == "Tango"), "Dancer"], '\n')

# 11. UPDATE VALUES BASED ON FILTER
# Using the same filter as above, add an asterisk * to the end of Dancer names
# that match the filter. Print out your DataFrame again to make sure the change
# was successful.
df_dancers.loc[ (df_dancers["Age"] < 22)
              | (df_dancers["Type"] == "Tango"), "Dancer"] += '*'

print(df_dancers)

'''
TIP
---
Remember that what you are doing here is one of the main advantages of using
pandas over other data types / importing Excel files with openpyxl. You can
make changes to entire columns / subsections without using loops. It is very
computationally efficient. Plus, it is fewer lines of code.
'''
