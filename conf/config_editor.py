import pickle
import json
stri =[""]
choix=""

def choice(i):
    
    switcher={
                
        0:"'password dump' +@gmail.com site:pastebin.com",
        1:"https://duckduckgo.com/",
        2:"./driver/chromedriver",
        3:"~/Desktop/"
             
    }

    return switcher.get(i,"out of range")


print("Création du fichier de Configuration :\n (les champs laissé vide seront remplis automatiquement)\n\n")

stri.insert(0,input("QUERY_DORK>>>"))
stri.insert(1,input("(laisser vide)BROWSER>>>"))
stri.insert(2,input("(laisser vide)DRIVER>>>"))
stri.insert(3,input("RESULT_PATH>>>"))
stri.insert(4,input("NAME CONFIG>>>"))

choix=input("Save extention: json/p ?")

while choix != "json" and choix != "p":
    print("Error please retype the format type output")
    choice=input("Save extention: json/p ?\n")

i=0

for var in stri: #Cherche les var vides

    if not(var):

        stri[i]=choice(i)

    i+=1


conf={ 
        
        "query":stri[0],
        "browser":stri[1], 
        "driver":stri[2], 
        "result_path":stri[3],
        "name":stri[4]
    
    }


print("query: "+stri[0]+"\nbrowser: "+stri[1]+"\ndriver: "+stri[2]+"\nresult_path: "+stri[3]+"\n")


if choix=="p":

    pickle.dump( conf, open( stri[4]+".p", "wb" ) )
    print("Génération du fichier "+stri[4]+".p")
else:

    print("Génération du fichier "+stri[4]+".p")
    with open(stri[4]+'.json', 'w') as json_file:
        json.dump(conf, json_file)


print("Génération terminée !")

exit(0)