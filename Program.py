import sklearn as sk
import tensorflow as tf






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
    def encoder(text,model):
        # encodes the text to produces a response
        encoded =5
        return encoded
    def decoder(encodedText):
        # returns the decoded response
        decoded = 5
        return decoded
    
    def modelGen(dataset):
        model = "my model"
        return model
    
    
    def modelSave(model):
        print("model")
    
