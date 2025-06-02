from flask import Flask, render_template, request
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    return render_template('caesar.html', 
                         encrypt_result={
                             'text': text,
                             'key': key,
                             'result': encrypted_text
                         })

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    return render_template('caesar.html', 
                         decrypt_result={
                             'text': text,
                             'key': key,
                             'result': decrypted_text
                         })

@app.route("/vigenere_encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key.upper())
    return render_template('vigenere.html', 
                         encrypt_result={
                             'text': text,
                             'key': key,
                             'result': encrypted_text
                         })

@app.route("/vigenere_decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key.upper())
    return render_template('vigenere.html', 
                         decrypt_result={
                             'text': text,
                             'key': key,
                             'result': decrypted_text
                         })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)