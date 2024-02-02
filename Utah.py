def test_func():
    print("Hello, World!")

import pandas as pd
HPI_monthly_file_path = 'HPI_PO_monthly_hist.xls'
df_HPI = pd.read_excel(HPI_monthly_file_path)
print(df_HPI.head())

#test test test 