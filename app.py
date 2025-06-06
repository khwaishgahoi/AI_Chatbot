# from flask import Flask, request, jsonify, send_from_directory
# import json
# import os

# app = Flask(__name__)

# # Load FAQ data from JSON file at startup
# with open('faq_data.json', 'r') as f:
#     faq_data = json.load(f)

# # Function to find answer based on keyword matching
# def find_answer(user_message):
#     user_message = user_message.lower()

#     for topic, content in faq_data.items():
#         for keyword in content['response']:
#             if keyword in user_message:
#                 return content['response']
#     return None

# # Chat endpoint
# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.json
#     message = data.get("message", "").lower()

#     # Try to find an answer from JSON data
#     answer = find_answer(message)
#     if answer:
#         return jsonify({"response": answer})

#     # Optional: fallback to greetings or other hardcoded responses
#     greetings = ['hi', 'hello', 'hey']
#     if any(greet in message for greet in greetings):
#         return jsonify({"response": "Hi there! How may I assist you today?"})

#     return jsonify({"response": "I'm sorry, I don't have an answer to that yet. How else may I help you?"})

# # Homepage route (for your index.html)
# @app.route("/")
# def home():
#     return send_from_directory('.', 'index.html')

# # Suggested FAQs endpoint for quick access questions
# @app.route("/suggested-questions", methods=["GET"])
# def suggested_questions():
#     # Top suggested questions
#     suggestions = [
#         {"question": "How can I book a room?"},
#         {"question": "What is the check-in and check-out time?"},
#         {"question": "Do you have parking available?"},
#         {"question": "What food and dining options are available?"}
        
#     ]
#     return jsonify(suggestions)

# # Run the Flask app
# if __name__ == "__main__":
#     app.run(debug=True)





from flask import Flask, request, jsonify, send_from_directory
import json

app = Flask(__name__)

# Load FAQ data from JSON file
with open('faq_keywords.json', 'r') as f:
    faq_data = json.load(f)

# Suggested questions with fixed responses
suggested_responses = {
    "How can I book a room?": "You can book directly on our website at https://live.ipms247.com/booking/book-rooms-hotelmoksha or contact us at +91 9557053066.",
    "What is the check-in and check-out time?": "Check-in is at 1:00 PM and check-out is at 11:00 AM.",
    "Do you have parking available?": "Yes, we have limited on-site parking for 8–10 cars. Larger vehicles like tempo travellers can park nearby at your own expense.",
    "What food and dining options are available?": "Breakfast is served from 8:00 AM to 10:00 AM. Last restaurant order is at 9:00 PM. Extra breakfast costs ₹250."
}

# ✅ Keyword-based answer matching
def find_answer(user_message):
    user_message = user_message.lower()

    for topic, content in faq_data.items():
        for keyword in content['keywords']:
            if keyword.lower() in user_message:
                return content['response']
    return None

# ✅ POST endpoint for chatbot
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "").lower()

    # Check if it's one of the suggested questions
    for q, response in suggested_responses.items():
        if message == q.lower():
            return jsonify({"response": response})

    # Check for keyword matches in JSON
    answer = find_answer(message)
    if answer:
        return jsonify({"response": answer})

    # Greetings fallback
    greetings = ['hi', 'hello', 'hey']
    if any(greet in message for greet in greetings):
        return jsonify({"response": "Hi there! How may I assist you today?"})

    # Final fallback
    return jsonify({"response": "I'm sorry, I don't have an answer to that yet. Could you please rephrase?"})

# ✅ Serve index.html when opened from browser
@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

# ✅ GET endpoint to fetch suggested questions
# @app.route("/suggested-questions", methods=["GET"])
# def suggested_questions():
#     return jsonify([
#         {"question": q} for q in suggested_responses.keys()
#     ])

@app.route("/suggested-questions", methods=["GET"])
def suggested_questions():
    suggestions = [
        {"question": "How can I book a room?"},
        {"question": "What is the check-in and check-out time?"},
        {"question": "Do you have parking available?"},
        {"question": "What food and dining options are available?"}
    ]
    return jsonify(suggestions)


# ✅ Run the app
if __name__ == "__main__":
    app.run(debug=True)

