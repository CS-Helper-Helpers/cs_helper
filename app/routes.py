from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Record
import os
#from intent_classifier import predictions
import speech_recognition as sr  

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<html>
    <head>
        <title>Home Page - CS Helper</title>
    </head>
    <body>
        <h1>Welcome to the CS Helper Web App!</h1>
    </body>
    <link rel="icon" href="data:;base64,iVBORw0KGgo=">
</html>'''

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls and mention the caller's city"""
    # Start our TwiML response
    resp = VoiceResponse()
    
    resp.say("You have reached the Computer Science Department Office.")
    resp.say("At the tone, ask a question. Then press pound.")
    
    resp.record(finish_on_key='#')
    #resp.play('https://demo.twilio.com/docs/classic.mp3')
    
    resp.hangup() 

    return str(resp)

@app.route("/record", methods=['GET', 'POST'])
def record():
    """Returns TwiML which prompts the caller to record a message"""
    # Start our TwiML response
    response = VoiceResponse()

    # Use <Say> to give the caller some instructions
    response.say('Hello. Please leave a message after the beep.')

    # Use <Record> to record the caller's message
    response.record(timeout=10, transcribe=True)

    print(response)

    return str(response)

if __name__ == "__main__":
    port = int(os.getenv('PORT', 8080))
    app.run(debug=True, use_reloader=False, port=port)
