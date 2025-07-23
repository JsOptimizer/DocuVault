from flask import Blueprint, jsonify

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
    data = {"name": "pau", "age": 43}
    return (
        jsonify(
            {
                "status": "success",
                "message": "User registered successfully.",
                "data": data,
            }
        ),
        200,
    )
