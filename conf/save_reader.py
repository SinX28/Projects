import pickle
import sys

if len(sys.argv) < 2:

    print("ERREUR veuillez specifier le fichier\nde configuration à lire\npython3 save_reader.py <file_config.p>")

else:

    msg=str(sys.argv[1])

    print("\n   Lecture de "+str(sys.argv[1])+"...\n")

    data = pickle.load( open( msg, "rb" ),encoding='bytes' )

    print("query: "+data['query']+"\nchemin: "+data['result_path']+"\nnavigateur: "+data['browser']+"\ndriver: "+data['driver']+"\nnom sauvegarde:"+data['name']+"\n")

