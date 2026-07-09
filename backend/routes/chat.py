from flask import Blueprint, request, jsonify
from services.ai_service import ai

chat_bp = Blueprint("chat", __name__)

employees = {
    1: {
        "name": "Sarah",
        "role": "Receptionist"
    },
    2: {
        "name": "Mike",
        "role": "Sales"
    },
    3: {
        "name": "Grace",
        "role": "Customer Support"
    }
}


@chat_bp.route("/chat", methods=["POST"])
def chat():

    data = request.json

    employee_id = data.get("employee_id")
    message = data.get("message")

    employee = employees.get(employee_id)

    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    response = ai.chat(employee, message)

    return jsonify(response)
