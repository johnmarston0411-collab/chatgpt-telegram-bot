from flask import Flask, request
import subprocess
import os

app = Flask(__name__)
SECRET = os.getenv('SECRET_KEY')

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('X-Secret') == SECRET:
        subprocess.run(["/app/deploy.sh"], shell=True)
        return "OK", 200
    return "Forbidden", 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)