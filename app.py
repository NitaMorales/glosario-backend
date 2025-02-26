from flask import Flask, request, jsonify

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)

