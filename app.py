from flask import Flask, jsonify
from dotenv import load_dotenv, dotenv_values
from google import genai


load_dotenv()

config = dotenv_values(".env")

client = genai.Client(api_key=config['GEMINI_API_KEY'])

app = Flask(__name__)

# Sample data
diseases = [
    {
        "name": "Flu",
        "symptoms": ["fever", "cough", "sore throat", "runny nose"]
    },
    {
        "name": "Common Cold",
        "symptoms": ["sneezing", "stuffy nose", "sore throat", "cough"]
    },
    {
        "name": "COVID-19",
        "symptoms": ["fever", "cough", "tiredness", "loss of taste or smell"]
    }
]

@app.route('/diseases', methods=['GET'])
def get_diseases():
    return jsonify(diseases)

@app.route('/chat', methods=['GET'])
def get_chat():
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        "You a disease diagnosing staff",
        "Create a basic diagnosis for a patient with the following symptoms: black skin spots, swelling, fever, vomiting, and headache.",
        "The patient has been experiencing the symptoms for a week already",
        "Provide an accurate diagnosis"
        ])
    
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
