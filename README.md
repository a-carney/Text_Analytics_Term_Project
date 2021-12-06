# Text_Analytics_Term_Project
Term Project for Text Analytics Class At USM


Using Pubmed as a data base, we are looking to pick 4 disease topics, and import the data for the disease name and corresponding abstract
Using nltk and pandas, clean up data and place into dataset
Using sklearn, run classifier tests using Naïve Bayes, Support Vector Classification, and Logistic Regression


Results for Naive Bayes...
Accuracy Score:  0.9623
Precision Score: 0.9621
Recall Score:  0.9602
F1 Score:  0.9610
Elapsed time: 5.8202 seconds
Results for SVM...
Accuracy Score:  0.9883
Precision Score: 0.9880
Recall Score:  0.9879
F1 Score:  0.9879
Elapsed time: 8.4739 seconds
Results for Logistic Regression....
Accuracy Score:  0.9875
Precision Score: 0.9871
Recall Score:  0.9871
F1 Score:  0.9871
Elapsed time: 7.8276 seconds


Conclusion:
Based on the three classifiers, I would consider Logistical Regression to be the best.
Naives Bayes makes assumption for independence, which is ill-fitting for this type of data
SVM, although was fast with this data, would likely become much more time consuming with larger quantities of data
Using Logistical Regression, we could now have a program that assigns disease names to abstracts 
![image](https://user-images.githubusercontent.com/77558389/144905710-62ec5104-8cf0-4430-be4e-f4f1163e9967.png)

