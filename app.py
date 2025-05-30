from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "aezakmiAEZAKMI261@"  # هذا هو التوكن الذي ستكتبه في إعدادات Meta

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("WEBHOOK_VERIFIED")
            return challenge, 200
        else:
            return "Verification token mismatch", 403

    elif request.method == "POST":
        data = request.get_json()
        print("Received message:", data)
        return "EVENT_RECEIVED", 200

@app.route("/")
def home():
    return "Webhook is running!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
