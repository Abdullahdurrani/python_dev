# Create a class that can be called to fix the formatting of the csv in this dir (sample.csv) and return it as a df. 
# BONUS: Return the data grouped in the best manner you see fit.

import pandas as pd
import numpy as np

class CSVFormatter:
    def __init__(self, filename, schema):
        self.filename = filename
        self.schema = schema

    def fix_formatting(self):
        try:
            df = pd.read_csv(self.filename)
            df = df.replace('[\$,]', '', regex=True)
            df = df.replace(r'^\s*$', np.nan, regex=True).astype(self.schema)
            return df
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
    def group_data(self, df, grouping_cols):
        try:
            grouped_df = df.groupby(grouping_cols).sum(numeric_only=True).reset_index()
            return grouped_df
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

if __name__ == "__main__":
    schema = {
            'Master': int,
            'ID': int,
            'Revenue': float,
            'Profit': float,
            'Cost': float,
            'Expense': float,
            'Income': float,
            'Price': float,
            'Salary': float,
            'Investment': float
        }
    csv_formatter = CSVFormatter(r"C:\Desktop\python_dev\sample.csv", schema)
    formatted_df = csv_formatter.fix_formatting()

    if formatted_df is not None:
        print("Formatted DataFrame:")
        print(formatted_df)
        
        grouping_cols = ['Master', 'ID']
        grouped_data = csv_formatter.group_data(formatted_df, grouping_cols)
        print("\nGrouped Data:")
        print(grouped_data)