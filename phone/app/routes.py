from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Record, Gather
import os
import requests
import speech_recognition as sr
from intent_classifier import IntentClassifier

app = Flask(__name__)

full_path = ''
text = ''

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
    global text
    global full_path
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
                print("chunking")
    full_path = os.path.join(os.getcwd(),file)
    
    r = sr.Recognizer()
    audio = ''
    with sr.WavFile(full_path) as source:              # use "test.wav" as the audio source
        audio = r.record(source)                        # extract audio data from the file

    text = r.recognize_google(audio, language = 'en-US', show_all=True)

    resp.redirect("https://cshelper.ngrok.io/passString")

    resp.hangup()
    return str(resp)

@app.route("/passString", methods=['POST'])
def passString():
    resp = VoiceResponse()
    gather = Gather(num_digits=1, action = '/newQuestion')
    
    # testIC = IntentClassifier()
    # testIC.train_model()
    # ans = testIC.train_model()
    # print(ans)
    
    try:
        ic = IntentClassifier()
        answer = ic.answer(text)
        resp.say(answer)
    except:
        resp.say("Couldn't transcribe audio")        
    
    resp.sap("Do you have another question? If not, please hang up")
    resp.redirect('/voice')
    return str(resp)

@app.route("/validation", methods=['GET','POST'])
def validation():
    resp = VoiceResponse()
    
    if 'Digits' in request.values:
        choice = request.values['Digits']
        
        if choice == '1':
            resp.say("Thank you for your response.")
        elif choice == '2':
            resp.say("We will log this response. Thank you for your call.")
        
        resp.say("Have a good day.")
    
    resp.hangup()
    os.remove(full_path)
    return str(resp)


if __name__ == "__main__":
    port = int(os.getenv('PORT', 8080))
    app.run(debug=True, use_reloader=False, port=port)
