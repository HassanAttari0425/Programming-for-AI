from flask import Flask, render_template, request
import openai

openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"
model_name = "deepseek/deepseek-r1:free"

app = Flask(__name__)

chat_history = [{"role": "system", "content": "You are a helpful assistant."}]

def clean_input(text):
    cleaned = text.encode("utf-8", "ignore").decode("utf-8", "ignore")
    cleaned = ''.join(c for c in cleaned if c.isprintable())
    return cleaned.strip()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    cleaned_input = clean_input(user_input)

    chat_history.append({"role": "user", "content": cleaned_input})

    response = openai.ChatCompletion.create(
        model=model_name,
        messages=chat_history,
        headers={
            "HTTP-Referer": "http://localhost:5003",
            "X-Title": "My Chat App",
        }
    )

    bot_reply = response.choices[0].message["content"]

    #history
    chat_history.append({"role": "assistant", "content": bot_reply})

    return render_template('index.html', user_input=cleaned_input, bot_response=bot_reply)

if __name__ == '__main__':
    app.run(debug=True, port=5003)

