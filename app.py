from flask import Flask, request, jsonify

from generate_timetable import generate

app = Flask(__name__)

# @app.route('/process_text', methods=['POST'])
# def process_text():
#     text = request.form.get('question')  # Get the 'text' parameter from the request
#     processed_text = get_answer(text)  # Process the input text

#     # Create a response dictionary
#     response = {
#         'answer': processed_text
#     }

#     return jsonify(response)

@app.route('/generate_timetable', methods=['POST'])
def generate_timetable():
    text = request.form.get('inputStr')
    processed_json = generate(text)
    return jsonify(processed_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0')