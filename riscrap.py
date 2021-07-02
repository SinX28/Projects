from selenium import webdriver #importation lib selenium
import time
import sys
import os
from selenium.common.exceptions import NoSuchElementException     
import shutil
import pickle
import json
import requests

def move(res):

    os.chdir(res)
    os.mkdir("Scrap_Data")
    shutil.move("/Users/maximep/Downloads/*",res+"Scrap_Data/") #Changer cette itération Nulle


def check_exists_by_xpath(xpath):
    
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def search(query,browser,driver='./driver/chromedriver'): #Retourne les URL à an alyser

    driver = webdriver.Chrome(executable_path=driver) #bien ajouter le ./ car c'est un executable
    driver.get(browser) #Récupération du site
    #Entre la recherche dans la search Bar
    bar_rech = driver.find_element_by_id("search_form_input_homepage")
    bar_rech.send_keys(query)
    #Appuie sur rechercher
    srch_but = driver.find_element_by_id("search_button_homepage")
    srch_but.click()

    searching = driver.find_elements_by_xpath("//div/h2/a[@class='result__a js-result-title-link']")

    for link in searching: #pour chaque lien ressortant de la recherche (extrait le nom)   
        print(link.text)

    responses = driver.find_elements_by_xpath("//*[contains(@class,'result__url ')]") 
    lst = []

    for link in responses: #On met dans un array dynamique toute les url histoire de pas avoir d'erreur de merde
        link.text
        lst.append(link.text)
        print("Adding ["+link.text+"]")
   
    print("Searching done !")
    
    return lst #retourne la liste des URLs
   
def scrap(lst,driver='./driver/chromedriver'): #prend en param l'array d'URL ajouter mode en fonction du site

    driver = webdriver.Chrome(executable_path=driver)

    for el in lst: #Pour chaque url on fait ce qui xsuit:
        
        print("Going on "+el)
        
        

        try: #except+ si on est sur pastbin
            if el.find("pastebin")>0: #Soluce temp, ca dependra du nombre de site a trouver (si + de 4 refonte intégrale du code)
                
                driver.get(el)
                time.sleep(2)
                print("[Pastebin] Pass "+driver.find_element_by_xpath("//button[@mode='primary']").text)
                driver.find_element_by_xpath("//button[@mode='primary']").click()


                dl = driver.find_element_by_xpath("//a[contains(@href,'/dl/')]") #
                print("Clicking on " + dl.text)
                dl.click()
        

            else:           #autre sites comme rentry.co (elif a chaque nous site implémenté)

                prefile=requests.get(el+"/Raw")
                print(prefile)
                with open("result/"+el[-4:]+".txt", "w") as out_f:
                    out_f.write(prefile.text)

        except NoSuchElementException:
            pass


    print("Scraping done")
#Début

if len(sys.argv)<2:

    print("ERROR: python3 riscrap.py <file_config.p>")

else:

    fconf=str(sys.argv[1])

    if fconf.find(".json")>0: #car en cas de non match la valeure renvoyé est -1

        print("Json File Detected")

        data = json.load( open( fconf, "rb" ))

    else:

        print("Pickle File Detected")

        data = pickle.load( open( fconf, "rb" ),encoding='bytes' )


    url = search(data['query'],data['browser'],data['driver'])
    scrap(url)
    #move(data['result_path'])



