from helper_functions import clear_screen
clear_screen()

# ===========================
# MATH FUNCTIONS AND GROUP BY
# ===========================

'''
OVERVIEW
--------
You can run some built-in math functions, to find the mean, max, etc.

You can combine this with the groupby function that functions similarly to
the GROUP BY statement in SQL.
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

'''
USEFUL MATH FUNCTIONS
---------------------
There are more than these, but some standard ones are:
    .mean()
    .median()
    .std
    .sum()
    .max()
    .min()
    .count()

'''

# 1. USE MATH FUNCTIONS ON A COLUMN
# Access the "hours_slept" column in the DataFrame and try adding one of the
# above listed functions to the end of it. Print out the result


# 2. USE MATH FUNCTIONS ON A WHOLE DATAFRAME
# Use one of the above listed functions on the whole DataFrame. Notice how it
# automatically only applies it to columns that it can run on.


'''
GROUP BY
--------
.groupby() lets you mimic the functionality of a GROUP BY statement in SQL
but with pandas. We won't use this much, so don't worry if it is confusing or
if you don't know SQL.

When using .groupby() you specify a column name. It will then create groups
for each unique value in that column. You can then add another column and a 
math function afterwards and it will calculate that function on each individual
group.

SYNTAX
------
df.groupby("column_name_to_group_on")["column_to_do_calculation_on"].math_function()

'''

# 3. USING GROUP BY TO PERFORM CALCULATIONS ON SUBSETS OF DATA
# Using the provided DataFrame, group by the "gender" column and calculate the
# mean hours_slept for Males and Females.

