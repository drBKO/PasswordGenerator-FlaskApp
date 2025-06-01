from flask import Flask, render_template, request
import secrets
import string
import random

app = Flask(__name__)

def generate_password(length, use_digits, use_symbols):
    if length < 4:
        return "Error: Min length 4"

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    password_chars = [secrets.choice(letters)]
    if use_digits:
        password_chars.append(secrets.choice(digits))
    if use_symbols:
        password_chars.append(secrets.choice(symbols))

    char_pool = letters
    if use_digits:
        char_pool += digits
    if use_symbols:
        char_pool += symbols

    while len(password_chars) < length:
        password_chars.append(secrets.choice(char_pool))

    random.shuffle(password_chars)
    return ''.join(password_chars)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        use_digits = request.form.get('digits') == 'yes'
        use_symbols = request.form.get('symbols') == 'yes'
        password = generate_password(length, use_digits, use_symbols)

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
