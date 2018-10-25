
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
import numpy
#print(dir(gensim))
from nltk.tokenize import word_tokenize


"""
Criar alguns docoumetos
"""
#raw_documents = [""]


def similarity(adress_list):
    text_file = open("bairros.txt", "r")
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

    """
    s = 0
    for i in corpus:
        s += len(i)

    """
    #print(s)


    """
    Now create a query document and convert it to tf-idf.
    """
    sims = gensim.similarities.Similarity('D:\similarity/',tf_idf[corpus],
                                        num_features=len(dictionary))

    #print ("Sims")
    #print(sims)
    #print(type(sims))


    for ad in adress_list:
        query_doc = [w.lower() for w in word_tokenize(ad)]
        #print(query_doc)
        query_doc_bow = dictionary.doc2bow(query_doc)
        #print(query_doc_bow)
        query_doc_tf_idf = tf_idf[query_doc_bow]
        #print(query_doc_tf_idf)

        print ("Analisando : "+ad+" Resultado "+raw_documents[sims[query_doc_tf_idf].argmax(axis=0)])
        ##print ("Resultado "+raw_documents[sims[query_doc_tf_idf].argmax(axis=0)])

    """ Array com asimilaridade"""
    """
    print ((sims[query_doc_tf_idf]))
    print ((sims[query_doc_tf_idf].argmax(axis=0)))
    print (type(sims[query_doc_tf_idf]))
    print ('Size')
    print (sims[query_doc_tf_idf].size)
    """
    """
    for x in range (0, sims[query_doc_tf_idf].size):
        if  sims[query_doc_tf_idf][x] > 0.5:
            print ("Simi "+ str(sims[query_doc_tf_idf][x])+" Valor "+raw_documents[x])
            #print (raw_documents[x])

    """



    """
    ---------------------------------------------------------------------------------
    

    query_doc = [w.lower() for w in word_tokenize("AV. BIAS FORTES")]
    #print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    #print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    #print(query_doc_tf_idf)
    print ("Result")
    print (raw_documents[sims[query_doc_tf_idf].argmax(axis=0)])

    """


if __name__ == "__main__":
        adress_list = ["AVENIDA AFONSO pena 120", "DAS PRINCESA", "GETULIO VARGAS"]
        text_file = open("endereco.txt", encoding="utf8")
        raw_documents = text_file.readlines()

        stoplist = [
        "RECAPEAMENTO ASFÁLTICO DA ", 
        "RECAPEAMENTO DA ",
        "RECAPEMENTO DA ",
        'RECAPEAMENTO PARA ',
        "RECAPEAMENTO UTILIZANDO ASFALTO MOÍDO",
        "SERVIÇO CE TAPA BURACOS NA",
        "RECAPEAMENTO ASFÁLTICO EM TODA A EXTENSÃO DA "
        "RECAPEAMENTO UTILIZANDO ASFALTO MOÍDO NA ",
        'ASFALTAMENTO DA ',
        "SERVIÇO DE TAPA BURACOS NA ",
        "SERVIÇO DE TAPA BURACOS DA ",
        "SERVIÇO DE TAPA BURACOS EM TODA A EXTENSÃO DA",
        "SERVIÇO DE TAPA BURACOS EM TODA EXTENSÃO DA ",
        "SINALIZAÇÃO HORIZONTAL NA ",
        "COLOCAÇÃO DE POSTE NA ",
        "ILUMINAÇÃO PÚBLICA EM ",
        "IMPLANTAÇÃO DE BUEIROS / BOCAS DE LOBO",
        "IMPLANTAÇÃO DE CICLOVIA NA ",
        "IMPLANTAÇÃO DE ILUMINAÇÃO PÚBLICA NA ",
        "IMPLANTAÇÃO DE RAMPA DE ACESSIBILIDADE NA ",
        "INSTALAÇÃO DE REDE DE ESGOTO NO ",
        "MANUTENÇÃO DA REDE PLUVIAL NA ",
        "MANUTENÇÃO DA SINALIZAÇÃO HORIZONTAL DAS ",
        "PODA DE ÁRVORE NA ",
        "SOLICITA NA",
        "SOLICITA ",
        "SOLICITA TAPA BURACO NA RUA " ,
        "TAPA BURACOS AO LONGO DA ",
        "TAPA BURACO NA ",
        "TAPA BURACOS NA ",
        "SERVIÇO DE "]

        #print (raw_documents)

        for i in range (0, len(raw_documents)):
            for s in stoplist:
                if s in raw_documents[i]:
                    raw_documents[i] = raw_documents[i].replace(s , "")



        print (raw_documents)
        #similarity(raw_documents)