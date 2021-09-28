from config import app
from flask import Flask, jsonify, request
import json
from flask_restful import Resource
from models.thoughtmodel import ThoughtModel

class ThoughtProcess(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('thought_content', required=True)
    # parser.add_argument('is_done', type=bool, required=True)
    
    def createThought(thought_content, is_done):
        # existenceCheck = ThoughtModel.find_by_content(thought_content)

        # # If exists
        # if existenceCheck:
        #     return { 'message': 'A similar Thought has been posted before.' }, 400

        # If does not exist
        thought = ThoughtModel(thought_content, is_done)

        try:
            thought.save_to_db()
        except:
            return { "message": "An error occurred inserting the data." }, 500
        
        # Successfully saved to table
        return thought.json(), 201
    
    def editThought(thought_id, thought_content='', is_done=''):
        editing = ThoughtModel.find_by_id(thought_id)

        if thought_content=='':
            editing.is_done = is_done
        if is_done == '':
            editing.thought_content = thought_content
        
        try:
            editing.save_to_db()
        except:
            return { 'message': 'An error occurred updating the data.' }, 500
        
        return editing.json(), 201

    def deleteThought(thought_id):
        thought = ThoughtModel.find_by_id(thought_id)
        thought.delete_from_db()
        
        return { 'message': 'Thought deleted' }

        