from helper_functions import clear_screen
clear_screen()

# ==========================
# FILTERING USING CONDITIONS
# ==========================

'''
OVERVIEW
--------
You now know how to get access to parts of a DataFrame and change the data.
But what if you want to only get / change the data based on some condition,
like only those 20 years and older?

I will show 2 ways of doing this: 

1. .query()
    - You write a condition similar to an SQL query. The main disadvantage is
      that it isn't easy to change the data using this. It is an easy way to
      get the data though.

2. boolean indexing (with .loc)
    - This lets you specify specific rows to grab and makes it easy to alter
      the data in the same go. I think the syntax of this is more confusing,
      but being able to alter data makes it very useful.


OTHER WAYS I WILL NOT SHOW YOU
------------------------------
I will NOT show examples of the following. But here are short descriptions.
Feel free to look them up if they sound useful.

- .isin()
    - returns rows where a column's value matches a provided list of values.
- .between()
    - returns rows that are between 2 values (inclusive). Useful for numerical
      data
- .nlargest() and .nsmallest()
    - returns the smallest or largest n number of rows in a column you specify.
- .where() and .mask()
    - you specify a condition and it either keeps just those rows or everything
      except those rows. Similar to boolean indexing.
- .apply()
    - combine with boolean indexing to use custom functions in your filtering
- .filter()
    - allows you to specify rows or columns to select based on conditions of 
      the index or the column label, rather than the data itself.
'''

import pandas as pd

dancers_dict = {
    "Type" : ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
    "Dancer" : ["Jane", "Hadley", "Lyla", "London", "Zoey", "Millie", "Beck"],
    "Age" : [18, 23, 19, 20, 21, 22, 21]
}

df_dancers = pd.DataFrame(dancers_dict)
print(df_dancers, "\n")

# =======================
# FILTERING WITH .query()
# =======================

# 1. FILTER USING .query()
# Show all columns, but only for those age 21 and older. Use .query
print(df_dancers.query("Age > 21"), "\n")

# 2. FILTER USING .query(), SHOW A SINGLE COLUMN
# Show only 21 or older, but just show the Dancer column. Use .query.
# Just use brackets after the query method to get the "Dancer" column.
print(df_dancers.query("Age > 21")["Dancer"], '\n')

# 3. FILTER USING .query() WITH MULTIPLE CONDITIONS
# Show only 21 or older that have a dance Type of Jazz
print(df_dancers.query("Age > 21 and Type == 'Jazz'"), '\n')

# 4. CHANGE YOUR DATAFRAME WITH .query() BY USING inplace=True
# Print out your DataFrame. Then run a query to only retain those with an age
# over 21, but add the parameter inplace with True as the argument. Print out
# your DataFrame again. What happened?
print(df_dancers, '\n')
df_dancers.query("Age > 21", inplace=True)
print(df_dancers, '\n')

'''
DO I NEED TO USE inplace=True?
------------------------------
These 2 lines of code accomplish the same thing:

df_dancers = df_dancers.query("Type == 'Modern'")
df_dancers.query("Type == 'Modern'", inplace = True)
'''

