import random
from Model.cowInformation import get_cow_breasts
def calculateBreasts(cowId):
    breastsNum = get_cow_breasts(cowId)
    print('breastsNum:', breastsNum)
    if breastsNum == '4':
        fourtothree = probfourtothree()
        print('fourtothree:', fourtothree)
        if fourtothree == False:
            return 3
        else:
            return 4
    else:  
        threetofour = probthreetofour()
        print('threetofour:', threetofour)
        if threetofour == False:
            return 4
        else:
            return 3

def probfourtothree():
    if random.randint(1,100) < 5:
        print('Your cow has 3 breasts')
        return False
    else:
        print('Your cow has 4 breasts')
        return True
    
# 20% chance of 4 breasts : false when breast change from 4 to 3
def probthreetofour():
    randomValue = random.randint(1,100)
    print('ramdom:', randomValue)
    if randomValue < 20:
        print('Your cow has 4 breasts')
        return False
    else:
        print('Your cow has 3 breasts')
        return True

    