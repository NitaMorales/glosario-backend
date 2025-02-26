from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Forzar que permita cualquier origen en TODOS los endpoints
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.route("/")
def home():
    return "¡Backend funcionando correctamente!"

@app.route("/generate-definition", methods=["POST"])
def generate_definition():
    data = request.get_json()
    word = data.get("word", "")
    if not word:
        return jsonify({"error": "No se proporcionó ninguna palabra"}), 400
    
    return jsonify({
        "significado": f"{word} es una sombra que se extiende en el tiempo.",
        "vease": "eco; reflejo; vacío",
        "origen": "Nació del silencio de las cosas olvidadas.",
        "suenos": "Ser algo más de lo que ya es."
    })

if __name__ == '__main__':
    app.run(debug=True)

