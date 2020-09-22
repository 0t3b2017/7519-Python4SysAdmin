from flask import Flask, Response, request
import json
from aula01 import desafio

app = Flask(__name__)

@app.route("/")
def index():
    retorno = {
        "app": "Sistema de encrypt / decrypt rot13 - by Jcruz",
        "version": 1.0
    }

    return Response(
        json.dumps(retorno),
        200,
        content_type="application/json"
    )

@app.route("/encrypt", methods=["POST"])
def encrypt():
    retorno = request.get_json()
    msg = retorno['msg']
    encrypted_msg = desafio.rot13_encrypt(msg)
    data = {
        "msg": encrypted_msg
    }
    return Response(json.dumps(data), 200, content_type="application/json")

@app.route("/decrypt", methods=["POST"])
def decrypt():
    retorno = request.get_json()
    msg = retorno['msg']
    decrypted_msg = desafio.rot13_decrypt(msg)
    data = {
        "msg": decrypted_msg
    }
    return Response(json.dumps(data), 200, content_type="application/json")

if __name__ == "__main__":
    app.run(debug=True)
