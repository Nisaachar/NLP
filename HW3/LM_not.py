import pandas as pd
import re
from nltk.lm.preprocessing import pad_both_ends
from nltk.util import bigrams
from nltk.lm.preprocessing import flatten
from nltk.util import everygrams
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE
import pickle


def train_LM(path):
    df = pd.read_csv(path)
    #looping through each row
    for i in range(len(df)):
        text = df.loc[i,"comment_text"]

        if df.loc[i,"toxic"] == 0:
            #normalisation and tokenisation
            noNumber = re.sub(r'\d+', '',text) #Removing all the numbers from the text to normalize it.
            noUnder = re.sub(r'_', '', noNumber) #Removing underscores. There were many instances of words with '_' in the text.
            strLower = noUnder.lower() #lower casing the text
            strPunch = re.sub(r'[^\w\s]', '', strLower)  #removing all the puntuations like commas, fullstops, brackets, etc. Anything ie, other than a word or space.
            finalText = strPunch.split() #removing all the white spaces, newlines, or tabs. 

            #forming Ngrams
            train, vocab = padded_everygram_pipeline(2, finalText)

            ##delaring lm as a global variable so that it can also be accessed by the second function which then calculates the MLE score
            #for individual text. 
            global lm 
            lm = MLE(2)

            #training the model
            lm.fit(train, vocab)


    ##saving the model into a csv file using pickle. 
    with open("trained_model.csv", "wb") as f:
        pickle.dump(lm, f)



def test_LM(pathTest, filePath):
    dfTest = pd.read_csv(pathTest)
    dfModel = pd.read_csv(filePath)
    dfTest['MLE Score'] = 0
    
    for i in range(len(dfTest)): 
        dfTest.loc[i, "MLE Score"] = lm.logscore(dfTest.loc[i,"comment_text"], [dfModel.loc[i,"comment_text"]])
    
    #saving the result to csv. this file contains the MLE score of each row. 
    dfTest.to_csv('results.csv')
    print(dfTest)
    return None




filePath = input("Enter the name/path of the training file: ")
train_LM(filePath)

pathTest = input('Enter path to the test file: ')
test_LM(pathTest, filePath)

   

