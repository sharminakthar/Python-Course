import pandas as pd
import os 

#method 1 : specify full path to file 
#windows:
stats = pd.read_csv('C:\\Users\\GS769ZA\\OneDrive - EY\\Documents\\Python Udemy\\Section 4\\DemographicData.csv')
#print(stats)

#method 2 : change working directory

print(os.getcwd())

#Windows:
os.chdir('C:\\Users\\GS769ZA\\OneDrive - EY\\Documents\\Python Udemy\\Section 4')