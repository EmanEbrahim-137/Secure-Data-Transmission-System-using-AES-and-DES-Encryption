from flask import Flask, render_template, request
from encription import encrypt_text
from decrypt import decrypt_text


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    text = ''

    if request.method == 'POST':
        text = request.form.get('text')
        action = request.form.get('action')

        if action == 'encrypt':
            result = encrypt_text(text)
        elif action == 'decrypt':
            result = decrypt_text(text)

    return render_template('index.html', result=result, text=text)

if __name__ == '__main__':
    app.run(debug=True)
