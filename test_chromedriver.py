from selenium import webdriver #importation lib selenium
import time
import os
from selenium.common.exceptions import NoSuchElementException     
import shutil
import pickle

# Config 

conf= { "query":"'password dump' +@gmail.com site:pastebin.com", #Génération de la configuration standart du fichier de la query (exemple)
        "browser":"https://duckduckgo.com/",
        "driver":"./chromedriver",
        "result_path":"~/Desktop/"

    }

pickle.dump(conf,open("scrap_conf.p","wb"))


def check_exists_by_xpath(xpath):
    
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

driver = webdriver.Chrome(executable_path="./chromedriver") #bien ajouter le ./ car c'est un executable

driver.get("https://duckduckgo.com/") #Récupération du site

#Entre la recherche dans la search Bar
bar_rech = driver.find_element_by_id("search_form_input_homepage")



bar_rech.send_keys("'password dump' +@gmail.com site:pastebin.com")

#Indexage de chaque stickers

#Appuie sur rechercher

srch_but = driver.find_element_by_id("search_button_homepage")
srch_but.click()

#element = driver.find_element_by_xpath("//form[input/@name ='search']")

searching = driver.find_elements_by_xpath("//div/h2/a[@class='result__a js-result-title-link']")

for link in searching: #pour chaque lien ressortant de la recherche (extrait le nom)
    
    print(link.text)

responses = driver.find_elements_by_xpath("//*[contains(@class,'result__url ')]")
    
print("-----____________----- ")

lst = []

for link in responses: #On met dans un array dynamique toute les url histire de pas avoir d'erreur de merde

    link.text

    lst.append(link.text)

    print("Adding ["+link.text+"]")
   

#print(lst)

for el in lst: #Pour chaque url on fait ce qui xsuit:

    print(el)

    driver.get(el)

    time.sleep(2)

    try:
     
       print("Pass "+driver.find_element_by_xpath("//button[@mode='primary']").text)
       driver.find_element_by_xpath("//button[@mode='primary']").click()
    
    except NoSuchElementException:
        print("Pas de AGREE")

    dl = driver.find_element_by_xpath("//a[contains(@href,'/dl/')]") #

    print("Clicking on " + dl.text)

    dl.click()

os.chdir("")

os.mkdir("Scrap_Data")

shutil.move("/Users/maximep/Downloads/*",path+"Scrap_Data/")

