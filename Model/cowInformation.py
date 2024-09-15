import csv
csv_path = 'Model/cowInform.csv'
def cowInformation():
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile)
        cow = []
        for row in reader:
            cow.append(row)
    return cow

def get_cow_breasts(cowId):
    cow = cowInformation()
    cowId = str(cowId)
    for c in cow:
        c = clean_cow_data(c)
        if c['CowId'] == cowId:
            return c.get('CowBreasts')  
    return 'Not Found'  

# remove leading and trailing whitespaces ex. goat not have age and breasts
def clean_cow_data(cow):
    return {k.strip(): v for k, v in cow.items()}

def get_cow_age(cowId):
    cow = cowInformation()
    cowId_str = str(cowId)
    for c in cow:
        c = clean_cow_data(c)  
        if c['CowId'] == cowId_str:
            c.get('CowAge') != None
            return c.get('CowAge')
    return 'Not Found'





