from helper_functions import clear_screen
clear_screen()

# ===============================
# CREATING PLOTS USING MATPLOTLIB
# ===============================

'''
OVERVIEW
--------
Creating graphs and plots is a rabbit hole that you could spend weeks on, and
we just don't have time for that in this course, but this file shows off a
simple example of what is possible. Look up more of what you can do with
matplotlib if this interests you.
'''

import matplotlib.pyplot as plot
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


# Create a subset of data that would make for an interesting graph:
result = df_mock_data.groupby("gender")["hours_slept"].mean()
print(result)

# basic idea is that you specify a chart type
# and tell it the axis
# do a bar graph with the x-axis as gender and the y-axis as average hours slept.
result.plot(kind='bar')
plot.title = "Average Hours slept by gender"
plot.xlabel("Gender")
plot.ylabel("Hours Slept")
plot.show()
