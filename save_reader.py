import pickle

print("   Lecture de la Save...")

data = pickle.load( open( "scrap_conf.p", "rb" ),encoding='bytes' )

print("query: "+data['query'])
print("chemin: "+data['result_path'])
print("navigateur: "+data['browser'])


