import os
import pandas as pd

current_directory = os.path.dirname(os.path.realpath(__file__))

spreadsheet = pd.read_excel(os.path.join(current_directory, 'SpreadsheetName.xlsx'))

for index, row in spreadsheet.iterrows():
    original_name = row['Original Name'] ##Column with the original name
    new_name = row['Rename'] ##Column with the new Name

    original_path = os.path.join(current_directory, original_name)
    new_path = os.path.join(current_directory, new_name)

    if os.path.exists(original_path):
        os.rename(original_path, new_path)
        print(f"File {original_name} renamed to {new_name}")
    else:
        print(f"File {original_name} not found. Check the paths.")

print("Renaming completed.")
