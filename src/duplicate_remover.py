import pandas as pd
import os

'''
This file aims to remove rows with identical value for all columns
'''

# input file path
input_path = 'data/tables-raw'

# output file path
output_path = 'data/tables-deduplicated/'

input_directory = os.fsencode(input_path)
for file in os.listdir(input_directory):
    file_name = os.fsdecode(file)
    if file_name.endswith('.csv'):
        # print(file_name)
        df = pd.read_csv(os.path.join(input_path, file_name), header=0)
        df = df.drop_duplicates()
        df.to_csv(output_path + file_name, index=False)
