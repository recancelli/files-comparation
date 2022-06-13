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

def make_comparation(jsonFilePath,columnName):

    listDados = []

    with open(jsonFilePath, encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
        
        for i in dados:
            #print(dadosAd[i].get("Email"))
            listDados.append(dados[i].get(columnName))

    return (listDados)

def result_comparation(jsonFilePathAd,columnNameAd, jsonFilePathGd, columnNameGd):
   
   suspended = set(make_comparation(jsonFilePathAd,columnNameAd)) & set(make_comparation(jsonFilePathGd,columnNameGd))
   
   resultFilePath = r'../../docs/file-result.csv'
   
   
   with open(resultFilePath, 'w', encoding='utf-8') as f:
        f.write(str(suspended))

# ad = Active Directory
csvFilePath_ad = r'../../docs/file-ad.csv'
jsonFilePath_ad = r'../../docs/file-ad.json'
keyword_ad = "Nome"
 
# gd = Google Drive
csvFilePath_gd = r'../../docs/file-gd.csv'
jsonFilePath_gd = r'../../docs/file-gd.json'
keyword_gd = "First Name"
 

make_json(csvFilePath_ad, jsonFilePath_ad,keyword_ad)
make_json(csvFilePath_gd,jsonFilePath_gd,keyword_gd)


## mudar variavel "email" porque nao é esse nome
result_comparation(jsonFilePath_ad,"Email",jsonFilePath_gd,"Email Address")