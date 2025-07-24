import datetime
from pprint import pprint

from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash

from flaskr.extension.core import db
from flaskr.models.user import User

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=("GET", "POST"))
def register():
    """
    Register a new user.
    ---
    responses:
      200:
        description: Registration successful
        content:
          application/json:
            example:
              status: "success"
              message: "User registered successfully."
    """
    data = request.get_json()
    print(f"entry data {data}")

    user = User(
        username=data["username"],
        email=data["email"],
        password_hash=generate_password_hash(data["password"]),
    )
    db.session.add(user)
    db.session.commit()

    pprint(data)
    return (
        jsonify(
            {
                "status": "success",
                "message": "User registered successfully.",
                "data": {
                    "username": data["username"],
                    "email": data["email"],
                    "password": generate_password_hash(data["password"]),
                },
            }
        ),
        200,
    )
