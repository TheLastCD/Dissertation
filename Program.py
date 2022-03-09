import sklearn as sk
import tensorflow as tf
import pandas as pd





class Response_Get():
    def findResponse(question):
        # get the response to the question answered
        response = "from internet" 
        return response
    def Question():
        # receive a question
        question = "whats 2+2?"
        return question
    def QuestionEncoding(question):
        # perform any encoding necassery to prepare the question
        encodedQuestion = "shdfbs"
        return encodedQuestion


class Response_Tailor():
    
    def modelGen(dataset,questionGiver, questionAnswer):
        model = "my model"
        return model
    
    
    def modelSave(model):
        print("model")
    
class Encoder():
    def hello():
        return 0

class Decoder():
    def hello():
        return 0

def Clean(dataset):
    dataset['Utterance'] = dataset['Utterance'].str.replace(r'\"','')
    return dataset.dropna()

    
dataset = pd.read_csv('Johnny Depp.csv')
print(dataset)
dataset = Clean(dataset)
print (dataset)



    