from Basketball_data import Games,Players, Seasons, FieldGoalAttempts, MinutesPlayed, Sdict, Pdict, Salary, FieldGoals
import warnings 
warnings.filterwarnings('ignore')
import numpy as np
import matplotlib.pyplot as plt

def myplot(playerlist):
    for name in playerlist:
        plt.plot(Games[Pdict[name]], c='pink', ls='--', marker='s', ms=3, label = Players[Pdict[name]])
    plt.xticks(list(range(0,10)), Seasons, rotation = 'vertical')
    plt.legend(loc= 'upper left', bbox_to_anchor=[1,1])
    plt.xticks(list(range(0,10)), Seasons, rotation = 'vertical')
    plt.tight_layout
    plt.show()
myplot(['KobeBryant', 'LeBronJames', 'DerrickRose'])