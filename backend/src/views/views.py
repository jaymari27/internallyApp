from app import app
from flask import json, Blueprint
from models.thoughtmodel import ThoughtModel

@app.route('/thoughts', methods=['GET'])
def all_thoughts():
    return json.dumps(ThoughtModel.query.all())