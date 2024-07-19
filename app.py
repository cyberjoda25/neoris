from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"

@app.route('/DevOps', methods=['POST'])
def devops():
    if request.headers.get('X-Parse-REST-API-Key') != API_KEY:
        return "ERROR", 403

    data = request.json
    if not data or 'to' not in data:
        return "Invalid data", 400

    response = {
        "message": f"Hello {data['to']} your message will be sent"
    }
    return jsonify(response)

@app.route('/DevOps', methods=['GET', 'PUT', 'DELETE'])
def devops_error():
    return "ERROR", 405

if __name__ == '__main__':
    app.run(debug=True)