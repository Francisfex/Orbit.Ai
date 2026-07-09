from flask import Blueprint, request, jsonify

from database.database import SessionLocal
from database.models import Business

business_bp = Blueprint("business", __name__)

@business_bp.route("/businesses", methods=["GET"])
def get_businesses():

    db = SessionLocal()

    businesses = db.query(Business).all()

    results = []

    for business in businesses:

        results.append({
            "id": business.id,
            "name": business.name,
            "description": business.description,
            "phone": business.phone,
            "email": business.email
        })

    db.close()

    return jsonify(results)

@business_bp.route("/business/create", methods=["POST"])
def create_business():

    db.close()

    return jsonify(results)

    db = SessionLocal()

    data = request.json

    business = Business(

        name=data.get("name"),

        description=data.get("description"),

        phone=data.get("phone"),

        email=data.get("email")

    )

    db.add(business)

    db.commit()

    db.refresh(business)

    db.close()

    return jsonify({

        "success": True,

        "business_id": business.id,

        "message": "Business created successfully."

    })
