import os
import pandas as pd
import xlrd
#import openpyxl

# filter files for format  
file = [i for i in os.listdir(path=os.getcwd()) if i.endswith(('.xlsx', '.csv', '.xlsm', '.xltx', '.xltm'))][0]

# read file different by format
if file.endswith('.csv'):
    df = pd.read_csv(file)
else:
    df = pd.read_excel(file)


# get dictionary with Key(tiker) : Value[price]
data = df.groupby('ticker.keyword: Ascending')['Max price'].apply(list).to_dict()
