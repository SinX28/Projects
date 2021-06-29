import pickle

print("   Lecture de la Save...\n")

data = pickle.load( open( "scrap_conf.p", "rb" ),encoding='bytes' )

print("query: "+data['query']+"\nchemin: "+data['result_path']+"\nnavigateur: "+data['browser']+"\n")

