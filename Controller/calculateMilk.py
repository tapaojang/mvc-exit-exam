import re
from Model.cowInformation import get_cow_age
def calculateMilk(cowId):
    cowAge = get_cow_age(cowId)
    years_match = re.search(r'(\d+) years?', cowAge)
    months_match = re.search(r'(\d+) months?', cowAge)

    years_match = int(years_match.group(1)) if years_match else 0
    months_match = int(months_match.group(1)) if months_match else 0

    litersOfMilk = years_match + months_match

    return litersOfMilk