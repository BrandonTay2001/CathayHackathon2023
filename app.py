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
    inputStr = f"""
    Pacing: {pace}
    Destination: {location}
    Start date: {startDate}
    End date: {endDate}
    Prompt: {prompt}
    
    Apart from attractions, also fit in lunch and dinner recommendations between activities. Durations of each activity should be between 30 minutes to 90 minutes.
    Response (do not include newline characters in response):
    """
    processed_json = generate(inputStr)
    return jsonify(processed_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0')