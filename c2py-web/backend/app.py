from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    code = data.get("code", "")

    with open("input.c", "w") as f:
        f.write(code)

    try:
        subprocess.run(["../../parser.exe", "input.c", "out.py"], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return jsonify({"result": f"[parser.exe error]\n{e.stderr}"})

    if not os.path.exists("out.py"):
        return jsonify({"result": "Error: Python code not generated."})

    with open("out.py", "r") as f:
        output = f.read()

    return jsonify({"result": output})
if __name__ == "__main__":
    app.run(debug=True)
