from flask import Flask

from routes.business import business_bp
from routes.employee import employee_bp
from routes.chat import chat_bp

app = Flask(__name__)

app.register_blueprint(business_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(chat_bp)


@app.route("/")
def home():
    return {
        "app": "Orbit.AI",
        "status": "running"
    }


if __name__ == "__main__":
    app.run(debug=True)
