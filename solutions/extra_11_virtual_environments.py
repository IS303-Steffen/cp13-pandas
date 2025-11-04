from helper_functions import clear_screen
clear_screen() # This just clears the terminal window each time we run code

# ==========================================
# EXTRA - PYTHON VIRTUAL ENVIRONMENTS (VENV)
# ==========================================

'''
OVERVIEW
--------
A virtual environment is like a clean, self-contained workspace for your Python
project. It includes a full copy of the Python interpreter and its own place to
install packages, so anything you add or change doesn’t affect other projects
or your system-wide Python. This isolation is especially useful when different
projects need different versions of the same package. It also makes your code
easier to share and reproduce, since you can list exactly what dependencies it
needs.

In short, virtual environments help keep projects organized,
conflict-free, and easier to manage.
'''

# 1. CREATE A VIRTUAL ENVIRONMENT USING VS CODE
'''
1: Press F1 (you might have to hold your computer's FN or Function key and
             then press F1)
2: A window will pop up (called the Command Palette). Type in "Python: Create
   Environment" and press enter or return
3: If it gives you a choice, choose "venv"
4: If it gives you a choice, choose which version of Python you want to
   use for your virtual environment
5: Exit out of any open terminal, and then open a new terminal window
6: Now you can just run pip and it will install any packages directly to that
   virtual environment
'''

import openpyxl
wb = openpyxl.Workbook()
wb.active["A1"] = "quick example"
wb.save("extra_01.xlsx")
wb.close()

'''
MAKING VENV THROUGH THE COMMAND LINE
------------------------------------

MAC/LINUX:
python3 -m venv env       # Create a virtual environment named 'env'
source env/bin/activate   # Activate the environment
deactivate                # Exit the environment

WINDOWS:
python -m venv env             # Create a virtual environment named 'env'
env\Scripts\activate           # Activate the environment
deactivate                     # Exit the environment
'''


