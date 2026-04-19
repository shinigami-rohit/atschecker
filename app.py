from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "ATS Checker is running successfully 🚀"

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "API working ✅"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
