# coding : utf-8
#1)considérant que dans le titre ou les autres cellules on ne trouvera peu ou pas de mots, non plus trouverons-nous de termes qui pourraient induire en erreur notre classement, je vais les inclure dans la tokenization
#2) j'ai très mal compris ce cours, étant sur pc je me retrouvais constamment à devoir traduire ce qui était expliqué en NLTK et comme ça allait vite et que je croyais que c'était mon ordi le problème, je n'ai pas trop insisté, aussi, après 
#une journée de travail sur ce code, je ne pense pas avoir trouvé la solution, mais je propose quand même des avenues qui fonctionnent selon moi. 

import csv, nltk, string

martino = "martino.csv"

from nltk.tokenize import word_tokenize
from nltk.tokenize import casual_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
set(stopwords.words("french"))
from collections import Counter

f=open("martino.csv", encoding="mbcs")
chroniques=f.read()
mots=chroniques.split()
# print(mots)
# print('-----------------------------------------------------------------------------------------------------------------')

for mot in mots:
    token = mots
    filteredsentence = [] 
    if token not in stop_words:
        filteredsentence.append
    # pour une raison obscure, la fonction stop_words ne fonctionne pas, contrairement à ce que j'ai trouvé sur internet, j'ai vérifié que stopwords était importé sur mon ordi et c'est le cas... ce sera donc en commentaire dans la livraison et je vais essayer de terminer l'exercice sans.
    

    stemmer = SnowballStemmer("french")
    words = [fr.stem(token) for mot in word_tokenize(filteredsentence) if mot not in stopwords.words("french") and mot not in string.punctuation]
    print(words)
    #ici aussi la racinisation ne fonctionne pas, on diriat que tous les plus in nltk ne veulent rien savoir... Mais normalement ça devrait fonctionner.

    tabous=freqdist1
    freqdist1=freqdist(words)
    print(tabous)
