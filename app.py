"""
1. make sure you have sql alchemy installed with `pip install -U Flask-SQLAlchemy`
2. run `python .\database.py`
3. run `python .\create_tables.py`
4. run `python .\create_animal.py`
5. run "python app.py"
6. Running on http://127.0.0.1:5000
"""
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
    data = Animal.query.all()[0]
    print(data)
    return jsonify(data.to_dict()), 200


if __name__ == "__main__":
    app.run(debug=True)