#import pandas and read csv file and store in the database
import pandas as pd
bankdata    =pd.read_csv("bank_list.csv")
print(bankdata.head())
print(bankdata.columns)
print(bankdata['ST'].nunique())#unique values from each column
print(bankdata['ST'].unique())#unique values from each column and representeed in array
#print most failed banks in states
print(bankdata.groupby('ST').count().sort_values('Bank Name', ascending=False).iloc[:5]['Bank Name'])
#top 5 acquiring institutions
print(bankdata['Acquiring Institution'].value_counts().iloc[:5])

#how  many banks has State  of Bank Texas acquire? and how many are in texas

print(bankdata[bankdata['Acquiring Institution']=='State Bank of Texas'])
#most common city in califormia to bank fail in
print(bankdata[bankdata['ST']=='CA'].groupby('City').count().sort_values('Bank Name',ascending=False).head(1))
