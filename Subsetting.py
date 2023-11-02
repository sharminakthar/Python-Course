import pandas as pd

stats = pd.read_csv('C:\\Users\\GS769ZA\\OneDrive - EY\\Documents\\Python Udemy\\Section 4\\DemographicData.csv')
#print(stats)

#rename columns without space
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']

#Subsetting datafames in pandas
#print(stats.head())

#Rows!
#extract certain rows, row 21 to and incl 25 slicing
stats[21:26]
#print(stats[21:26])

#print everything
#print(stats[:])

#reverse dataframe
print(stats[::-1])

#only every 20th country
print(stats[::20])

#Columns!
print(stats.columns)

#stats['ColummnName']
print(stats['CountryName'].head())

#list = ['CountryName', 'BirthRate']
#stats[[...]].head()
stats[['CountryName', 'BirthRate']].head()

#Quick access, requires name to be one word 
#rename columns to be one word

stats.head()

stats['BirthRate']
print(stats.BirthRate)

#top five
print(stats.BirthRate.head())

#Rows and Columns!
stats[4:8][['CountryName', 'BirthRate']]
#equivalent to
stats[['CountryName', 'BirthRate']][4:8]
#sliced 4,5,6,7th row and country name and birthrate
