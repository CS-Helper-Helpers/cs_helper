import os
import sys
sys.path.append("/home/groups3/cshelper/public_html/cgi-bin/cs_helper/")
import requests
import speech_recognition as sr

from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Record, Gather
from twilio.rest import Client
from intent_classifier import IntentClassifier
from tensorflow.keras.models import load_model
from app import app

full_path = ''
text = ''
answer = ''
ic = IntentClassifier()
loaded = load_model("../intent_classifier/model.h5")

# HTML code for web page
@app.route('/')
def index():
    return '''
<html>
    <head>
        <title>Home Page - CS Helper</title>
    </head>
    <body>
        <h1>Welcome to the Computer Science Department!</h1>
        <p> Activate me by saying Hey CS Helper or AI Have a Question <br>Or type your question below </p>
        <form>
            <label for="question_input">Question</label><br>
            <input type="text" id="question_input" name="question_input" size = 100><br>
            <input type="submit" value="Submit">
        </form>
    </body>
    <link rel="icon" href="data:;base64,iVBORw0KGgo=">
</html>'''

@app.route("/voice", methods=['POST'])
def voice():
    resp = VoiceResponse()
    
    resp.say("You have reached the Computer Science Department Office.")
    resp.say("This is CS Helper. Your call is being temporarily recorded. How may I help you?")
    
    # Records audio and goes to /getrecording after 2 seconds of silence
    resp.record(timeout=2, action = "/getrecording")
    return str(resp)

@app.route("/getrecording", methods=['POST'])
def getrecording(): 
    global full_path
    
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    
    recSID = request.form.get('RecordingSid')
    recURL = request.form.get('RecordingUrl') + '.wav'
    
    resp = VoiceResponse()
    resp.say("Just a moment")

    # Retrieves the URL for the current recording
    wav_link = requests.get(recURL, stream = True)
    file = recSID + ".wav"
       
    # Saves the wav file locally
    with open(file, "wb") as wav:
        for chunk in wav_link.iter_content(chunk_size=1024):
            if chunk:
                wav.write(chunk)
    full_path = os.path.join(os.getcwd(),file) 
    
    # Deletes the recording from the Twilio Recording
    client.recordings(recSID).delete()
    
    resp.redirect('/transcribeAudio')
    
    return str(resp)

@app.route("/transcribeAudio", methods=['POST'])
def transcribeAudio():
    global text
    global full_path
    resp = VoiceResponse()
    
    r = sr.Recognizer()
    audio = ''
    with sr.WavFile(full_path) as source:              # use "test.wav" as the audio source
        audio = r.record(source)                        # extract audio data from the file
        
    os.remove(full_path)
    full_path=''

    try:
        text = r.recognize_google(audio, language="en-US")
        resp.play('https://puce-chihuahua-4715.twil.io/assets/RoyaltyFree_CrazyParty_190374032322_1_8.mp3')
        resp.redirect('/passString')
    except:
        resp.say("Unable to transcribe your audio.")
        resp.say("Can you repeat your question?")
        resp.record(timeout=2, action = "https://cshelper.ngrok.io/getrecording")
    
    return str(resp)


@app.route("/passString", methods=['POST'])
def passString():
    global text
    global ic
    global answer
    
    resp = VoiceResponse()
    gather = Gather(num_digits=1, action = '/validation')
        
    resp.pause(length=5)
    answer = ic.answer(text)
    resp.say(answer)
    print(answer)   
    gather.say("Is this response satisfactory? Press 1 for yes, 2 for no.")
    resp.append(gather)
    resp.redirect('/voice')
    return str(resp)


@app.route("/validation", methods=['GET','POST'])
def validation():
    resp = VoiceResponse()
    gather = Gather(num_digits=1, action = '/newQuestion')
    qfile = open(r"QandAs.txt", "a")
    line = text + ", " + answer + ", " 
    
    if 'Digits' in request.values:
        choice = request.values['Digits']

        if choice == '1':
            resp.say("Thank you for your response.")
            line += "Correct Response\n"
        elif choice == '2':
            resp.say("We will log this response. Thank you for your call.")
            line += "Incorrect Response\n"
        
        qfile.write(line)
        
        gather.say("Do you have another question? If so, press 1. Otherwise, please hang up")
        resp.append(gather)
        resp.redirect('/voice')

    resp.hangup()
    qfile.close()
    return str(resp)

@app.route("/newQuestion", methods=['POST'])
def newQuestion():
    resp = VoiceResponse()
    
    if 'Digits' in request.values:
        choice = request.values['Digits']
        
        if choice == '1':
            resp.say("How may I help you?")
            resp.record(timeout=2, action = "https://cshelper.ngrok.io/getrecording")
    
    return str(resp)
