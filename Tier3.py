import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix
from timer import Timer

t = Timer()
t.start()

# create empty list for abstracts and search terms
Abstracts = []
Search_Term = []

# open and read text file and turn into list with comma as delimeter
file = open("withDelimeterAbstracts.txt", 'r')
file = file.read()
file = file.split(" , ")

#    use following algorith to place each list item into either the
# Abstract or Search_Term list
count = 0
for x in file:
    if count % 2 == 0:
        Abstracts.append(x)        
    else:
        Search_Term.append(x)
    count+=1

# create dictionary of two lists for pandas
inputForDF = {'Abstract' : Abstracts, 'Search_Term' : Search_Term}

# use pandas to put dict into df
df = pd.DataFrame.from_dict(inputForDF, orient='index')
df = df.transpose()



# crop data to max of 10,000 items per Search_Term
a = df[df.Search_Term == " acute rheumatic arthritis"].iloc[:10000]
b = df[df.Search_Term == " disease lyme"].iloc[:10000]
c = df[df.Search_Term == " abnormalities cardiovasculars"].iloc[:10000]
d = df[df.Search_Term == " knee osteoarthritis"].iloc[:10000]

# append pieces back to df
df = a.append(b).append(c).append(d)

# declare depedent and independent varialbe
x = df['Abstract'].to_list()
y = df['Search_Term'].to_list()


# train_test_split function
x_train, x_test, y_train, y_test = train_test_split(x, y, 
                                    train_size=0.8, random_state=17)



print("Data is ready for testing...")
t.stop()
t.start()


#Naive Bayes
bayes = Pipeline([('count', CountVectorizer()), ('transform', TfidfTransformer()),
        ('classifier', MultinomialNB())])
bayes.fit(x_train, y_train)
predict = bayes.predict(x_test)

print("Results for Naive Bayes...")
print("Accuracy Score:  %.4f" % (accuracy_score(y_test, predict)))
print("Precision Score: %.4f" % (precision_score(y_test, predict, average='macro')))
print("Recall Score:  %.4f" % (recall_score(y_test, predict, average='macro')))
print("F1 Score:  %.4f" % (f1_score(y_test, predict, average='macro')))
t.stop()
t.start()

#SVM
svm = Pipeline([
        ('count', CountVectorizer()),
        ('transform', TfidfTransformer()),
        ('classify', SGDClassifier())
        ])
svm.fit(x_train, y_train)
predict = svm.predict(x_test)
print("Results for SVM...")
print("Accuracy Score:  %.4f" % (accuracy_score(y_test, predict)))
print("Precision Score: %.4f" % (precision_score(y_test, predict, average='macro')))
print("Recall Score:  %.4f" % (recall_score(y_test, predict, average='macro')))
print("F1 Score:  %.4f" % (f1_score(y_test, predict, average='macro')))
t.stop()
t.start()

#Logistic Regression
lr = Pipeline([
        ('count', CountVectorizer()),
        ('transform', TfidfTransformer()),
        ('classify', LogisticRegression())
        ])

lr.fit(x_train, y_train)
predict = lr.predict(x_test)
print("Results for Logistic Regression....")
print("Accuracy Score:  %.4f" % (accuracy_score(y_test, predict)))
print("Precision Score: %.4f" % (precision_score(y_test, predict, average='macro')))
print("Recall Score:  %.4f" % (recall_score(y_test, predict, average='macro')))
print("F1 Score:  %.4f" % (f1_score(y_test, predict, average='macro')))
t.stop()



