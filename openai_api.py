from flask import Blueprint, request, jsonify
from openai_functions import generate_response

openai_api = Blueprint('openai_api', __name__)


@openai_api.route('/generate', methods=['POST'])
def generate():
    prompt = request.json.get('prompt')
    if prompt is None:
        message = "Please enter a prompt."
    else:
        message = generate_response(prompt)

    return jsonify({'message': message})
