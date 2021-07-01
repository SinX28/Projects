import pickle

stri =[""]

def choice(i):
    switcher={
                
        0:"'password dump' +@gmail.com site:pastebin.com",
        1:"https://duckduckgo.com/",
        2:"./driver/chromedriver",
        3:"~/Desktop/"
             
    }

    return switcher.get(i,"Invalid day of week")


print("Création du fichier de Configuration :\n (les champs laissé vide seront remplis automatiquement)\n\n")

stri.insert(0,input("QUERY_DORK>>>"))
stri.insert(1,input("(laisser vide)BROWSER>>>"))
stri.insert(2,input("(laisser vide)DRIVER>>>"))
stri.insert(3,input("RESULT_PATH>>>"))
stri.insert(4,input("NAME CONFIG>>>"))

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
print("Génération du fichier "+stri[4]+".p")

pickle.dump( conf, open( stri[4]+".p", "wb" ) )

print("Génération terminée !")

exit(0)