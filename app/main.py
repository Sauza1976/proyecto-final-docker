from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open("app/data.json") as f:
    respuestas = json.load(f)

@app.route("/chat", methods=["POST"])
def chat():
    pregunta = request.json.get("pregunta", "").lower()
    respuesta = respuestas.get(pregunta, "No entiendo la pregunta")
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
