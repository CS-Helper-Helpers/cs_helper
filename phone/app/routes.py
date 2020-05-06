import os
import requests
import speech_recognition as sr

from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Record, Gather
from twilio.rest import Client
from intent_classifier import IntentClassifier
from tensorflow.keras.models import load_model

app = Flask(__name__)

full_path = ''
text = ''
answer = ''
ic = IntentClassifier()
#ic.train_model()
loaded = load_model("../cs_helper/model.h5")

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
    
    resp.record(timeout=2, action = "https://cshelper.ngrok.io/getrecording")
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

    wav_link = requests.get(recURL, stream = True)
    file = recSID + ".wav"
       
    with open(file, "wb") as wav:
        for chunk in wav_link.iter_content(chunk_size=1024):
            if chunk:
                wav.write(chunk)
    full_path = os.path.join(os.getcwd(),file) 
    client.recordings(recSID).delete()
    
    resp.redirect('transcribeAudio')
    return str(resp)

@app.route("/transcribeAudio", methods=['POST'])
def transcribeAudio():
    global text
    resp = VoiceResponse()
    
    r = sr.Recognizer()
    audio = ''
    with sr.WavFile(full_path) as source:              # use "test.wav" as the audio source
        audio = r.record(source)                        # extract audio data from the file

    try:
        text = r.recognize_google(audio, language="en-US")
        resp.redirect('/passString')
    except:
        resp.say("Unable to transcribe your audio.")
        resp.say("Can you repeat your question?")
        resp.record(timeout=2, action = "https://cshelper.ngrok.io/getRecording")
    
    return str(resp)


@app.route("/passString", methods=['POST'])
def passString():
    global text
    global ic
    global answer
    
    resp = VoiceResponse()
    gather = Gather(num_digits=1, action = '/validation')
    
    resp.pause(length=10)
    
    try:
        answer = ic.answer(text)
        resp.say(answer)
        print(answer)
    except:
        resp.say("We were unable to find an answer to your question.")        
    gather.say("Is this response satisfactory? Press 1 for yes, 2 for no.")
    resp.append(gather)
    resp.redirect('/voice')
    os.remove(full_path)
    return str(resp)


@app.route("/validation", methods=['GET','POST'])
def validation():
    resp = VoiceResponse()
    gather = Gather(num_digits=1, action = '/newQuestion')
    wrongQs_file = open(r"WrongQandAs.txt", "a")
    
    if 'Digits' in request.values:
        choice = request.values['Digits']

        if choice == '1':
            resp.say("Thank you for your response.")
        elif choice == '2':
            resp.say("We will log this response. Thank you for your call.")
            line = text + ", " + answer
            wrongQs_file.write(line)
            wrongQs_file.write("\n")
        
        gather.say("Do you have another question? If so, press 1. Otherwise, please hang up")
        resp.append(gather)
        resp.redirect('/voice')

    resp.hangup()
    wrongQs_file.close()
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


if __name__ == "__main__":
    port = int(os.getenv('PORT', 8080))
    app.run(debug=True, use_reloader=False, port=port)
