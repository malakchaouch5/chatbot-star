from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from nltk.chat.util import Chat, reflections

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Download necessary NLTK data
import nltk
nltk.download('punkt')

# Define English Q&A pairs
pairs = [
    (r"what is software\??", ["Software is a set of instructions that a computer uses to perform tasks like writing or gaming."]),
    (r"what is a software engineer\??", ["A software engineer designs, develops, and maintains programs and applications."]),
    (r"what does a software engineer do daily\??", ["They brainstorm ideas, write code, and test programs to ensure they work correctly."]),
    (r"hello|hi", ["Hi there! How can I assist you?", "Hello! Feel free to ask me anything about software engineering."]),
    (r"what is the story of google\??", [
        "Google started as a research project by Larry Page and Sergey Brin at Stanford. They created a revolutionary search algorithm, which grew into the world’s most popular search engine and a tech giant."
    ]),
    (r"how was facebook created\??", [
        "Facebook was created by Mark Zuckerberg in 2004 while he was a student at Harvard. It started as a campus social network and later expanded to connect people globally."
    ]),
    (r"what is microsoft's success story\??", [
        "Microsoft was founded by Bill Gates and Paul Allen in 1975. Their breakthrough came with the MS-DOS operating system, followed by the Windows platform, revolutionizing personal computing."
    ]),
    (r"how did amazon succeed\??", [
        "Amazon began as an online bookstore founded by Jeff Bezos in 1994. It grew by diversifying into e-commerce, cloud computing (AWS), and entertainment, becoming a global powerhouse."
    ]),
    (r"what made apple successful\??", [
        "Apple was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976. Its success is attributed to innovative products like the iPhone, iPad, and Mac, alongside a strong focus on design and user experience."
    ]),
    (r"can you share a software engineering success story\??", [
        "Sure! The development of Linux by Linus Torvalds is a great example. Starting as a personal project, Linux became the backbone of servers, mobile devices (Android), and many modern technologies."
    ]),
    (r"(.*)", ["I'm not sure I understand. Can you rephrase your question?"])
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Route to serve the homepage
@app.route("/")
def index():
    return render_template("index.html")

# Route for chatbot communication
@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")
        response = chatbot.respond(user_message)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"response": "An error occurred: " + str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)