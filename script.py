
import re
import pandas as pd 

# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("filename.csv") 

#Select duplicate rows except first occurrence based on all columns
duplicateRowsDF = data[data.duplicated()]
 
print("Duplicate Rows except first occurrence based on all columns are :")
print(duplicateRowsDF)

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

for index, row in df.iterrows():
    if not EMAIL_REGEX.match(row):
        print(row)
    else:
        s = 'My name is Conrad, and blahblah@gmail.com is my email.'
        domain = re.search("@[\w.]+", s)
        print domain.group()
      
      
