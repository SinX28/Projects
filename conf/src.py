from selenium import webdriver #importation lib selenium
from selenium.common.exceptions import NoSuchElementException
import logging
import shutil
import time
import os

def move(a,b): #Used to change path of file result

    try:
        files = os.listdir(a)
        for f in files:
            print(a+f)
            shutil.move(a+f, b)#mettre exception

    except : 
        print ("[INFO] Erreur un fichier porte déjà le même nom") 
    #    Add whatever logic you want to execute

def next(driver,debmod=False): #étend la somme des résultats trouvés

    
    if not debmod:
        logging.basicConfig(format='%(asctime)s %(message)s')
    else:
        logging.basicConfig(format='%(asctime)s %(message)s',level=logging.INFO)

    while True:

        try:

            logging.info("[INFO] Targeting of extending button")
            pages_but = driver.find_element_by_class_name('result--more__btn')#Cliquer sur le bouton plus de résultat
            time.sleep(2)
            
            pages_but.click()
            time.sleep(2)
            logging.info("[INFO] Clicking Done")

        except NoSuchElementException:
            
            logging.warning("[WARINING] Extention no exist")
            break



def search(query,browser,pages=0,driver='./driver/chromedriver',debmod=False): #Retourne les URL à an alyser

    if not debmod:
        logging.basicConfig(format='%(asctime)s %(message)s')
    else:
        print("--debug_src--")
        logging.basicConfig(format='%(asctime)s %(message)s',level=logging.INFO)

    driver = webdriver.Chrome(executable_path=driver) #bien ajouter le ./ car c'est un executable
    driver.get(browser) #Récupération du site
    bar_rech = driver.find_element_by_id("search_form_input_homepage") #Entre la recherche dans la search Bar
    bar_rech.send_keys(query) #Appuie sur rechercher
    srch_but = driver.find_element_by_id("search_button_homepage")
    srch_but.click()
    lst = []

    #Gestion des pages

    if pages==0: #Cela veut dire qu'une seule page 0 donc pas d'extention
        logging.info("[INFO] Only one page")
    else:
        logging.info("[INFO] Several pages detected")
        time.sleep(2)
        next(driver,debmod)
    
    #On commence a réeunir les URLs
    responses = driver.find_elements_by_xpath("//*[contains(@class,'result__url ')]") 
    searching = driver.find_elements_by_xpath("//div/h2/a[@class='result__a js-result-title-link']")
    
    print("Nbr elements sur la page {}".format(len(searching)))
    #result__a js-result-title-link
    for link in searching: #pour chaque lien ressortant de la recherche (extrait le nom)   
        logging.info("[INFO] {} found".format(link.text))

    for link in responses: #On met dans un array dynamique toute les url histoire de pas avoir d'erreur de merde
        link.text
        lst.append(link.text)
        logging.info("[INFO] Adding [{}]".format(link.text))#INFO
            
    logging.info("[INFO] Searching done !")#INFO
    return lst #retourne la liste des URLs
