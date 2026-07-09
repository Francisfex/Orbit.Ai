from flask import Blueprint, request, jsonify

from database.database import SessionLocal
from database.models import Employee

employee_bp = Blueprint("employee", __name__)

@employee_bp.route("/employees", methods=["GET"])
def get_employees():

    db = SessionLocal()

    employees = db.query(Employee).all()

    results = []

    for employee in employees:

        results.append({
            "id": employee.id,
            "business_id": employee.business_id,
            "name": employee.name,
            "role": employee.role
        })

    db.close()

    return jsonify(results)

@employee_bp.route("/employee/create", methods=["POST"])
def create_employee():

    db = SessionLocal()

    data = request.json

    employee = Employee(
        business_id=data.get("business_id"),
        name=data.get("name"),
        role=data.get("role"),
        system_prompt=data.get("system_prompt")
    )

    db.add(employee)

    db.commit()

    db.refresh(employee)

    db.close()

    return jsonify({
        "success": True,
        "employee_id": employee.id,
        "message": "Employee created successfully."
    })
