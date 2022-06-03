import csv
import json

def make_json(csvFilePath, jsonFilePath,keyWord):
     
    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        
        for rows in csvReader:
             
            # Assuming a column named 'No' to
            # be the primary key
            key = rows[keyWord]
            data[key] = rows
            
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
         
def make_comparation():

    listAd = []
    listGd = []

    with open('file-ad.json', encoding='utf-8') as meu_json:
        dadosAd = json.load(meu_json)
        
        for i in dadosAd:
            #print(dadosAd[i].get("Email"))
            listAd.append(dadosAd[i].get("Email"))


    with open('file-gd.json', encoding='utf-8') as meu_json:
        dadosGd = json.load(meu_json)
        
        for i in dadosGd:
            listGd.append(dadosGd[i].get("Email Address"))

    suspended = set(listAd) & set(listGd)

    for i in suspended:
        print(i)


csvFilePath_ad = r'../../file-ad.csv'
jsonFilePath_ad = r'../../file-ad.json'
keyword_ad = input("Keyword da tabela:")
 
csvFilePath_gd = r'../../file-gd.csv'
jsonFilePath_gd = r'../../file-gd.json'
keyword_gd = input("Keyword da tabela:")
 
# Call the make_json function
make_json(csvFilePath_ad, jsonFilePath_ad,keyword_ad)
make_json(csvFilePath_gd,jsonFilePath_gd,keyword_gd)
