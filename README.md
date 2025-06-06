Project Title:**Keyword-Based FAQ Chatbot using Flask used in offical HOTEL MOKSHA website**
Overview:
This is a simple chatbot built with Python (Flask) that replies to user queries based on keyword matching from a predefined JSON FAQ file.
Files:
**app.py** – Main Flask backend to process chat messages.
**faq_keywords.json** – Contains keyword-response pairs.
**index.html** – Basic frontend to interact with the chatbot.
How it works:
User types a message (e.g., “How can I pay?”).
Flask checks for matching keywords in faq_keywords.json.
If a match is found, a relevant answer is returned.
Supports greetings like “hi”, “hello”.
Gives a fallback response if nothing matches.
How to Run:
**Install Flask: pip install flask
Run: python app.py
Open: http://localhost:5000/**
Use Case:
Ideal for small websites or businesses needing automated FAQ support.
