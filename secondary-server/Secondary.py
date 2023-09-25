from flask import Flask, request, jsonify

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

    return jsonify({"message": "Message replicated."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')