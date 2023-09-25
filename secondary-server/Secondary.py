from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# List to store messages
messages = []

# Route to get ordered list of sent messages
@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({"messages": messages})

# Route to replicate messages from main server
@app.route('/replicate_messages', methods=['POST'])
def replicate_messages():
    data = request.get_json(force=True)
    message = data.get('message')
    messages.append(message)
    # Send ACK back to main server
    send_ack(message)

    return jsonify({"message": "Message replicated."})

# Function to send ACK back to main server
def send_ack(ack_message):
    # Assume main server URL is known
    main_server_url = "http://main-server:5000/acknowledge"
    requests.post(main_server_url, json={"ack_message": "hello"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')