from helper_functions import clear_screen
clear_screen()

# =====================
# HANDLING MISSING DATA
# =====================

'''
OVERVIEW
--------
If you have missing data (shown below as None), Pandas will show that as
NaN, meaning "not a number". It is essentially the same a null or None value.

You can choose to replace missing data with a specific value. There are also
more complex options that what is shown here.
'''
import pandas as pd
    
dancers_dict =  {
    "Type" : [None, "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
    "Dancer" : ["Jane", None, "Lyla", "London", "Zoey", "Millie", "Beck"],
    "Age" : [18, 23, 19, "A", 21, 22, 21]
}

df_dancers = pd.DataFrame(dancers_dict)

# 1. FIND ALL MISSING DATA USING .isnull()
print(df_dancers.isnull())

# 2. REPLACE ANY NaN VALUE
# Use .fillna() to replace NaN values with a string that says "MISSING"
df_dancers.fillna("MISSING", inplace=True)
print(df_dancers)