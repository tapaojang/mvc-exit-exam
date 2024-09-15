from Model.cowInformation import cowInformation
from Model.cowInformation import get_cow_age
from Model.cowInformation import get_cow_breasts
def isValidCow(cowId):
    cow = cowInformation()
    # print(cow)
    for c in cow:
        if c['CowId'] == cowId:
            return True   
    return False

def isCow(cowId):
    print(get_cow_age(cowId))
    if get_cow_age(cowId) == None:
        return False
    return True

def isFourBreasts(cowId):
    print(get_cow_breasts(cowId))
    if get_cow_breasts(cowId) == '4':
        return True
    return False