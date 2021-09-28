from config import app, db, api, ma
from models.thoughtmodel import ThoughtModel
from resources.thoughtprocess import ThoughtProcess

from flask_restful import Api, Resource
from flask import json, jsonify, request


class ThoughtSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ThoughtModel

def db_init():
    # Try to get entry with the ID 1
    try:
        ThoughtModel.query.get(1)
    # Create database table if not existing
    except:
        db.create_all()

def query_database():
    # To get access in database
    with app.app_context():
        allThoughts = ThoughtModel.query.all()
        thought_schema = ThoughtSchema(many=True)
        output = thought_schema.dump(allThoughts)
        return jsonify(output)

def modify_thought(thought_id=-1, thought_content='', is_done='', to_delete=False):
    # Existence check
    if thought_id == -1:
        ThoughtProcess.createThought(thought_content, is_done)
    else:
        target_entry = ThoughtModel.find_by_id(thought_id)
        if to_delete == True:
            target_entry.delete_from_db()
        else:
            ThoughtProcess.editThought(thought_id, thought_content, is_done)

class get_db_access(Resource):
    db_init()
    def get(self):
        output = query_database()
        return output
    def post(self):
        thought_args = request.get_json()
        print(thought_args)
        modify_thought(**thought_args)
        return jsonify(status = 'Update success')

api.add_resource(get_db_access, '/thoughts')

if __name__ == '__main__':
    db_init()
    query_database()
    app.run(debug=True)