import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

spam_header='spam\t'
no_spam_header='ham\t'
documents=[]
labels=[]

with open('SMSSpamCollection','r',encoding='UTF8') as file_handle:
    for line in file_handle:
        if line.startswith(spam_header):
            labels.append(1)
            documents.append(line[len(spam_header):])
        elif line.startswith(no_spam_header):
            labels.append(0)
            documents.append(line[len(no_spam_header)])

vectorizer=CountVectorizer()
term_counts=vectorizer.fit_transform(documents)
vocabulary=vectorizer.get_feature_names()

tf_transformer=TfidfTransformer(use_idf=False).fit(term_counts)
features=tf_transformer.transform(term_counts)

with open('processed.pickle','wb') as file_handle:
    pickle.dump((vocabulary,features,labels),file_handle)