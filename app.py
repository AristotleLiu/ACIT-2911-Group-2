from database import db
from pathlib import Path
from flask import Flask, jsonify, render_template, request

from animal import Animal

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.instance_path = Path(".").resolve()
db.init_app(app)

@app.route("/")
def home():
    data = Animal.query.all()
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)