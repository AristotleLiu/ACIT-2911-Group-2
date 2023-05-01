from database import db
from pathlib import Path
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.instance_path = Path(".").resolve()
db.init_app(app)