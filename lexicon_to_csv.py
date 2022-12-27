import pickle

lexicon = {}

with open('letter_lexicon.pickle', 'rb') as handle:
    lexicon = pickle.load(handle)
    
f = open("lexicon.csv", "w")
f.write("character #1, character #2, similarity")

for key in lexicon:
    f.write("\n" + str(key)[0] + ", " + str(key)[1] + ", " + str(lexicon.get(key)))

f.close()
