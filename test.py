import pickle

lexicon = {}
# set up a dictionary to store the orthographic similarity
with open('letter_lexicon.pickle', 'rb') as handle:
    lexicon = pickle.load(handle)
    
f = open("lexicon.csv", "w")
f.write("pair, similarity")

for key in lexicon:
    f.write("\n" + str(key) + ", " + str(lexicon.get(key)))

f.close()
