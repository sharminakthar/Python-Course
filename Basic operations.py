import pandas as pd 

# Full dataframe
stats = pd.read_csv('C:\\Users\\GS769ZA\\OneDrive - EY\\Documents\\Python Udemy\\Section 4\\DemographicData.csv')
#print(stats)

#renaming columns
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']

#1st Operation = Subsetting
#stats.head()
#stats.tail()
#stats[:]
#stats[['..''..']][: ]

#Mathematical operations
#divison subtraction addition multiplication
result = stats.BirthRate * stats.InternetUsers
print(result.head())

#adds column called 'MyCalc' into dataframe
stats['MyCalc'] = stats.BirthRate * stats.InternetUsers 

#remove column
stats = stats.drop('MyCalc', 1)

#stats.drop('Column', axis = 0 or 1)