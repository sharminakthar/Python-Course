import pandas as pd 

# Full dataframe
stats = pd.read_csv('C:\\Users\\GS769ZA\\OneDrive - EY\\Documents\\Python Udemy\\Section 4\\DemographicData.csv')
#print(stats)

#renaming columns
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']

#Accessing individual elements

# for labels : even integers are treated as labels
# .at

# for integer location
# .iat

print(stats.head())

print(stats.iat[3,4])
#Upper Middle Income @ 3rd row and 4th column

print(stats.at[2, 'BirthRate'])
#second row, and birthrate column

#every 10th row -> subtable
sub10 = stats [::10]

sub10.iat[10,0]
#Libya
#Looks for 10th row in the sub10 data = 100th

sub10.at[10,'CountryName']
#Azerbaijan 
#Looks for label '10'