from Basketball_data import Games,Players, Seasons, FieldGoalAttempts, MinutesPlayed, Sdict, Pdict, Salary, FieldGoals
import warnings 
warnings.filterwarnings('ignore')
import numpy as np
import matplotlib.pyplot as plt

#figure size
plt.rcParams['figure.figsize'] = 6,5

#c= colour, ls= linestyle, marker = points, ms = marker size
#plt.plot(Salary[0], c='pink', ls='--', marker='s', ms=3, label = Players[0])
#plt.xticks(list(range(0,10)), Seasons, rotation = 'vertical')
#plt.show()

#Expanded visualisation
plt.plot(Salary[0], c='pink', ls='--', marker='s', ms=3, label = Players[0])
plt.plot(Salary[1], c='orange', ls='--', marker='s', ms=3, label = Players[1])
plt.plot(Salary[2], c='yellow', ls='--', marker='s', ms=3, label = Players[2])
plt.plot(Salary[3], c='blue', ls='--', marker='s', ms=3, label = Players[3])
plt.plot(Salary[4], c='purple', ls='--', marker='s', ms=3, label = Players[4])
plt.plot(Salary[5], c='pink', ls='--', marker='o', ms=3, label = Players[5])
plt.plot(Salary[6], c='orange', ls='--', marker='o', ms=3, label = Players[6])
plt.plot(Salary[7], c='yellow', ls='--', marker='o', ms=3, label = Players[7])
plt.plot(Salary[8], c='blue', ls='--', marker='o', ms=3, label = Players[8])
plt.plot(Salary[9], c='purple', ls='--', marker='o', ms=3, label = Players[9])
#add and position legend
plt.legend(loc= 'upper left', bbox_to_anchor=[1,1])
plt.xticks(list(range(0,10)), Seasons, rotation = 'vertical')
plt.tight_layout
plt.show()
