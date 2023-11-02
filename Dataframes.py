import pandas as pd

# Exploring your data

#1. Full dataframe
stats = pd.read_csv('C:\\Users\\GS769ZA\\OneDrive - EY\\Documents\\Python Udemy\\Section 4\\DemographicData.csv')
#print(stats)

#2. Number of rows
print(len(stats))
#195 rows imported
#traceability & good for large files just to check

#3. See columns
print(stats.columns)
#Index(['Country Name', 'Country Code', 'Birth rate', 'Internet users', 'Income Group'], dtype='object')

#4. Number of columns
print(stats.columns)

#5. Prints 5 Top rows (or n rows in stats.head(n))
print(stats.head())

#6. Prints 5 Last rows (or n rows in stats.tail(n))
print(stats.tail())

#7. Information on the columns
print(stats.info)

#8. Get stats on the columns
print(stats.describe)
#tip: if its not easy to read, can flip x and y 
print(stats.describe.transpose())

#renaming columns
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']