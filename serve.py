from flask import Flask, request
import socket
import subprocess

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        process = subprocess.Popen(['python', 'stress_cpu.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return 'success'
    else:
        return socket.gethostname()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)