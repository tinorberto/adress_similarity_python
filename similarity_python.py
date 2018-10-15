
"""
Install gensim
Instalacao do nltk
pip install -U nltk

Download dos reasourves  
import nltk
nltk.download()

https://www.oreilly.com/learning/how-do-i-compare-document-similarity-using-python

"""
import gensim

#print(dir(gensim))
from nltk.tokenize import word_tokenize


"""
Criar alguns docoumetos
"""
#raw_documents = [""]


text_file = open("nome_logradouro.txt", "r")
raw_documents = text_file.readlines()


print("Number of documents:",len(raw_documents))

"""
List of tokens
"""
gen_docs = [[w.lower() for w in word_tokenize(text)] 
            for text in raw_documents]
#print(gen_docs)

"""
Create Dictionary 
A dictionary maps every word to a number.
"""
dictionary = gensim.corpora.Dictionary(gen_docs)
#print(dictionary[5])
#print(dictionary.token2id['road'])
print("Number of words in dictionary:",len(dictionary))

"""
for i in range(len(dictionary)):
    print(i, dictionary[i])

"""

"""
Bag-of-words representation for a document 
just lists the number of times each word occurs in the document.
"""

corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
#print ('Bag of words')
#print(corpus)

tf_idf = gensim.models.TfidfModel(corpus)
#print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
#print(s)


"""
Now create a query document and convert it to tf-idf.
"""
sims = gensim.similarities.Similarity('D:\similarity/',tf_idf[corpus],
                                      num_features=len(dictionary))

#print ("Sims")
#print(sims)
#print(type(sims))

query_doc = [w.lower() for w in word_tokenize("RUA JOAQUIM TEIXEIRA DOS ANJOS")]
#print(query_doc)
query_doc_bow = dictionary.doc2bow(query_doc)
#print(query_doc_bow)
query_doc_tf_idf = tf_idf[query_doc_bow]
#print(query_doc_tf_idf)

print ("Result")

""" Array com asimilaridade"""
print ((sims[query_doc_tf_idf]))
print ((sims[query_doc_tf_idf].argmax(axis=0)))
print (raw_documents[sims[query_doc_tf_idf].argmax(axis=0)])