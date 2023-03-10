from flask import Flask, request, render_template
from chatbot import chat

app = Flask(__name__)


@app.route('replace with your url')
def home():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    text = ""
    prompt = text + "\n" + user_input
    if len(prompt) <= 2000:
        result = chat(prompt)
    else:
        result = chat(prompt[-2000:])
    return {'chatbot_response': result}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7000)
