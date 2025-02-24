from flask import Flask, jsonify

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

if __name__ == '__main__':
    app.run(debug=True)
