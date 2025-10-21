import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load the API key from environment variables
GOOGLE_AI_API_KEY = os.getenv('GOOGLE_AI_API_KEY')
GOOGLE_AI_ENDPOINT = "AIzaSyDCMMybMYrBCNWPNWYPSMFKZR-oeaulW5k"  # Replace with actual endpoint

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_code():
    # Parse user input
    data = request.get_json()
    language = data['language']
    comments = data['comments']

    # Call the Google AI Studio API
    try:
        headers = {
            "Authorization": f"Bearer {GOOGLE_AI_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "gemini-2.0-flash-exp",  # Example model name
            "input": comments,
            "parameters": {
                "language": language
            }
        }
        response = requests.post(GOOGLE_AI_ENDPOINT, headers=headers, json=payload)

        if response.status_code == 200:
            generated_code = response.json().get("generated_code", "// Code could not be generated.")
        else:
            generated_code = f"// Error: {response.status_code} - {response.text}"

    except Exception as e:
        generated_code = f"// An error occurred: {str(e)}"

    return jsonify({"code": generated_code})


if __name__ == '__main__':
    app.run(debug=True)
