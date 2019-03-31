import pandas as pd

# constants for table headers
header1 = ['BRAND_ID', 'BRAND_NAME', 'BRAND_TYPE']
header2 = ['CUST_CODE', 'CUST_FNAME', 'CUST_LNAME', 'CUST_STREET', 'CUST_CITY', 'CUST_STATE', 'CUST_ZIP', 'CUST_BALANCE']
header3 = ['DEPT_NUM', 'DEPT_NAME', 'DEPT_MAIL_BOX', 'DEPT_PHONE', 'EMP_NUM']
header4 = ['EMP_NUM', 'EMP_FNAME', 'EMP_LNAME', 'EMP_EMAIL', 'EMP_PHONE', 'EMP_HIREDATE', 'EMP_TITLE', 'EMP_COMM', 'DEPT_NUM',
           'SUPV_EMP_NUM']
header5 = ['INV_NUM', 'INV_DATE', 'CUST_CODE', 'INV_TOTAL', 'EMPLOYEE_ID']
header6 = ['INV_NUM', 'LINE_NUM', 'PROD_SKU', 'LINE_QTY', 'LINE_PRICE']
header7 = ['PROD_SKU', 'PROD_DESCRIPT', 'PROD_TYPE', 'PROD_BASE', 'PROD_CATEGORY', 'PROD_PRICE', 'PROD_QOH', 'PROD_MIN',
           'BRAND_ID']
header8 = ['EMP_NUM', 'SAL_FROM', 'SAL_END', 'SAL_AMOUNT']
header9 = ['PROD_SKU', 'VEND_ID']
header10 = ['VEND_ID', 'VEND_NAME', 'VEND_STREET', 'VEND_CITY', 'VEND_STATE', 'VEND_ZIP']

# data sources
dataFrame1 = pd.read_csv('data/DataSet2.txt', sep='\t', header=0, engine='python')
dataFrame2 = pd.read_csv('data/DataSet3.txt', sep='\t', header=0, engine='python')
dataFrame3 = pd.read_csv('data/DataSet4.txt', sep='\t', header=0, engine='python')

# slicing data sources to 10 tables (df)
# df2 = dataFrame1[header2]
# df2.to_csv('data/table2_CUST.csv', index=False)

df5 = dataFrame1[header5]
df5.to_csv('data/table5_INV.csv', index=False)

df6 = dataFrame1[header6]
df6.to_csv('data/table6_LINE.csv', index=False)

df1 = dataFrame2[header1]
df1.to_csv('data/table1_BRAND.csv', index=False)

df7 = dataFrame2[header7]
df7.to_csv('data/table7_PROD.csv', index=False)

df9 = dataFrame2[header9]
df9.to_csv('data/table9_SUPP.csv', index=False)

df10 = dataFrame2[header10]
df10.to_csv('data/table10_VEND.csv', index=False)

df3 = dataFrame3[header3]
df3.to_csv('data/table3_DEPT.csv', index=False)

df4 = dataFrame3[header4]
df4.to_csv('data/table4_EMP.csv', index=False)

df8 = dataFrame3[header8]
df8.to_csv('data/table8_SAL.csv', index=False)
