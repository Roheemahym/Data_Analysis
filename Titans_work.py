import pandas as pd

# Read from CSV & Excel Files
df_for_csv_original = pd.read_csv(r"c:\Users\USER\Downloads\student_performance_data.csv")
df_for_excel_original = pd.read_excel(r"c:\Users\USER\Downloads\Python_excel.xlsx")

# Copied the original data into another variable
df_csv_copied = df_for_csv_original.copy() # the reason why it was not copied is so that the original data will remain untouched
# refer back to the original one
