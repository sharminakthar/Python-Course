from Basketball_data import Games,FieldGoalAttempts, MinutesPlayed, Sdict, Pdict, Salary, FieldGoals
import warnings 
warnings.filterwarnings('ignore')
import numpy as np

#Salary[][]
print(Pdict['LeBronJames'])
#2
print(Sdict['2009'])
#4

Salary[Pdict['LeBronJames']][Sdict['2009']]
#15779912

#Matrix division
#how many points per game average
FieldGoals / Games
#gives long numbers, not neat
FieldGoalsPerGame = (np.matrix.round(FieldGoals/Games))

#normalising, 
#minutes played by each player per game
MinutesPlayedPerGame = (np.matrix.round(MinutesPlayed/Games))

#Accuracy of Players in percent
Accuracy = (np.matrix.round(100 * (FieldGoals/FieldGoalAttempts)))
print(Accuracy)