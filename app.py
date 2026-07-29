from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/message")
def message():
    return jsonify({"message": "Hello from Flask on AWS!"})

if __name__ == "__main__":
    app.run(debug=True)