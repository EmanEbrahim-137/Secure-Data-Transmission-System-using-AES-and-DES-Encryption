from flask import Flask, render_template, request
from encription import encrypt_text
from decrypt import decrypt_text
from encription_des import encrypt_text as encrypt_text_des
from decrypt_des import decrypt_text as decrypt_text_des


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    text = ''

    if request.method == 'POST':
        text = request.form.get('text', '').strip()
        action = request.form.get('action')
        algorithm = request.form.get('algorithm', 'aes')

        if action == 'encrypt':
            if algorithm == 'des':
                result = encrypt_text_des(text)
            else:
                result = encrypt_text(text)
        elif action == 'decrypt':
            try:
                if algorithm == 'des':
                    result = decrypt_text_des(text)
                else:
                    result = decrypt_text(text)
            except Exception as e:
                result = f"Decryption Failed: {str(e)}"

    return render_template('index.html', result=result, text=text, algorithm=request.form.get('algorithm', 'aes'))

if __name__ == '__main__':
    app.run(debug=True)
