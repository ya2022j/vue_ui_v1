import pandas as pd
xls = pd.ExcelFile(r"d.xlsx")
df = pd.DataFrame()
for name in xls.sheet_names:
    print(name)