from selenium import webdriver #importation lib selenium
from selenium.common.exceptions import NoSuchElementException
import requests
import time
import logging




def scrap(lst,driver='./driver/chromedriver',debmod=False): #prend en param l'array d'URL ajouter mode en fonction du site

    if not debmod:
        logging.basicConfig(format='%(asctime)s %(message)s')
    else:
        logging.basicConfig(format='%(asctime)s %(message)s',level=logging.INFO)
        print("--debug_scp--")

    driver = webdriver.Chrome(executable_path=driver)

    for el in lst: #Pour chaque url on fait ce qui xsuit:
        
        logging.info("[INFO] Going on {}".format(el)) #INFO
        
        if el.find("pastebin")>0: #Soluce temp, ca dependra du nombre de site a trouver (si + de 4 refonte intégrale du code)

            try:

                driver.get(el)
                time.sleep(2)
                logging.info("[INFO] Pass pastebin's {} button".format(driver.find_element_by_xpath("//button[@mode='primary']").text))#INFO
                driver.find_element_by_xpath("//button[@mode='primary']").click()
                    
            except NoSuchElementException:
                
                logging.warning("[WARNING] Unable to find AGREE button")#WARNING

            dl = driver.find_element_by_xpath("//a[contains(@href,'/dl/')]") #
            logging.info("[INFO] Clicking on {}".format(dl.text))#INFO
            dl.click()
        
        else:           #autre sites comme rentry.co (elif a chaque nous site implémenté)

            prefile=requests.get("{}/Raw".format(el))
            logging.info(prefile)
                
            with open("result/{}.txt".format(el[-4:]), "w") as out_f:
                out_f.write(prefile.text)

    logging.info("[INFO] Scraping done")#INFO
