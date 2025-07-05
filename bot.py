from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "hi" in incoming_msg:
        msg.body("Yo! It’s OnyiGPT live online. Let’s talk.")
    elif "help" in incoming_msg:
        msg.body("Available commands: hi, gold, help.")
    elif "gold" in incoming_msg:
        msg.body("Gold setup coming up. Send chart or ask for market bias.")
    else:
        msg.body("I don’t recognize that command yet. Type 'help'.")

    return str(resp)
