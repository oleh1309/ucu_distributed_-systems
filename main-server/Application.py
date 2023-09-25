from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# List to store messages
messages = []

# Secondary server URL
secondary_server_url = "http://0.0.0.0:5001/replicate_messages"

# Route to receive messages
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json(force=True)
    message = data.get('message')
    messages.append(message)

    # Replicate to secondary server
    replicate_to_secondary(message)

    return jsonify({"message": "Message received."})

# Function to replicate data to secondary server
def replicate_to_secondary(message):
    requests.post(secondary_server_url, json={"message": message})

# Route to get ordered list of sent messages
@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({"messages": messages})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')