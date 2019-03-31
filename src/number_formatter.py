import pandas as pd
import numpy as np
import os

'''
This file aims to clean columns with number format
'''

# table-wise dictionary for number format columns
number_cols_dict = {
    'table1': ['BRAND_ID'],
    'table2': ['CUST_CODE', 'CUST_BALANCE'],
    'table3': ['DEPT_NUM', 'EMP_NUM'],
    'table4': ['EMP_NUM', 'EMP_COMM', 'DEPT_NUM', 'SUPV_EMP_NUM'],
    'table5': ['INV_NUM', 'CUST_CODE', 'INV_TOTAL', 'EMPLOYEE_ID'],
    'table6': ['INV_NUM', 'LINE_NUM', 'LINE_QTY', 'LINE_PRICE'],
    'table7': ['PROD_PRICE', 'PROD_QOH', 'PROD_MIN', 'BRAND_ID'],
    'table8': ['EMP_NUM', 'SAL_AMOUNT'],
    'table9': ['VEND_ID'],
    'table10': ['VEND_ID']
}

decimal_cols = ['CUST_BALANCE', 'EMP_COMM', 'INV_TOTAL', 'LINE_PRICE', 'PROD_PRICE', 'PROD_QOH', 'PROD_MIN', 'SAL_AMOUNT']

# input file path
input_path = 'data/tables-deduplicated'

# output file path
output_path = 'data/tables-deduplicated-number/'

input_directory = os.fsencode(input_path)
for file in os.listdir(input_directory):
    file_name = os.fsdecode(file)
    if file_name.endswith('.csv'):
        # print(file_name)
        df = pd.read_csv(os.path.join(input_path, file_name), header=0)
        file_prefix = file_name.split('_')[0]
        if file_prefix in number_cols_dict:
            for number_col in number_cols_dict[file_prefix]:
                if number_col in decimal_cols:
                    df[number_col] = df[number_col].astype(str).str.extract(r'(\d+\.?\d*)').astype(np.float)
                else:
                    df[number_col] = df[number_col].astype(str).str.extract(r'(\d+)').astype(int)
            df.to_csv(output_path + file_name, index=False)
