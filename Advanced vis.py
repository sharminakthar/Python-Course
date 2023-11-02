from Basketball_data import Games,Players, Points, Seasons, FieldGoalAttempts, MinutesPlayed, Sdict, Pdict, Salary, FieldGoals
import warnings 
warnings.filterwarnings('ignore')
import numpy as np
import matplotlib.pyplot as plt

#fix up the inputs
#playerlist = Players gives default parameter
def myplot(data, playerlist = Players):
    #specify each player to colour and marker
    Col = {'KobeBryant':'Black', 'JoeJohnson':'Red', 'LeBronJames':'Green', 'CarmeloAnthony':'Blue', 'DwightHoward':'Magenta', 'ChrisBosh':'Black', 'ChrisPaul':'Red', 'KevinDurant':'Green','DerrickRose':'Blue', 'DwayneWade':'Magenta'}
    Mark = {'KobeBryant':'o', 'JoeJohnson':'*', 'LeBronJames':'s', 'CarmeloAnthony':'d', 'DwightHoward':'x', 'ChrisBosh':'+', 'ChrisPaul':'o', 'KevinDurant':'*','DerrickRose':'s', 'DwayneWade':'d'}
    for name in playerlist:
        #'data' has to replace 'Games'
        plt.plot(data[Pdict[name]], c=Col[name], ls='--', marker=Mark[name], ms=5, label = Players[Pdict[name]])
    plt.xticks(list(range(0,10)), Seasons, rotation = 'vertical')
    plt.legend(loc= 'upper left', bbox_to_anchor=[1,1])
    plt.xticks(list(range(0,10)), Seasons, rotation = 'vertical')
    plt.tight_layout
    plt.show()
    #Points comes from data
myplot(Points, ['KobeBryant', 'LeBronJames', 'DerrickRose'])