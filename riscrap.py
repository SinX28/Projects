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
import argparse

pars=argparse.ArgumentParser(description="Process to scrap some usefull raw text on a browser")

pars.add_argument('-d','--debug',help="Used to display debbug log",dest='debug',action="store_true")#permet d'afficher le mode debug
pars.add_argument('-f', '--file', dest='filename', help='Path to the selected config file')

arg=pars.parse_args()



if arg.debug:

    print("[Debug mode enabled]")

    logging.basicConfig(format='%(asctime)s %(message)s',level=logging.DEBUG)

else:

    logging.basicConfig(format='%(asctime)s %(message)s')

#Début

if not arg.filename:   # if filename is not given
    
    parser.error('Filename not given')

    logging.error("ERROR: python3 riscrap.py -f <file_config.p>")

else:

    logging.info("[INFO] Json File Detected") #INFO

    data = json.load( open( arg.filename, "rb" ))#Add try catch
    url = src.search(data['query'],data['browser'],data['driver'],arg.debug)
    
    scp.scrap(url,data['driver'],arg.debug)
    src.move("/Users/maximep/Downloads/",data['result_path'])
