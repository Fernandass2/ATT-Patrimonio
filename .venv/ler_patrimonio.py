import csv

# Abrir o aquivo csv e atribuir a uma variável 
arquivo = open("Patrimônio.csv","r",encoding="utf8")
linhas = csv.reader(arquivo)


for i in linhas:
    lin = str(i).replace("['","").replace("']","").split(";")
    if(lin[0]=="1452"):
        print(lin)