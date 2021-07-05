import sys 

sys.path.append("/Users/maximep/Desktop/Perso/Prog/lib/conf")

import time
import sys
import os
import shutil
import json
import src
import scp
import logging

logging.basicConfig(format='%(asctime)s %(message)s')


#def move(res):

#    print("Déplacement du résultat")
#    shutil.move("/Users/maximep/Downloads/*","result/") #Changer cette itération Nulle

#Début

if len(sys.argv)<2:# A REVOIR AVEC PARSLIB

    logging.erreur("ERROR: python3 riscrap.py <file_config.p>")

else:

    logging.info("[INFO] Json File Detected") #INFO

    data = json.load( open( sys.argv[1], "rb" ))#Add try catch

    url = src.search(data['query'],data['browser'],data['driver'])
    scp.scrap(url,data['driver'])
    src.move("/Users/maximep/Downloads/",data['result_path'])



