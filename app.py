from flask import Flask, request, jsonify

app = Flask(__name__)

# Example bad phrases
bad_phrases = ["win money", "click here", "lottery", "prize", "free gift"]

def detect_spam(text):
    score = 0
    if any(p in text.lower() for p in bad_phrases):
        score += 0.6
    if text.count("!") > 3:
        score += 0.3
    if text.isupper():
        score += 0.2
    if score >= 0.6:
        return "SPAM", score
    else:
        return "NOT SPAM", score

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    label, score = detect_spam(message)
    return jsonify({
        "message": message,
        "classification": label,
        "score": score
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
