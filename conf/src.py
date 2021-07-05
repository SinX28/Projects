from selenium import webdriver #importation lib selenium
import logging
import shutil
import os

logging.basicConfig(format='%(asctime)s %(message)s')

def move(a,b): #Used to change path of file result

    files = os.listdir(a)

    for f in files:

        print(a+f)
        shutil.move(a+f, b)#mettre exception


def search(query,browser,driver='./driver/chromedriver'): #Retourne les URL à an alyser

    driver = webdriver.Chrome(executable_path=driver) #bien ajouter le ./ car c'est un executable
    driver.get(browser) #Récupération du site
    bar_rech = driver.find_element_by_id("search_form_input_homepage") #Entre la recherche dans la search Bar
    bar_rech.send_keys(query) #Appuie sur rechercher
    srch_but = driver.find_element_by_id("search_button_homepage")
    srch_but.click()
    searching = driver.find_elements_by_xpath("//div/h2/a[@class='result__a js-result-title-link']")

    for link in searching: #pour chaque lien ressortant de la recherche (extrait le nom)   
        logging.info("[INFO] ".format(link.text))

    responses = driver.find_elements_by_xpath("//*[contains(@class,'result__url ')]") 
    lst = []

    for link in responses: #On met dans un array dynamique toute les url histoire de pas avoir d'erreur de merde
        link.text
        lst.append(link.text)
        logging.info("[INFO] Adding [{}]".format(link.text))#INFO
   
    logging.info("[INFO] Searching done !")#INFO
    
    return lst #retourne la liste des URLs
