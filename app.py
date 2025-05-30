from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "aezakmiAEZAKMI261@"  # غيّر هذا إلى توكن تحقق خاص بك

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # التحقق من التوكن
        token_sent = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token_sent == VERIFY_TOKEN:
            return challenge
        return "Invalid verification token", 403

    if request.method == "POST":
        data = request.json
        print("Received message:", data)
        return "Event received", 200

if __name__ == "__main__":
    app.run()
