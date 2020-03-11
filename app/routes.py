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
    
    resp.play('https://demo.twilio.com/docs/classic.mp3')
    
    resp.hangup() 

    return str(resp)

if __name__ == "__main__":
    port = int(os.getenv('PORT', 8080))
    app.run(debug=True, use_reloader=False, port=port)
