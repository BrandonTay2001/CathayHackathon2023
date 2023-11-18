from flask import Flask, request, jsonify
from flask_cors import CORS

from generate_timetable import generate

app = Flask(__name__)
CORS(app)

@app.route('/generate_timetable', methods=['POST'])
def generate_timetable():
    location = request.json['city']
    pace = request.json['pace']
    prompt = request.json['prompt']
    startDate = request.json['startDate']
    endDate = request.json['endDate']
    inputStr = f"Pacing: {pace}\nStart date: {startDate}\nPrompt: {prompt}\nDestination: {location}\nEnd date: {endDate}\n\nResponse (do not include newline characters in response):\n"
    processed_json = generate(inputStr)
    return jsonify(processed_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0')