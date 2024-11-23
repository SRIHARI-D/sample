from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the YouTube Transcript and PDF Generator API!"
if __name__ == '__main__':
    app.run(debug=True)
