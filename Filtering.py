import pandas as pd 

# Full dataframe
stats = pd.read_csv('C:\\Users\\GS769ZA\\OneDrive - EY\\Documents\\Python Udemy\\Section 4\\DemographicData.csv')
#print(stats)

#renaming columns
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']

stats.head()

#print(stats.InternetUsers<2 )
#True or False
Filter = (stats.InternetUsers<2 )

#get certain tows
stats[3:7]

#gives rows where filter is true
print(stats[Filter])

#practice
Filter2 = stats.BirthRate > 40 
stats[Filter2]
stats[stats.BirthRate > 40 ]

#more interesting
# stats.BirthRate > 40 and stats.InternetUsers<2
#Error! (equivalent below)
# Filter and Filter2 

#have to convert series into single values
Filter & Filter2 
#only when both conditions are met will it return a true
#logical operator only!
stats[Filter & Filter2]
stats [(stats.BirthRate > 40) & (stats.InternetUsers<2)]

#Another one
stats.head()
stats[stats.IncomeGroup == 'High Income']

#How to get unique categories
stats.IncomeGroup.unique()

print(stats[stats.CountryName == 'Malta'])