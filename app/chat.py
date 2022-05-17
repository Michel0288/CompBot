from flask import request
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from keras.models import load_model
import json
import random
# model = load_model('general.h5')
# intents = json.loads(open('app/general/general.json', encoding='utf-8').read())

# words = pickle.load(open('words.pkl','rb'))
# classes = pickle.load(open('classes.pkl','rb'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    if(model=="general"):
        model = load_model('general.h5')
        words = pickle.load(open('words1.pkl','rb'))
        classes = pickle.load(open('classes1.pkl','rb'))
    if(model=="computing_about"):
        model = load_model('computing_about.h5')
        words = pickle.load(open('words.pkl','rb'))
        classes = pickle.load(open('classes.pkl','rb'))
    if(model=="computing_staff"):
        model = load_model('computing_staff.h5')
        words = pickle.load(open('words2.pkl','rb'))
        classes = pickle.load(open('classes2.pkl','rb'))
    if(model=="computing_courses"):
        model = load_model('computing_courses.h5')
        words = pickle.load(open('words3.pkl','rb'))
        classes = pickle.load(open('classes3.pkl','rb'))
        
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.50
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints,model):
    if(model=="computing_courses"):
        intents = json.loads(open('app/courses/computing_courses.json', encoding='utf-8').read())
    if(model=="computing_staff"):
        intents = json.loads(open('app/lecturers/computing_staff.json', encoding='utf-8').read())
    if(model=="general"):
        intents = json.loads(open('app/general/general.json', encoding='utf-8').read())
    if(model=="computing_about"):
        intents = json.loads(open('app/about/computing_about.json', encoding='utf-8').read())
    tag = ints[0]['intent']
    list_of_intents = intents['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
        else:
            result = "You must ask the right questions"
    return result

def chatbot_response():
    while True:
        if request.method == 'POST':
            msg = request.form['userinput']
            modeltype=request.form['modeltype']
            ints = predict_class(msg, modeltype)
            res = getResponse(ints,modeltype)
            return res